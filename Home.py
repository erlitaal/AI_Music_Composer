import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Melody AI Studio",
    page_icon="🎹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (AGAR TAMPILAN LEBIH MODERN) ---
st.markdown("""
<style>
    /* HILANGKAN IKON RANTAI DI HEADER */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    /* Import Font Keren (Google Fonts) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');
    
    /* Terapkan Font ke seluruh aplikasi */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Style Judul Utama */
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #4B4B4B; /* Abu Gelap */
        text-align: center;
        margin-bottom: 0;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Style Kotak Fitur */
    .feature-box {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    .feature-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    /* Hilangkan dekorasi link default */
    a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col_spacer1, col_hero, col_spacer2 = st.columns([1, 3, 1])

with col_hero:
    st.markdown('<p class="main-header">🎹 Melody AI Studio</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Bangun komposisi musik tanpa batas dengan kekuatan <b>Artificial Intelligence</b> dan <b>Teori Otomata</b>.</p>', unsafe_allow_html=True)
    st.write("---")

# --- FITUR UNGGULAN (3 KOLOM) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h1>🎭</h1>
        <h3>Mood-Based</h3>
        <p>Pilih suasana hati—Ceria, Sedih, atau Tegang. AI akan menyesuaikan tangga nada dan tempo secara otomatis.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h1>🧠</h1>
        <h3>Smart Logic</h3>
        <p>Menggunakan <b>Finite State Automata</b> untuk harmoni dan <b>Markov Chain</b> untuk variasi melodi yang natural.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h1>🎛️</h1>
        <h3>Multi-Track</h3>
        <p>Hasil output lengkap dengan <b>Drum, Bass, Chord, & Melodi</b>. Siap download dalam format WAV & MIDI.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Spasi kosong
st.write("")

# --- SECTION CALL TO ACTION ---
col_cta_left, col_cta_right = st.columns([2, 1])

with col_cta_left:
    st.subheader("🚀 Siap membuat lagu pertamamu?")
    st.write("""
    Tidak perlu keahlian musik. Cukup tentukan parameter, dan biarkan AI bekerja.
    1.  Buka menu **🎵 Generator** di sebelah kiri.
    2.  Pilih **Simple Mode** untuk hasil instan.
    3.  Atau **Advanced Mode** untuk kustomisasi penuh.
    """)
    
with col_cta_right:
    # Gambar ilustrasi (Ganti link jika mau)
    st.image("https://images.unsplash.com/photo-1514320291940-7c5846613c77?q=80&w=1000&auto=format&fit=crop", caption="AI Music Generation", use_container_width=True)

st.write("---")
st.markdown("<div style='text-align: center; color: grey;'>© 2025 Kelompok 5 - Tugas Besar TBO</div>", unsafe_allow_html=True)