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
        nama="Nama Anggota", 
        nim="10101010", 
        peran="Lead Developer & Logic",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix", 
        quote="Coding is poetry, music is math.",
        link_ig="https://www.instagram.com/instagram"
    )

with col_b:
    kartu_anggota(
        nama="Nama Anggota 2", 
        nim="12121212", 
        peran="Backend & Audio Engineer",
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Aneka",
        quote="Mengubah angka menjadi nada.",
        link_ig="https://www.instagram.com/"
    )

st.write("---")

# --- BARIS 2 (Anggota Lain) ---
c1, c2, c3 = st.columns(3)

def kartu_kecil(col, nama, role, img, ig):
    with col:
        html_code = f"""
        <div style="text-align: center;">
            <a href="{ig}" target="_blank">
                <img src="{img}" class="profile-img" style="margin: 0 auto;">
            </a>
            <p style="margin-top: 10px;"><b>{nama}</b><br>
            <span style="font-size: 0.8em; color: gray;">{role}</span></p>
        </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)

kartu_kecil(c1, "Nama Anggota 3", "Frontend & UI/UX", "https://api.dicebear.com/7.x/avataaars/svg?seed=Bob", "https://instagram.com")
kartu_kecil(c2, "Nama Anggota 4", "Data Analyst & QA", "https://api.dicebear.com/7.x/avataaars/svg?seed=Data", "https://instagram.com")
kartu_kecil(c3, "Nama Anggota 5", "Report & Doc", "https://api.dicebear.com/7.x/avataaars/svg?seed=Jack", "https://instagram.com")

st.write("---")
st.markdown("### 🛠️ Tech Stack yang Digunakan")
st.markdown("""
* 🐍 **Python 3.10** (Bahasa Pemrograman Utama)
* 🌊 **Streamlit** (Framework Web App)
* 🎹 **MidiUtil** (Generasi File MIDI)
* 🔊 **Scipy & NumPy** (Pemrosesan Sinyal Audio Digital)

""")


