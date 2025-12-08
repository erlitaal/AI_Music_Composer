import streamlit as st

st.set_page_config(page_title="Tentang Kami", page_icon="👥", layout="wide")

# ==========================================
# CSS CUSTOM (GAYA TAMPILAN)
# ==========================================
st.markdown("""
<style>
    /* HILANGKAN IKON RANTAI DI HEADER */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* GAYA FOTO PROFIL */
    .profile-img {
        width: 100%;             /* Lebar mengikuti kolom */
        max-width: 150px;        /* Maksimal 150px biar gak kegedean */
        border-radius: 15px;     /* Sudut tumpul */
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: block;
        margin-bottom: 10px;
        cursor: pointer;         /* Ubah kursor jadi tangan */
    }

    /* EFEK SAAT MOUSE DIARAHKAN (HOVER) */
    .profile-img:hover {
        transform: scale(1.08);  /* Membesar */
        box-shadow: 0 10px 20px rgba(0,0,0,0.2); /* Bayangan timbul */
        filter: brightness(1.1); /* Sedikit lebih terang */
    }
    
    /* GAYA LINK IG (BIAR GAK ADA GARIS BAWAH JELEK) */
    a.profile-link {
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

st.title("👥 Tim Pengembang")
st.markdown("Aplikasi ini dipersembahkan oleh **Kelompok 5** untuk memenuhi Tugas Besar Mata Kuliah **Teori Bahasa Otomata (TBO)**.")
st.write("---")

# FUNGSI UNTUK MEMBUAT KARTU PROFIL
def kartu_anggota(nama, nim, peran, url_foto, quote, link_ig):
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            html_code = f"""
            <a href="{link_ig}" target="_blank" class="profile-link" title="Klik untuk ke Instagram">
                <img src="{url_foto}" class="profile-img">
            </a>
            """
            st.markdown(html_code, unsafe_allow_html=True)
            
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
        nama="Fahri Khairun Ariansyah", 
        nim="1247050084", 
        peran="Lead Developer & Backend",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/fahrii.png", 
        quote="\"People can only save themselves. One person saving another is impossible.\"",
        link_ig="https://www.instagram.com/p_ftttt"
    )

with col_b:
    kartu_anggota(
        nama="Erlita Amelia", 
        nim="1247050088", 
        peran="Data search & QA",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto erlita.jpg",
        quote="\"Mengubah angka menjadi nada.\"",
        link_ig="https://www.instagram.com/erlitaall"
    )

st.write("---")

# --- BARIS 2 (Anggota Lain) ---
c1, c2, c3 = st.columns(3)

with c1:
    kartu_anggota(
        nama="Azmi Putri Kuswandi", 
        nim="1247050126", 
        peran="Backend & Audio Engineer",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto azmi.jpg",
        quote="\"Good things take time.\"",
        link_ig="https://www.instagram.com/azmiptr_"
    )

with c2:
    kartu_anggota(
        nama="Alden Shalih Falah", 
        nim="1247050050", 
        peran="Frontend & UI/UX",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto alden.jpg",
        quote="\"The moment you drop 'if' is the moment your life starts moving forward.\"",
        link_ig="https://www.instagram.com/dennn.26sf"
    )

with c3:
    kartu_anggota(
        nama="Ahmad Maftuh Rojak", 
        nim="12121212", 
        peran="Frontend & UI/UX",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Jack",
        quote="\"growing freely.\"",
        link_ig="https://www.instagram.com/stagarling"
    )

st.write("---")
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
