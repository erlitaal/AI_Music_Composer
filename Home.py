import streamlit as st

# Konfigurasi Halaman (Wajib di baris pertama)
st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS CUSTOM UNTUK TAMPILAN LEBIH CANTIK ---
st.markdown("""
<style>
    /* HILANGKAN IKON RANTAI DI HEADER */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* Mengubah warna background header */
    .stAppHeader {
        background-color: transparent;
    }
    
    /* Style untuk Judul Utama */
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #1E1E1E; /* Warna Judul Utama */
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.5rem;
        font-weight: 400;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Style untuk Kartu Fitur */
    .feature-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin-bottom: 10px;
        transition: transform 0.3s;
        border: 1px solid #ddd; /* Tambah garis pinggir biar jelas */
    }
    .feature-card:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* --- PERBAIKAN WARNA TEKS --- */
    .feature-card h3 {
        color: #000000 !important; /* Judul di dalam kotak WAJIB Hitam */
        font-weight: 600;
    }
    .feature-card p {
        color: #333333 !important; /* Tulisan deskripsi WAJIB Abu Gelap */
        font-size: 1rem;
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION (JUDUL BESAR) ---
st.markdown('<p class="main-title">🎹 AI Music Composer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Tugas Besar Teori Bahasa Otomata (TBO) - Kelompok 5</p>', unsafe_allow_html=True)

st.divider()

# --- INTRO & GAMBAR ---
col_intro, col_img = st.columns([1.5, 1], gap="large")

with col_intro:
    st.write("### 🚀 Selamat Datang di Masa Depan Musik!")
    st.markdown("""
    Aplikasi ini mendemonstrasikan bagaimana **Ilmu Komputer** dapat berkolaborasi dengan **Seni Musik**. 
    Kami tidak menggunakan file audio rekaman, melainkan algoritma cerdas yang "mengarang" lagu secara *real-time* detik demi detik.
    
    **Teknologi di balik layar:**
    * **Finite State Automata (FSA):** Menjaga agar nada tetap harmonis dan tidak fals (sebagai "Polisi Nada").
    * **Markov Chain:** Memberikan variasi ritme dan melodi agar terdengar manusiawi (sebagai "Jiwa Kreatif").
    * **Pattern Recognition:** Mengatur drum dan bass agar sesuai genre (Pop/Jazz/Ballad).
    """)
    
    st.info("💡 **Tips:** Buka menu di sebelah kiri (Sidebar) untuk mulai menggunakan aplikasi.")

with col_img:
    # PERBAIKAN DI SINI: Mengganti 'use_column_width' menjadi 'use_container_width'
    st.image("https://images.unsplash.com/photo-1511379938547-c1f69419868d?q=80&w=1000&auto=format&fit=crop", 
             caption="Harmony of Code & Sound", use_container_width=True)

st.write("---")

# --- FITUR HIGHLIGHTS (3 KOLOM) ---
st.subheader("🌟 Fitur Unggulan")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎭</div>
        <h3>Mood Detection</h3>
        <p>Pilih suasana hati (Senang, Sedih, Tegang), dan AI akan meracik tangga nada yang sesuai secara otomatis.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎷</div>
        <h3>Genre Adaptive</h3>
        <p>Sistem pengiring cerdas yang bisa berubah gaya main (Drum & Bass) dari Pop, Ballad, hingga Jazz Swing.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎼</div>
        <h3>MIDI Export</h3>
        <p>Hasil karya AI bisa didownload dalam format MIDI Profesional untuk diedit di FL Studio atau GarageBand.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 50px;">
    © 2025 Kelompok 5 - Teknik Informatika. Dibuat dengan Python & Streamlit.
</div>
""", unsafe_allow_html=True)