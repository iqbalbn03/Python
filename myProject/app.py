import streamlit as st
import yt_dlp
import os

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="YouTube MP3 Downloader", page_icon="🎵")

st.title("🎵 YouTube ke MP3 Converter")
st.markdown("Download video satuan atau satu playlist penuh menjadi MP3.")

# --- Input User ---
col_mode1, col_mode2 = st.columns([1, 3])

with col_mode1:
    # Pilihan Mode: Satuan atau Playlist
    mode = st.radio("Pilih Mode:", ["Satuan (Single Link)", "Playlist (Full Album)"])

with col_mode2:
    url_input = st.text_input(f"Masukkan URL {mode}:", placeholder="https://youtube.com/watch?v=... atau playlist")

# --- Opsi Tambahan (Expander) ---
with st.expander("⚙️ Pengaturan Tambahan (Folder & FFmpeg)"):
    col1, col2 = st.columns(2)
    with col1:
        output_folder = st.text_input("Nama Folder Output:", value="Downloads")
    with col2:
        ffmpeg_path = st.text_input("Lokasi Folder FFmpeg (Opsional):", 
                                    placeholder=r"C:\ffmpeg\bin",
                                    help="Isi HANYA jika muncul error 'ffmpeg not found'.")

# --- Fungsi Hook untuk Update Status di UI ---
def progress_hook(d):
    if d['status'] == 'downloading':
        try:
            p = d.get('_percent_str', '0%').replace('%','')
            # Simpan status ke session state agar bisa dibaca UI
            st.session_state.log_text = f"⏳ Sedang mendownload: {d.get('filename', 'Unknown')} ({p}%)"
        except:
            pass
    elif d['status'] == 'finished':
        st.session_state.log_text = f"🔨 Sedang mengonversi ke MP3: {d.get('filename', 'Unknown')}"

# --- Tombol Eksekusi ---
if st.button("🚀 Mulai Download", type="primary"):
    if not url_input:
        st.error("Mohon masukkan URL terlebih dahulu!")
    else:
        # Buat folder output
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        status_container = st.status("Memproses...", expanded=True)
        
        if 'log_text' not in st.session_state:
            st.session_state.log_text = "Menghubungkan ke YouTube..."
        
        log_display = status_container.empty()

        # Konfigurasi Dasar yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ignoreerrors': True,
            'quiet': True,
            'no_warnings': True,
        }

        # LOGIKA PERBEDAAN MODE
        if mode == "Satuan (Single Link)":
            # Jika mode satuan: Nama file hanya Judul, dan matikan fitur playlist (biar gak download se-album kalau salah link)
            ydl_opts['outtmpl'] = f'{output_folder}/%(title)s.%(ext)s'
            ydl_opts['noplaylist'] = True 
        else:
            # Jika mode playlist: Nama file ada Nomor Urutnya (1 - Judul)
            ydl_opts['outtmpl'] = f'{output_folder}/%(playlist_index)s - %(title)s.%(ext)s'
            ydl_opts['noplaylist'] = False

        # Tambah Config FFmpeg jika diisi manual
        if ffmpeg_path:
            ydl_opts['ffmpeg_location'] = ffmpeg_path

        # Fungsi Update UI
        def ui_update_hook(d):
            progress_hook(d)
            log_display.markdown(f"**Status:** {st.session_state.log_text}")

        ydl_opts['progress_hooks'] = [ui_update_hook]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url_input])

            status_container.update(label="✅ Selesai!", state="complete", expanded=False)
            st.success(f"Berhasil! Cek folder: **{os.path.abspath(output_folder)}**")

        except Exception as e:
            status_container.update(label="❌ Gagal", state="error")
            st.error(f"Terjadi kesalahan: {e}")
            if "ffmpeg" in str(e).lower():
                st.warning("Tips: Masukkan lokasi folder `bin` FFmpeg di menu Pengaturan Tambahan.")