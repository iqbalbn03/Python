import streamlit as st
import os
import time
from Crypto.Cipher import DES, Blowfish
import matplotlib.pyplot as plt
import pandas as pd

# =======================================================
# CONFIG & CUSTOM CSS (MODERN UI FINAL)
# =======================================================
st.set_page_config(page_title="Crypto Benchmark", page_icon="🔐", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #e0e0e0;
    }

    /* 1. Background Gradient Global */
    .stApp {
        background: radial-gradient(circle at 10% 20%, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }

    /* 2. MAGIC CSS: Target Kolom Kanan untuk Glass Effect */
    div[data-testid="column"]:nth-of-type(2) > div {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* 3. Style untuk Kartu Info (Kolom Kiri) */
    .info-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        height: 100%;
    }

    /* 4. Unified Box: Kotak Key yang Menyatu */
    .unified-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 15px 20px;
        margin-bottom: 12px;
        transition: border 0.3s ease;
    }
    
    .unified-box:hover {
        border: 1px solid rgba(0, 210, 255, 0.5);
    }

    .key-label {
        color: #e0e0e0;
        font-size: 14px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .key-value {
        color: #00d2ff;
        background: rgba(0, 210, 255, 0.1);
        padding: 5px 10px;
        border-radius: 6px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 15px;
        letter-spacing: 1px;
    }

    /* Title Styling */
    .hero-title {
        font-size: 42px; font-weight: 700;
        background: -webkit-linear-gradient(45deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; margin-bottom: 10px;
    }
    
    .hero-subtitle {
        text-align: center; color: #a8b3cf; font-size: 18px; font-weight: 300; margin-bottom: 40px;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        border: none; color: white; padding: 15px 32px;
        font-size: 16px; font-weight: 600; border-radius: 12px;
        cursor: pointer; transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 210, 255, 0.5);
    }
    
    /* Metrics Styling */
    div[data-testid="stMetricValue"] {
        font-size: 24px; color: #00d2ff;
    }
</style>
""", unsafe_allow_html=True)

# =======================================================
# LOGIKA PROGRAM (ENKRIPSI & DEKRIPSI)
# =======================================================
def generate_file(filename, size_mb):
    with open(filename, "wb") as f:
        f.write(os.urandom(size_mb * 1024 * 1024))

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
# HEADER UI
# =======================================================
st.markdown("<div class='hero-title'>🔐 DES vs Blowfish</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>High-Performance Encryption Benchmark Dashboard</div>", unsafe_allow_html=True)

# =======================================================
# LAYOUT 2 KOLOM
# =======================================================
col1, col2 = st.columns([1.5, 1])

# --- KOLOM 1: Info ---
with col1:
    st.markdown("""
    <div class='info-card'>
        <h3>ℹ️ Tentang Aplikasi</h3>
        <p style='line-height: 1.6;'>
            Aplikasi ini dirancang untuk menguji performa algoritma kriptografi klasik secara <b>real-time</b>.
            Sistem akan membuat file <i>dummy</i> (1MB, 5MB, 10MB) dan mengukur:
        </p>
        <ul style='margin-bottom:0;'>
            <li>⚡ <b>Kecepatan Enkripsi</b> (Encryption Latency)</li>
            <li>⚡ <b>Kecepatan Dekripsi</b> (Decryption Latency)</li>
            <li>📦 <b>Efisiensi Storage</b> (Ciphertext Size)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- KOLOM 2: Konfigurasi ---
with col2:
    st.markdown("<h3 style='margin-bottom: 15px;'>⚙️ Konfigurasi Key</h3>", unsafe_allow_html=True)
    
    mode = st.radio(
        "Pilih Skenario Pengujian:",
        ("Fair Comparison (8 byte)", "Unfair Comparison (DES 8 vs BF 16)"),
        label_visibility="collapsed"
    )

    if mode == "Fair Comparison (8 byte)":
        DES_KEY = b"12345678"
        BF_KEY = b"12345678"
    else:
        DES_KEY = b"12345678"
        BF_KEY = b"A1B2C3D4E5F60718"
    
    st.markdown(f"""
    <div style='margin-top: 20px;'>
        <div class='unified-box'>
            <span class='key-label'>🗝️ DES Key</span>
            <span class='key-value'>{DES_KEY.decode()}</span>
        </div>
        <div class='unified-box'>
            <span class='key-label'>🐡 Blowfish Key</span>
            <span class='key-value'>{BF_KEY.decode()}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =======================================================
# TOMBOL & PROSES BENCHMARK
# =======================================================
st.write("") # Spacer

# Format Kolom Tombol
_, btn_col, _ = st.columns([5, 2, 5]) 

with btn_col:
    start_btn = st.button("🚀 JALANKAN BENCHMARK")

sizes = [1, 5, 10]
results = []

if start_btn:
    with st.spinner("⏳ Sedang melakukan kalkulasi kriptografi..."):
        progress_bar = st.progress(0)
        
        for idx, size in enumerate(sizes):
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
            progress_bar.progress(int((idx + 1) / len(sizes) * 100))
        
        time.sleep(0.5) 
        progress_bar.empty()

    # --- HASIL ANALISIS ---
    avg_des_enc = sum([r["des_enc"] for r in results]) / len(results)
    avg_bf_enc = sum([r["bf_enc"] for r in results]) / len(results)
    avg_des_dec = sum([r["des_dec"] for r in results]) / len(results)
    avg_bf_dec = sum([r["bf_dec"] for r in results]) / len(results)

    winner_enc = "DES" if avg_des_enc < avg_bf_enc else "Blowfish"
    speedup_enc = (max(avg_des_enc, avg_bf_enc) / min(avg_des_enc, avg_bf_enc)) 
    
    st.markdown("---")
    st.markdown("<h2 style='text-align:center; margin-bottom:30px;'>📊 Analisis Performa</h2>", unsafe_allow_html=True)

    # 1. Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("🏆 Tercepat (Enc)", winner_enc, delta=f"{speedup_enc:.2f}x Lebih Cepat")
    with m2: st.metric("Rata-rata DES (Enc)", f"{avg_des_enc:.4f} s")
    with m3: st.metric("Rata-rata Blowfish (Enc)", f"{avg_bf_enc:.4f} s")
    with m4: st.metric("Ciphertext Overlay", f"+{results[0]['des_ct'] - (results[0]['size']*1024*1024)} Bytes")

    # 2. Charts
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    plt.style.use('dark_background')
    plt.rcParams.update({
        "axes.facecolor": "#00000000",
        "figure.facecolor": "#00000000",
        "grid.color": "#444444",
        "text.color": "white"
    })
    sizes_plot = [r["size"] for r in results]

    with c1:
        st.markdown("<div class='info-card' style='text-align:center;'><h4>📉 Kecepatan Enkripsi</h4>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(sizes_plot, [r["des_enc"] for r in results], marker='o', color='#00d2ff', linewidth=2, label="DES")
        ax.plot(sizes_plot, [r["bf_enc"] for r in results], marker='o', color='#ff007f', linewidth=2, label="Blowfish")
        ax.set_xlabel("Ukuran File (MB)")
        ax.set_ylabel("Waktu (Detik)")
        ax.legend(frameon=False)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='info-card' style='text-align:center;'><h4>📉 Kecepatan Dekripsi</h4>", unsafe_allow_html=True)
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        ax2.plot(sizes_plot, [r["des_dec"] for r in results], marker='o', color='#00d2ff', linewidth=2, label="DES")
        ax2.plot(sizes_plot, [r["bf_dec"] for r in results], marker='o', color='#ff007f', linewidth=2, label="Blowfish")
        ax2.set_xlabel("Ukuran File (MB)")
        ax2.set_ylabel("Waktu (Detik)")
        ax2.legend(frameon=False)
        ax2.grid(True, linestyle='--', alpha=0.5)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        st.pyplot(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

    # 3. Data Detail & KESIMPULAN AKHIR
    with st.expander("📂 Lihat Data Detail & Kesimpulan", expanded=True):
        # HAPUS WRAPPER DIV DI SINI YANG MEMBUAT KOTAK KOSONG
        
        # Tabel Data
        df = pd.DataFrame(results)
        df_display = df.rename(columns={
            "size": "Size (MB)",
            "des_enc": "DES Enc (s)", "des_dec": "DES Dec (s)",
            "bf_enc": "BF Enc (s)", "bf_dec": "BF Dec (s)",
            "des_ct": "DES Size (B)", "bf_ct": "BF Size (B)"
        })
        st.dataframe(df_display, use_container_width=True)

        # --- KESIMPULAN AKHIR (PENTING) ---
        st.markdown(f"""
        <div class='info-card' style='margin-top: 20px;'>
            <h3 style='color: #00d2ff;'>📝 Kesimpulan Akhir</h3>
            <ul>
                <li>Algoritma yang lebih cepat dalam pengujian ini adalah <b>{winner_enc}</b>.</li>
                <li>Blowfish menggunakan blok 64-bit sama seperti DES, tetapi algoritmanya dioptimalkan untuk prosesor modern (operasi XOR dan Addition yang efisien).</li>
                <li>Secara keamanan, <b>Blowfish</b> jauh lebih disarankan daripada DES karena key-length yang fleksibel (hingga 448 bit) dan resistan terhadap cryptanalysis dasar, sedangkan DES rentan terhadap <i>Brute Force</i>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)