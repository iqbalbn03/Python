import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="AI Prediksi Penyakit dengan Perbandingan Model",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Fungsi untuk Melatih Model (dengan cache) ---
@st.cache_data
def load_data_and_train_models():
    """
    Memuat data, melakukan preprocessing, melatih berbagai model ML, 
    dan menghitung metrik kinerja termasuk Akurasi, Presisi, Recall, dan F1-Score.
    """
    try:
        # Asumsi file 'dataset.csv' berada di lokasi yang sama
        df = pd.read_csv('dataset.csv')
    except FileNotFoundError:
        st.error("Error: File 'dataset.csv' tidak ditemukan. Pastikan file tersebut ada di folder yang sama dengan aplikasi ini.")
        # Mengembalikan None untuk mencegah error lebih lanjut
        return None, None, None, None, None, None, None, None, None, None, None, None

    # Preprocessing data
    df.drop_duplicates(inplace=True)
    df.columns = df.columns.str.strip()
    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()

    df.fillna('No_Symptom', inplace=True)
    # Menggabungkan semua kolom gejala (Symptom_1, Symptom_2, dst) menjadi satu kolom 'symptoms'
    df['symptoms'] = df.iloc[:, 1:].values.tolist()
    df_final = df[['Disease', 'symptoms']]

    # Encoding gejala (One-Hot Encoding)
    # Membuat kolom biner untuk setiap gejala unik
    symptoms_encoded = pd.get_dummies(df_final['symptoms'].apply(pd.Series).stack()).groupby(level=0).sum()
    data = pd.concat([df_final['Disease'], symptoms_encoded], axis=1)

    # Memisahkan fitur (X) dan target (y)
    X = data.drop('Disease', axis=1)
    y = data['Disease']
    
    # Encoding label penyakit (Label Encoding)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Split data untuk evaluasi
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

    # Daftar model yang akan dibandingkan
    # HANYA menyertakan Random Forest, Support Vector Machine, dan Decision Tree
    models = {
        'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
        'Support Vector Machine': SVC(random_state=42, probability=True),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
    }

    # Inisialisasi dictionary untuk menyimpan hasil
    trained_models = {}
    accuracy_results = {}
    cv_scores = {}
    prediction_times = {}
    # Metrik Klasifikasi Baru (Weighted Average)
    precision_results = {}
    recall_results = {}
    f1_results = {}
    
    for name, model in models.items():
        # Cross-validation (5-fold)
        cv_score = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        cv_scores[name] = cv_score
        
        # Training model
        start_time = datetime.now()
        model.fit(X_train, y_train)
        training_time = (datetime.now() - start_time).total_seconds()
        
        # Prediksi
        y_pred = model.predict(X_test)
        
        # Menghitung Akurasi
        accuracy = accuracy_score(y_test, y_pred)
        
        # Menghitung metrik Presisi, Recall, dan F1-Score menggunakan Classification Report
        # Menggunakan weighted avg untuk masalah multi-kelas
        report = classification_report(
            y_test, y_pred, 
            target_names=label_encoder.classes_, 
            output_dict=True, 
            zero_division=0 # Mengatasi pembagian nol jika ada kelas yang tidak terprediksi
        )
        
        precision_results[name] = report['weighted avg']['precision']
        recall_results[name] = report['weighted avg']['recall']
        f1_results[name] = report['weighted avg']['f1-score']
        
        # Menyimpan hasil
        trained_models[name] = model
        accuracy_results[name] = accuracy
        prediction_times[name] = training_time

    # Mengambil daftar gejala untuk dropdown
    daftar_gejala = [symptom.replace('_', ' ').title() for symptom in X.columns]
    
    # Mengembalikan semua data yang diperlukan, termasuk metrik baru
    return (
        trained_models, accuracy_results, cv_scores, X.columns, daftar_gejala, 
        label_encoder, prediction_times, X_test, y_test, 
        precision_results, recall_results, f1_results
    )

# --- Memuat Model dan Data ---
(
    trained_models, accuracy_results, cv_scores, feature_names, daftar_gejala, 
    label_encoder, prediction_times, X_test, y_test, 
    precision_results, recall_results, f1_results
) = load_data_and_train_models()

