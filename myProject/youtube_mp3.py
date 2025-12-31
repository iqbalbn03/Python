import yt_dlp
import os

def download_playlist_mp3(url, output_folder="Downloads"):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Konfigurasi yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Ambil sumber audio terbaik
        'outtmpl': f'{output_folder}/%(playlist_index)s - %(title)s.%(ext)s', # Format nama file: "1 - Judul Lagu.mp3"
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True, # Lanjut ke video berikutnya jika ada 1 video error (misal: private video)
        'quiet': False,
        'no_warnings': True,
    }

    print(f"Mulai mendownload dari: {url}")
    print("Proses ini mungkin memakan waktu tergantung jumlah video dan koneksi internet...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ Selesai! File tersimpan di folder '{output_folder}'")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Masukkan URL Playlist di sini
    playlist_url = input("Masukkan URL Playlist YouTube: ")
    
    download_playlist_mp3(playlist_url)