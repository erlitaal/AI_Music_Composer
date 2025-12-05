import streamlit as st

st.set_page_config(page_title="Tentang Kami", page_icon="👥", layout="wide")

# --- CSS ---
st.markdown("""
<style>
    /* 1. HILANGKAN IKON RANTAI (ANCHOR LINK) DI JUDUL */
    /* Ini menyembunyikan tombol link di samping header */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* 2. HILANGKAN TOMBOL FULLSCREEN DI GAMBAR */
    /* Ini menyembunyikan tombol panah pembesar saat hover gambar */
    [data-testid="StyledFullScreenButton"] {
        display: none !important;
    }
    button[title="View fullscreen"] {
        display: none !important;
    }

    /* 3. EFEK HOVER ZOOM YANG LEBIH MULUS */
    /* Target container gambar agar rapi */
    [data-testid="stImage"] {
        transition: transform 0.3s ease;
        border-radius: 15px;
        overflow: hidden; /* Supaya sudut tetap tumpul saat zoom */
    }
    
    /* Target gambar di dalamnya */
    [data-testid="stImage"] img {
        border-radius: 15px;
        object-fit: cover;
    }

    /* Efek saat mouse diarahkan (Hover) */
    [data-testid="stImage"]:hover {
        transform: scale(1.08); /* Membesar 108% */
        box-shadow: 0 10px 20px rgba(0,0,0,0.15); /* Bayangan timbul */
        z-index: 99;
        cursor: default; /* Kursor panah biasa, bukan tangan klik */
    }
</style>
""", unsafe_allow_html=True)

st.title("👥 Tim Pengembang")
st.markdown("Aplikasi ini dipersembahkan oleh **Kelompok 5** untuk memenuhi Tugas Besar Mata Kuliah **Teori Bahasa Otomata (TBO)**.")
st.write("---")

# FUNGSI UNTUK MEMBUAT KARTU PROFIL
def kartu_anggota(nama, nim, peran, url_foto, quote):
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            # Menampilkan foto (Lingkaran jika memungkinkan di CSS, tapi kotak rapi di sini)
            st.image(url_foto, width=150)
        with col2:
            st.subheader(nama)
            st.caption(f"NIM: {nim}")
            st.markdown(f"**Role:** `{peran}`")
            st.info(f"_{quote}_")

# --- BARIS 1 (Ketua & Wakil) ---
col_a, col_b = st.columns(2)

with col_a:
    # Ganti URL ini dengan nama file lokal nanti (misal: "images/foto_budi.jpg")
    kartu_anggota(
        "Nama", "10101010", "Lead Developer & Logic",
        "https://api.dicebear.com/7.x/avataaars/svg?seed=Felix", # Placeholder Avatar
        "Coding is poetry, music is math."
    )

with col_b:
    kartu_anggota(
        "Nama Anggota 2", "12121212", "Backend & Audio Engineer",
        "https://api.dicebear.com/7.x/avataaars/svg?seed=Aneka",
        "Mengubah angka menjadi nada."
    )

st.write("---")

# --- BARIS 2 (Anggota Lain) ---
c1, c2, c3 = st.columns(3)

with c1:
    kartu_anggota(
        "Nama Anggota 3", "12121212", "Frontend & UI/UX",
        "https://api.dicebear.com/7.x/avataaars/svg?seed=Bob",
        "Mengubah angka menjadi nada."
    )

with c2:
    kartu_anggota(
        "Nama Anggota 4", "12121212", "Data Analyst & QA",
        "https://api.dicebear.com/7.x/avataaars/svg?seed=Data",
        "Mengubah angka menjadi nada."
    )

with c3:
    kartu_anggota(
        "Nama Anggota 5", "12121212", "Report & Documentation",
        "https://api.dicebear.com/7.x/avataaars/svg?seed=Jack",
        "Mengubah angka menjadi nada."
    )

st.write("---")
st.markdown("### 🛠️ Tech Stack yang Digunakan")
st.markdown("""
* 🐍 **Python 3.10** (Bahasa Pemrograman Utama)
* 🌊 **Streamlit** (Framework Web App)
* 🎹 **MidiUtil** (Generasi File MIDI)
* 🔊 **Scipy & NumPy** (Pemrosesan Sinyal Audio Digital)

""")