# --- Antarmuka Pengguna (UI) dengan Streamlit ---
if trained_models:
    st.title("🩺 AI Prediksi Penyakit dengan Perbandingan Model")
    
    # Tab untuk navigasi
    tab1, tab2, tab3 = st.tabs(["🔍 Prediksi Penyakit", "📊 Perbandingan Model", "ℹ️ Informasi Dataset"])

    with tab1:
        st.header("Prediksi Penyakit Berdasarkan Gejala")
        st.write(
            "Pilih gejala yang Anda rasakan dari daftar di bawah ini. "
            "Prediksi akan dijalankan secara otomatis menggunakan Random Forest, SVM, dan Decision Tree."
        )
        st.info("**Penting:** Aplikasi ini adalah purwarupa dan tidak menggantikan diagnosis medis profesional. Selalu konsultasikan dengan dokter.")

        # Menghilangkan pemilihan model (selectbox)
        # selected_model = st.selectbox(...)

        # Dropdown untuk memilih gejala
        gejala_terpilih_user = st.multiselect(
            "Pilih gejala Anda:",
            options=sorted(daftar_gejala),
            help="Pilih satu atau lebih gejala yang Anda alami"
        )

        # Tombol untuk prediksi
        if st.button("Prediksi Penyakit Saya", type="primary"):
            if gejala_terpilih_user:
                
                # Mengubah input user ke format yang sesuai dengan model
                gejala_input_user = [gejala.lower().replace(' ', '_') for gejala in gejala_terpilih_user]
                
                input_encoded = pd.DataFrame(columns=feature_names)
                input_encoded.loc[0] = 0
                for symptom in gejala_input_user:
                    if symptom in input_encoded.columns:
                        input_encoded.loc[0, symptom] = 1

                st.subheader("Hasil Prediksi dari Tiga Model")
                
                # Mengiterasi melalui setiap model untuk prediksi
                for model_name, model in trained_models.items():
                    with st.expander(f"Hasil Prediksi: {model_name}"):
                        with st.spinner(f'Menganalisis gejala dengan {model_name}...'):
                            
                            # Prediksi penyakit utama
                            prediksi_encoded = model.predict(input_encoded)
                            
                            # Menghitung probabilitas (jika model mendukung)
                            probabilitas = None
                            keyakinan_str = "N/A"
                            try:
                                probabilitas = model.predict_proba(input_encoded)
                                keyakinan_str = f"{np.max(probabilitas) * 100:.2f}%"
                            except AttributeError:
                                st.warning("Model ini tidak menyediakan probabilitas prediksi.")

                            # Mengubah hasil prediksi kembali ke nama penyakit asli
                            prediksi_penyakit = label_encoder.inverse_transform(prediksi_encoded)
                            
                            # Menampilkan hasil
                            st.metric(
                                label="Penyakit Diprediksi", 
                                value=prediksi_penyakit[0],
                                delta=keyakinan_str, # Menggunakan delta untuk menampilkan keyakinan
                                delta_color="normal"
                            )

                            if probabilitas is not None:
                                # Menampilkan top 3 prediksi
                                top_3_indices = np.argsort(probabilitas[0])[-3:][::-1]
                                top_3_diseases = label_encoder.inverse_transform(top_3_indices)
                                top_3_probs = probabilitas[0][top_3_indices] * 100
                                
                                st.markdown("---")
                                st.write("**Top 3 Probabilitas:**")
                                top_3_df = pd.DataFrame({
                                    'Penyakit': top_3_diseases,
                                    'Probabilitas (%)': top_3_probs
                                })
                                st.table(top_3_df.style.format({'Probabilitas (%)': "{:.2f}%"}))
                
                st.write("---")
                st.subheader("Gejala yang Anda Pilih:")
                for gejala in gejala_terpilih_user:
                    st.write(f"- {gejala}")
            else:
                st.warning("Mohon pilih setidaknya satu gejala untuk diprediksi.")

    with tab2:
        st.header("📊 Perbandingan Kinerja Model")
        
        # --- TABEL PERBANDINGAN BARU DENGAN SEMUA METRIK ---
        st.subheader("Perbandingan Kinerja Model (Metrik Klasifikasi dan Efisiensi)")
        
        # Urutkan model berdasarkan akurasi
        sorted_accuracy = dict(sorted(accuracy_results.items(), key=lambda x: x[1], reverse=True))
        
        # Tabel perbandingan komprehensif (mirip format gambar)
        comparison_data_full = []
        for model_name, accuracy in sorted_accuracy.items():
            cv_mean = np.mean(cv_scores[model_name])
            cv_std = np.std(cv_scores[model_name])
            comparison_data_full.append({
                'Model': model_name,
                # Menggunakan 4 desimal untuk Akurasi, Presisi, Recall, F1-Score
                'Akurasi': f"{accuracy:.4f}",
                'Presisi': f"{precision_results[model_name]:.4f}",
                'Recall': f"{recall_results[model_name]:.4f}",
                'F1-Score': f"{f1_results[model_name]:.4f}",
                'CV Akurasi Rata-rata': f"{cv_mean:.4f}",
                'CV Std Dev': f"{cv_std:.4f}",
                'Waktu Training (s)': f"{prediction_times[model_name]:.4f}"
            })
        
        comparison_df_full = pd.DataFrame(comparison_data_full)
        st.dataframe(comparison_df_full, use_container_width=True)
        # --- AKHIR TABEL PERBANDINGAN BARU ---
        
        # Visualisasi perbandingan akurasi
        st.write("---")
        col1, col2 = st.columns(2)
        
        models_list = list(sorted_accuracy.keys())
        
        with col1:
            st.subheader("Grafik Akurasi Model")
            fig, ax = plt.subplots(figsize=(10, 6))
            accuracy_values = [sorted_accuracy[model] * 100 for model in models_list]
            
            bars = ax.bar(models_list, accuracy_values, color=plt.cm.Set3(np.linspace(0, 1, len(models_list))))
            ax.set_ylabel('Akurasi (%)')
            ax.set_xlabel('Model')
            ax.set_title('Perbandingan Akurasi Model')
            ax.tick_params(axis='x', rotation=45)
            
            # Menambahkan nilai di atas bar
            for bar, value in zip(bars, accuracy_values):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                        f'{value:.1f}%', ha='center', va='bottom')
            
            plt.tight_layout()
            st.pyplot(fig)
        
        with col2:
            st.subheader("Grafik Waktu Training")
            fig, ax = plt.subplots(figsize=(10, 6))
            times_list = [prediction_times[model] for model in models_list]
            
            bars = ax.bar(models_list, times_list, color=plt.cm.Pastel1(np.linspace(0, 1, len(models_list))))
            ax.set_ylabel('Waktu (detik)')
            ax.set_xlabel('Model')
            ax.set_title('Waktu Training Model')
            ax.tick_params(axis='x', rotation=45)
            
            # Menambahkan nilai di atas bar
            for bar, value in zip(bars, times_list):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001, 
                        f'{value:.4f}s', ha='center', va='bottom', fontsize=8)
            
            plt.tight_layout()
            st.pyplot(fig)
        
        # Cross-validation scores
        st.subheader("Hasil Deskriptif Cross-Validation (5-fold)")
        # Mengubah dari list/array score ke DataFrame untuk fungsi .describe()
        cv_df = pd.DataFrame({model: scores * 100 for model, scores in cv_scores.items()})
        st.dataframe(cv_df.describe().T, use_container_width=True) # Transpose agar lebih mudah dibaca

    with tab3:
        st.header("ℹ️ Informasi Dataset dan Model")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Teknologi yang Digunakan")
            st.markdown("""
            - **Framework**: Streamlit
            - **Machine Learning**: Scikit-learn
            - **Algoritma**:
              - Random Forest
              - Support Vector Machine
              - Decision Tree
            - **Visualisasi**: Matplotlib, Seaborn
            """)
            
            st.subheader("Metrik Evaluasi")
            st.markdown("""
            - **Akurasi**: Persentase prediksi yang benar.
            - **Presisi (Precision)**: Kemampuan model untuk tidak melabeli sampel positif yang sebenarnya negatif.
            - **Recall**: Kemampuan model untuk menemukan semua sampel positif.
            - **F1-Score**: Rata-rata harmonik dari Presisi dan Recall.
            - **Cross-Validation**: Validasi 5-fold untuk menguji konsistensi model.
            """)
        
        with col2:
            st.subheader("Spesifikasi Dataset")
            st.markdown("""
            - **Sumber**: dataset.csv
            - **Fitur**: Gejala penyakit (Symptom_1 hingga Symptom_17)
            - **Target**: Nama penyakit (Disease)
            - **Preprocessing**:
              - Penghapusan duplikat
              - Handling missing values
              - One-hot encoding gejala
              - Label encoding penyakit
            - **Catatan**: Semua metrik Presisi, Recall, dan F1-Score menggunakan *Weighted Average* karena ini adalah masalah klasifikasi multi-kelas.
            """)
            
            st.subheader("Rekomendasi Model")
            best_model = max(accuracy_results, key=accuracy_results.get)
            st.success(f"**Model Terbaik (berdasarkan Akurasi)**: {best_model} dengan akurasi {accuracy_results[best_model]*100:.2f}%")

# --- Sidebar ---
st.sidebar.header("Tentang Aplikasi")
st.sidebar.info(
    "Aplikasi ini menggunakan berbagai model Machine Learning untuk memprediksi "
    "penyakit berdasarkan gejala yang dimasukkan. Dilengkapi dengan perbandingan "
    "kinerja model untuk analisis yang komprehensif."
)

st.sidebar.header("Cara Penggunaan")
st.sidebar.markdown(
    """
    1. **Tab Prediksi**: Pilih gejala, dan ketiga model akan memberikan prediksi secara instan.
    2. **Tab Perbandingan**: Lihat performa semua model yang diuji, termasuk Akurasi, Presisi, Recall, dan F1-Score
    3. **Tab Informasi**: Pelajari tentang dataset dan teknologi
    """
)

st.sidebar.header("Statistik Model")
if trained_models:
    total_models = len(trained_models)
    best_accuracy = max(accuracy_results.values()) * 100
    best_model = max(accuracy_results, key=accuracy_results.get)
    
    st.sidebar.metric("Total Model", total_models)
    st.sidebar.metric("Akurasi Tertinggi", f"{best_accuracy:.2f}%")
    st.sidebar.metric("Model Terbaik", best_model)