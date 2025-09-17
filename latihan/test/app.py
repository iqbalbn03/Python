import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="AI Prediksi Penyakit",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Fungsi untuk Melatih Model (dengan cache agar tidak perlu melatih ulang setiap kali) ---
@st.cache_data
def load_data_and_train_model():
    # 1. Memuat dan Mempersiapkan Data (Dataset asli dalam Bahasa Inggris)
    try:
        df = pd.read_csv('dataset.csv')
    except FileNotFoundError:
        st.error("Error: File 'dataset.csv' tidak ditemukan. Pastikan file tersebut ada di folder yang sama dengan aplikasi ini.")
        return None, None, None, None

    df.drop_duplicates(inplace=True)
    df.columns = df.columns.str.strip()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()

    df.fillna('No_Symptom', inplace=True)
    df['symptoms'] = df.iloc[:, 1:].values.tolist()
    df_final = df[['Disease', 'symptoms']]

    # 2. Mengubah Data Gejala (Encoding)
    symptoms_encoded = pd.get_dummies(df_final['symptoms'].apply(pd.Series).stack()).groupby(level=0).sum()
    data = pd.concat([df_final['Disease'], symptoms_encoded], axis=1)

    # 3. Memisahkan Data
    X = data.drop('Disease', axis=1)
    y = data['Disease']
    
    # Membuat dan melatih LabelEncoder untuk nama penyakit
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # 4. Melatih Model AI (Random Forest)
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y_encoded)
    
    # Mengambil daftar gejala untuk dropdown (tetap dalam bahasa Inggris tapi format diperbaiki)
    daftar_gejala = [symptom.replace('_', ' ').title() for symptom in X.columns]
    
    return model, X.columns, daftar_gejala, label_encoder

# --- Memuat Model dan Data ---
model, feature_names, daftar_gejala, label_encoder = load_data_and_train_model()

# --- Antarmuka Pengguna (UI) dengan Streamlit ---
if model:
    st.title("🩺 AI Prediksi Penyakit")
    st.write(
        "Pilih gejala yang Anda rasakan dari daftar di bawah ini. "
        "AI akan membantu memprediksi kemungkinan penyakit Anda berdasarkan data yang ada."
    )
    st.info("**Penting:** Aplikasi ini adalah purwarupa dan tidak menggantikan diagnosis medis profesional. Selalu konsultasikan dengan dokter.")

    # Dropdown untuk memilih gejala
    gejala_terpilih_user = st.multiselect(
        "Pilih gejala Anda:",
        options=sorted(daftar_gejala)
    )

    # Tombol untuk prediksi
    if st.button("Prediksi Penyakit Saya"):
        if gejala_terpilih_user:
            with st.spinner('Menganalisis gejala...'):
                # Mengubah input user ke format yang sesuai dengan model
                gejala_input_user = [gejala.lower().replace(' ', '_') for gejala in gejala_terpilih_user]
                
                input_encoded = pd.DataFrame(columns=feature_names)
                input_encoded.loc[0] = 0
                for symptom in gejala_input_user:
                    if symptom in input_encoded.columns:
                        input_encoded.loc[0, symptom] = 1

                # Melakukan prediksi
                prediksi_encoded = model.predict(input_encoded)
                probabilitas = model.predict_proba(input_encoded)
                
                # Mengubah hasil prediksi kembali ke nama penyakit asli
                prediksi_penyakit = label_encoder.inverse_transform(prediksi_encoded)
                
                st.success(f"**Prediksi Penyakit:** {prediksi_penyakit[0]}")
                st.info(f"**Tingkat Keyakinan:** {np.max(probabilitas) * 100:.2f}%")

                st.write("---")
                st.subheader("Gejala yang Anda Pilih:")
                for gejala in gejala_terpilih_user:
                    st.write(f"- {gejala}")
        else:
            st.warning("Mohon pilih setidaknya satu gejala untuk diprediksi.")

# --- Sidebar ---
st.sidebar.header("Tentang Aplikasi")
st.sidebar.info(
    "Aplikasi ini menggunakan model Machine Learning (Random Forest) untuk memprediksi "
    "penyakit berdasarkan gejala yang dimasukkan. Dataset yang digunakan berasal dari "
    "repositori GitHub hemasriram111/disease-symptom-dataset."
)
st.sidebar.header("Cara Penggunaan")
st.sidebar.markdown(
    """
    1.  Pilih satu atau lebih gejala dari kotak pilihan.
    2.  Klik tombol **'Prediksi Penyakit Saya'**.
    3.  Hasil prediksi dan tingkat keyakinan akan muncul.
    """
)