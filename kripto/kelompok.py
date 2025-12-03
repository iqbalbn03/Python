import streamlit as st
import os
import time
from Crypto.Cipher import DES, Blowfish
import matplotlib.pyplot as plt

# =======================================================
# CUSTOM CSS 
# =======================================================
st.markdown("""
<style>
    body {
        background-color: #0e1117;
    }
    .main-container {
        padding: 20px;
        background: #161a23;
        border-radius: 18px;
        box-shadow: 0px 0px 12px rgba(255,255,255,0.05);
        margin-bottom: 25px;
    }
    .title {
        text-align: center;
        font-size: 35px !important;
        font-weight: 700;
        color: #f8f9fa !important;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #a8b3cf;
        font-size: 17px;
        margin-top: -10px;
        margin-bottom: 25px;
    }
    .card {
        padding: 18px;
        background: #1d2230;
        border-radius: 14px;
        margin-bottom: 20px;
        border: 1px solid #2c3344;
    }
    .stButton>button {
        width: 100%;
        background: #3b82f6;
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# =======================================================
# Fungsi: Generate File
# =======================================================
def generate_file(filename, size_mb):
    with open(filename, "wb") as f:
        f.write(os.urandom(size_mb * 1024 * 1024))

# =======================================================
# DES
# =======================================================
def encrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    pad_len = 8 - (len(data) % 8)
    data += bytes([pad_len]) * pad_len
    return cipher.encrypt(data)

def decrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    result = cipher.decrypt(data)
    pad_len = result[-1]
    return result[:-pad_len]

# =======================================================
# Blowfish
# =======================================================
def encrypt_blowfish(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    pad_len = 8 - (len(data) % 8)
    data += bytes([pad_len]) * pad_len
    return cipher.encrypt(data)

def decrypt_blowfish(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    result = cipher.decrypt(data)
    pad_len = result[-1]
    return result[:-pad_len]

# =======================================================
# Benchmark
# =======================================================
def benchmark(enc, dec, key, data, trials=5):
    enc_times = []
    dec_times = []
    ct_size = 0

    for _ in range(trials):
        start = time.time()
        ciphertext = enc(key, data)
        enc_times.append(time.time() - start)

        start = time.time()
        dec(key, ciphertext)
        dec_times.append(time.time() - start)

        ct_size = len(ciphertext)

    return sum(enc_times)/trials, sum(dec_times)/trials, ct_size

# =======================================================
# HEADER
# =======================================================
st.markdown("<div class='title'>🔐 Benchmark DES vs Blowfish</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Automatic encryption benchmark for DES and Blowfish</div>", unsafe_allow_html=True)

# =======================================================
# Deskripsi
# =======================================================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
Aplikasi ini otomatis membuat file berukuran **1 MB, 5 MB, dan 10 MB**, lalu melakukan benchmark:

- ⚡ Waktu Enkripsi  
- ⚡ Waktu Dekripsi  
- 📦 Ukuran Ciphertext  
- 📈 Grafik Visual  
- 🧠 Analisis Otomatis  
""")
    st.markdown("</div>", unsafe_allow_html=True)

# =======================================================
# PILIHAN MODE KEY
# =======================================================
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.subheader("🗝️ Pengaturan Key")

mode = st.radio(
    "Pilih Mode Key:",
    (
        "Fair Comparison (keduanya 8 byte)",
        "Unfair Comparison (DES 8 byte vs Blowfish 16 byte)"
    )
)

if mode == "Fair Comparison (keduanya 8 byte)":
    DES_KEY = b"12345678"
    BF_KEY = b"12345678"
else:
    DES_KEY = b"12345678"
    BF_KEY = b"A1B2C3D4E5F60718"

st.markdown(f"""
<div class='card'>
<b>DES Key:</b> {DES_KEY}<br>
<b>Blowfish Key:</b> {BF_KEY}
</div>
""", unsafe_allow_html=True)

sizes = [1, 5, 10]
results = []

