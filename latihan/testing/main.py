import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# --- 1. Siapkan Dataset Sederhana ---
# Setiap baris adalah daftar gejala, dan elemen terakhir adalah penyakitnya.
data_gejala = [
    ['demam', 'sakit kepala', 'nyeri otot', 'flu'],
    ['demam', 'ruam', 'sakit kepala', 'demam berdarah'],
    ['sakit perut', 'mual', 'diare', 'maag'],
    ['batuk', 'hidung tersumbat', 'sakit tenggorokan', 'pilek'],
    ['sakit kepala', 'mual', 'pusing', 'migrain'],
    ['sakit kepala', 'demam', 'batuk', 'flu'],
    ['ruam', 'gatal', 'kulit kering', 'eksim'],
    ['batuk', 'demam', 'sesak napas', 'pneumonia']
]

# Pisahkan gejala dan penyakit dari dataset
gejala = [' '.join(d[:-1]) for d in data_gejala]
penyakit = [d[-1] for d in data_gejala]

# --- 2. Vektorisasikan Data Teks ---
# Mengubah teks gejala menjadi representasi numerik yang bisa dipahami model
vectorizer = TfidfVectorizer()
fitur_gejala = vectorizer.fit_transform(gejala)

# --- 3. Latih Model Naive Bayes ---
model_penyakit = MultinomialNB()
model_penyakit.fit(fitur_gejala, penyakit)

# --- 4. Fungsi untuk Memprediksi Penyakit ---
def prediksi_penyakit(gejala_input):
    """
    Memprediksi penyakit berdasarkan gejala yang dimasukkan pengguna.
    """
    # Ubah input gejala menjadi format yang sama dengan data latih
    gejala_input_vektor = vectorizer.transform([gejala_input])
    
    # Lakukan prediksi
    prediksi = model_penyakit.predict(gejala_input_vektor)
    
    # Dapatkan probabilitas prediksi
    probabilitas = model_penyakit.predict_proba(gejala_input_vektor)
    probabilitas_maks = np.max(probabilitas)
    
    return prediksi[0], probabilitas_maks * 100

# --- 5. Interaksi dengan Pengguna ---
if __name__ == "__main__":
    print("Selamat datang di Diagnosis AI Sederhana!")
    print("Masukkan gejala-gejala yang Anda rasakan, dipisahkan dengan spasi (contoh: 'demam sakit kepala').")
    
    gejala_pengguna = input("Gejala Anda: ")
    
    # Pastikan pengguna memasukkan sesuatu
    if gejala_pengguna.strip() == '':
        print("Anda belum memasukkan gejala.")
    else:
        # Lakukan prediksi
        hasil_prediksi, akurasi = prediksi_penyakit(gejala_pengguna)
        
        print("\n--- Hasil Prediksi ---")
        print(f"Berdasarkan gejala yang Anda masukkan, kemungkinan penyakit Anda adalah: {hasil_prediksi.upper()}")
        print(f"Dengan tingkat keyakinan: {akurasi:.2f}%")
        print("\n*DISCLAIMER: Ini hanyalah prediksi dari model AI sederhana. Selalu konsultasikan dengan dokter untuk diagnosis yang akurat.")