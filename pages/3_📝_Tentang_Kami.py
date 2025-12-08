import streamlit as st

# =================================================================
# KOMPONEN STYLING GLOBAL & TEMA
# Memisahkan CSS kustom ke dalam fungsi yang berfungsi sebagai komponen.
# =================================================================
def styling_global_component(background_color="#e8e9e4", accent_color="#5a6a62"):
    """
    Fungsi untuk mendefinisikan semua CSS kustom, termasuk warna tema.
    """
    st.markdown(f"""
    <style>
        /* 1. WARNA GLOBAL / BACKGROUND APLIKASI */
        .stApp {{
            background-color: {background_color}; /* Warna background baru Anda */
            color: #333333; /* Warna Teks Utama */
        }}

        /* HILANGKAN IKON RANTAI DI HEADER */
        [data-testid="stHeaderActionElements"] {{
            display: none !important;
        }}

        /* GAYA FOTO PROFIL */
        .profile-img {{
            width: 100%;             
            max-width: 120px;        
            height: auto;
            border-radius: 15px;     
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: block;
            margin: 0 auto 10px auto; 
            cursor: pointer;
            object-fit: cover; 
            border: 3px solid {accent_color}; /* Border foto menggunakan warna aksen */
        }}

        /* EFEK HOVER PADA FOTO */
        .profile-img:hover {{
            transform: scale(1.08);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            filter: brightness(1.1);
        }}
        
        /* GAYA LINK IG */
        a.profile-link {{
            text-decoration: none;
        }}

        /* GAYA KARTU ANGGOTA KESELURUHAN */
        .profile-card {{
            text-align: center; 
            padding: 10px; 
            background-color: #ffffff; /* Background Kartu tetap Putih agar menonjol */
            border: 1px solid #d0d2cc; /* Border disesuaikan agar cocok dengan background */
            border-radius: 10px; 
            height: 100%;
            transition: box-shadow 0.3s ease, transform 0.3s ease;
        }}

        /* EFEK HOVER PADA KARTU ANGGOTA */
        .profile-card:hover {{
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            transform: translateY(-3px);
        }}

        /* 2. WARNA GARIS PEMISAH (DIVIDER) */
        hr {{
            border-top: 1px solid {accent_color}; 
            opacity: 0.5;
        }}

        /* GAYA TEKS PERAN (Warna Aksen) */
        .profile-card p.role {{
            font-size: 0.9rem; 
            font-weight: bold; 
            margin: 5px 0 5px 0; 
            color: {accent_color}; /* Menggunakan warna aksen baru */
        }}
        
        /* GAYA QUOTE */
        .profile-card > div:last-child {{
            color: #6a6a6a !important; 
        }}
        
    </style>
    """, unsafe_allow_html=True)


# =================================================================
# FUNGSI KOMPONEN KARTU ANGGOTA (TETAP SAMA)
# =================================================================
def kartu_anggota(nama, nim, peran, url_foto, quote, link_ig):
    html_code = f"""
    <div class="profile-card">
        <a href="{link_ig}" target="_blank" class="profile-link" title="Klik untuk ke Instagram">
            <img src="{url_foto}" class="profile-img">
        </a>
        <h4 style="margin: 5px 0 0px 0;">{nama}</h4>
        <p class="nim">NIM: {nim}</p>
        <p class="role">{peran}</p>
        <div style="font-style: italic; font-size: 0.75rem; color: #666; margin-top: 5px;">"{quote}"</div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


# =================================================================
# STRUKTUR UTAMA APLIKASI (MAIN APP LOGIC)
# =================================================================

st.set_page_config(page_title="Tentang Kami", page_icon="👥", layout="wide")

# PANGGIL KOMPONEN STYLING DI AWAL
styling_global_component(
    background_color="#e8e9e4", 
    # Saya pilih warna aksen dark-green/gray agar cocok dengan background baru
    accent_color="#5a6a62" 
) 

st.title("👥 Tim Pengembang")
st.markdown("Aplikasi ini dipersembahkan oleh **Kelompok 5** untuk memenuhi Tugas Besar Mata Kuliah **Teori Bahasa Otomata (TBO)**.")
st.write("---")

# --- BARIS SEMUA ANGGOTA (Menggunakan 5 Kolom) ---
col_fahri, col_erlita, col_azmi, col_alden, col_ahmad = st.columns(5)

# (Anda bisa melanjutkan detail anggota seperti kode sebelumnya)
with col_fahri:
    kartu_anggota(
        nama="Fahri Khairun Ariansyah", 
        nim="1247050084", 
        peran="Lead Developer & Backend",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/fahrii.png", 
        quote="People can only save themselves.",
        link_ig="https://www.instagram.com/p_ftttt"
    )
# ... dan seterusnya untuk anggota lain ...

# (Saya hanya menampilkan 1 anggota sebagai contoh, tapi Anda masukkan 5 anggota di sini)

with col_erlita:
    kartu_anggota(
        nama="Erlita Amelia", 
        nim="1247050088", 
        peran="Data search & QA",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Aneka",
        quote="Mengubah angka menjadi nada.",
        link_ig="https://www.instagram.com/erlitaall"
    )
    
with col_azmi:
    kartu_anggota(
        nama="Azmi", 
        nim="1247050126", 
        peran="Backend & Audio Engineer",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Bob",
        quote="Good things take time.",
        link_ig="https://www.instagram.com/azmiptr_"
    )

with col_alden:
    kartu_anggota(
        nama="Alden Shalih Falah", 
        nim="1247050050", 
        peran="Frontend & UI/UX",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Data",
        quote="The moment you drop 'if' is the moment your life starts moving forward.",
        link_ig="https://www.instagram.com/dennn.26sf"
    )

with col_ahmad:
    kartu_anggota(
        nama="Ahmad Maftuh Rojak", 
        nim="12121212", 
        peran="Frontend & UI/UX",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Jack",
        quote="growing freely.",
        link_ig="https://www.instagram.com/stagarling"
    )

st.write("---")

# Bagian Tech Stack
st.markdown("### 🛠️ Tech Stack yang Digunakan")
st.markdown("""
* 🐍 **Python 3.10** (Bahasa Pemrograman Utama)
* 🌊 **Streamlit** (Framework Web App)
* 🎹 **MidiUtil** (Generasi File MIDI)
* 🔊 **Scipy & NumPy** (Pemrosesan Sinyal Audio Digital)
""")

st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 50px;">
    © 2025 Kelompok 5 - Teknik Informatika. Dibuat dengan Python & Streamlit.
</div>
""", unsafe_allow_html=True)