# =======================================================
# BUTTON START
# =======================================================
if st.button("Mulai Benchmark 🚀"):
    st.markdown("<div class='card'>⏳ Sedang melakukan pengujian...</div>", unsafe_allow_html=True)

    for size in sizes:
        filename = f"auto_{size}MB.bin"
        if not os.path.exists(filename):
            generate_file(filename, size)

        with open(filename, "rb") as f:
            data = f.read()

        des_enc, des_dec, des_ct = benchmark(encrypt_des, decrypt_des, DES_KEY, data)
        bf_enc, bf_dec, bf_ct = benchmark(encrypt_blowfish, decrypt_blowfish, BF_KEY, data)

        results.append({
            "size": size,
            "des_enc": des_enc,
            "des_dec": des_dec,
            "bf_enc": bf_enc,
            "bf_dec": bf_dec,
            "des_ct": des_ct,
            "bf_ct": bf_ct
        })

    st.success("Benchmark selesai!")

    # =======================================================
    # Tabel
    # =======================================================
    st.subheader("📊 Hasil Benchmark")
    st.table({
        "Ukuran (MB)": [r["size"] for r in results],
        "DES Enc (s)": [r["des_enc"] for r in results],
        "DES Dec (s)": [r["des_dec"] for r in results],
        "BF Enc (s)":  [r["bf_enc"] for r in results],
        "BF Dec (s)":  [r["bf_dec"] for r in results],
        "DES CT (B)":  [r["des_ct"] for r in results],
        "BF CT (B)":   [r["bf_ct"] for r in results],
    })

    # =======================================================
    # Grafik Enkripsi
    # =======================================================
    st.subheader("📈 Grafik Enkripsi")

    sizes_plot = [r["size"] for r in results]
    des_plot = [r["des_enc"] for r in results]
    bf_plot = [r["bf_enc"] for r in results]

    fig, ax = plt.subplots()
    ax.plot(sizes_plot, des_plot, marker='o', label="DES")
    ax.plot(sizes_plot, bf_plot, marker='o', label="Blowfish")
    ax.set_title("Waktu Enkripsi")
    ax.set_xlabel("Ukuran File (MB)")
    ax.set_ylabel("Detik")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # =======================================================
    # Grafik Dekripsi
    # =======================================================
    st.subheader("📈 Grafik Dekripsi")

    des_dec_plot = [r["des_dec"] for r in results]
    bf_dec_plot = [r["bf_dec"] for r in results]

    fig2, ax2 = plt.subplots()
    ax2.plot(sizes_plot, des_dec_plot, marker='o', label="DES")
    ax2.plot(sizes_plot, bf_dec_plot, marker='o', label="Blowfish")
    ax2.set_title("Waktu Dekripsi")
    ax2.set_xlabel("Ukuran File (MB)")
    ax2.set_ylabel("Detik")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

    # =======================================================
    # Analisis Naratif
    # =======================================================
    st.subheader("📝 Analisis Otomatis")

    avg_des_enc = sum([r["des_enc"] for r in results]) / len(results)
    avg_bf_enc = sum([r["bf_enc"] for r in results]) / len(results)

    avg_des_dec = sum([r["des_dec"] for r in results]) / len(results)
    avg_bf_dec = sum([r["bf_dec"] for r in results]) / len(results)

    # Penjelasan
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("### 1. Enkripsi – Siapa lebih cepat?")
    st.write("→ **DES lebih cepat**" if avg_des_enc < avg_bf_enc else "→ **Blowfish lebih cepat**")

    st.write("### 2. Dekripsi – Siapa lebih cepat?")
    st.write("→ **DES lebih cepat**" if avg_des_dec < avg_bf_dec else "→ **Blowfish lebih cepat**")

    st.write("### 3. Penjelasan Singkat")
    st.write("""
- DES: Struktur Feistel 16 ronde, lebih sederhana.  
- Blowfish: 16 ronde juga, tetapi operasi lebih ringan & efisien.  
- Secara umum, Blowfish sering unggul pada CPU modern.
""")

    st.write("### 4. Kesimpulan")
    st.write("""
- Fokus kecepatan → lihat hasil benchmark.  
- Fokus keamanan → Blowfish jauh lebih aman.  
""")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
