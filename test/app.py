import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="AI Prediksi Penyakit",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Fungsi untuk Memuat dan Melatih Model ---
@st.cache_data
def load_data_and_train_models():
    # 1. Memuat dan Mempersiapkan Data
    df = pd.read_csv('dataset.csv')
    df.drop_duplicates(inplace=True)
    df.columns = df.columns.str.strip()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
    df.fillna('No_Symptom', inplace=True)

    df['symptoms'] = df.iloc[:, 1:].values.tolist()
    df_final = df[['Disease', 'symptoms']]

    # 2. Encoding Gejala
    symptoms_encoded = pd.get_dummies(df_final['symptoms'].apply(pd.Series).stack()).groupby(level=0).sum()
    data = pd.concat([df_final['Disease'], symptoms_encoded], axis=1)

    X = data.drop('Disease', axis=1)
    y = data['Disease']

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # 3. Split Data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # 4. Melatih Dua Model
    model_dt = DecisionTreeClassifier(random_state=42)
    model_rf = RandomForestClassifier(random_state=42)

    model_dt.fit(X_train, y_train)
    model_rf.fit(X_train, y_train)

    # 5. Evaluasi Awal
    y_pred_dt = model_dt.predict(X_test)
    y_pred_rf = model_rf.predict(X_test)

    metrics = {
        "Decision Tree": {
            "Akurasi": accuracy_score(y_test, y_pred_dt),
            "Presisi": precision_score(y_test, y_pred_dt, average='macro'),
            "Recall": recall_score(y_test, y_pred_dt, average='macro'),
            "F1-Score": f1_score(y_test, y_pred_dt, average='macro')
        },
        "Random Forest": {
            "Akurasi": accuracy_score(y_test, y_pred_rf),
            "Presisi": precision_score(y_test, y_pred_rf, average='macro'),
            "Recall": recall_score(y_test, y_pred_rf, average='macro'),
            "F1-Score": f1_score(y_test, y_pred_rf, average='macro')
        }
    }

    daftar_gejala = [symptom.replace('_', ' ').title() for symptom in X.columns]
    return model_dt, model_rf, X.columns, daftar_gejala, label_encoder, metrics

# --- Memuat Model dan Data ---
model_dt, model_rf, feature_names, daftar_gejala, label_encoder, metrics = load_data_and_train_models()

# --- UI Utama ---
st.title("🩺 AI Prediksi Penyakit")
st.write("Pilih gejala Anda, lalu sistem akan memprediksi penyakit berdasarkan dua model: Decision Tree dan Random Forest.")

gejala_terpilih_user = st.multiselect(
    "Pilih gejala Anda:",
    options=sorted(daftar_gejala)
)

# Tombol Prediksi
if st.button("Prediksi Penyakit Saya"):
    if gejala_terpilih_user:
        gejala_input_user = [g.lower().replace(' ', '_') for g in gejala_terpilih_user]
        input_encoded = pd.DataFrame(columns=feature_names)
        input_encoded.loc[0] = 0
        for symptom in gejala_input_user:
            if symptom in input_encoded.columns:
                input_encoded.loc[0, symptom] = 1

        pred_dt = model_dt.predict(input_encoded)
        pred_rf = model_rf.predict(input_encoded)

        pred_dt_label = label_encoder.inverse_transform(pred_dt)[0]
        pred_rf_label = label_encoder.inverse_transform(pred_rf)[0]

        st.success(f"**Decision Tree Prediction:** {pred_dt_label}")
        st.success(f"**Random Forest Prediction:** {pred_rf_label}")
        st.write("---")
        st.subheader("Perbandingan Kinerja Model (Validation Set)")
        st.dataframe(pd.DataFrame(metrics).T)
    else:
        st.warning("Pilih minimal satu gejala untuk melakukan prediksi.")

st.sidebar.header("Tentang Aplikasi")
st.sidebar.info("Aplikasi ini membandingkan dua model Machine Learning: Decision Tree dan Random Forest dalam memprediksi penyakit berdasarkan gejala.")
