import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS CUSTOM ---
st.markdown("""
<style>
    /* 1. IMPORT FONT (Playfair Display & Lato) */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400&display=swap');

    /* 1. SEMBUNYIKAN UI BAWAAN (SIDEBAR & HEADER) */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stHeader"] { background-color: transparent; }
    [data-testid="stToolbar"] { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }
    [data-testid="stHeaderActionElements"] { display: none !important; }
    
    /* 2. BACKGROUND */
    .stApp { background-color: #E8E8E5; }

    /* 3. TYPOGRAPHY UMUM */
    h1, h2, h3, .big-font {
        font-family: 'Playfair Display', serif !important;
        color: #000000;
    }
    
    p, .stMarkdown, div, span {
        font-family: 'Lato', sans-serif;
        color: #333333;
    }

    /* 4. HERO SECTION STYLE */
    /* Container Kanan (Flexbox) */
    .hero-right {
        display: flex;
        justify-content: flex-end; /* KUNCI: MENTOK KANAN */
        align-items: center;
        height: 100%;
        width: 100%;
    }

    /* Judul Besar 160px */
    .hero-title-text {
        font-family: 'Playfair Display', serif; 
        font-size: 160px; 
        font-weight: 700; 
        line-height: 0.8; 
        color: black; 
        margin: 0;
        letter-spacing: -5px;
    }

    .price-tag {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        margin-bottom: 0;
    }

    /* 5. PRESET CARD STYLE (TYPOGRAPHY RAPI) */
    .preset-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 5px;
        color: #000;
    }
    
    .preset-meta {
        font-family: 'Lato', sans-serif;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #666; 
        margin-bottom: 12px;
        font-weight: 700;
    }

    .preset-desc {
        font-family: 'Lato', sans-serif;
        font-size: 0.9rem;      
        font-weight: 300;       
        line-height: 1.6;       
        color: #444;            
        margin-bottom: 20px;
    }

    /* 6. TOMBOL KOTAK */
    .stButton > button {
        background-color: transparent;
        border: 1px solid #000000;
        color: #000000;
        border-radius: 0px; 
        padding: 10px 20px;
        font-family: 'Lato', sans-serif; 
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #000000 !important;
        color: #f6eee5 !important; 
        border-color: #000000 !important;
    }
    
    .stButton > button:hover p {
        color: #f6eee5 !important;
    }

    /* 7. DIVIDER */
    .custom-divider {
        border-top: 1px solid #000;
        margin-top: 20px;
        margin-bottom: 40px;
        display: flex;
        align-items: center;
    }
    .section-letter {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: bold;
        margin-right: 20px;
        border-bottom: 3px solid black;
    }
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin-left: auto;
    }
    
    /* Class untuk Gambar: Grayscale + Rounded */
    .img-hover-effect {
        filter: grayscale(100%);       /* Hitam putih awal */
        transition: all 0.5s ease;     /* Animasi halus */
        cursor: pointer;               /* Kursor jari */
        border-radius: 20px;           /* <--- INI PEMBUAT SUDUT TUMPUL */
        object-fit: cover;             /* Biar gambar gak penyok */
    }
    
    /* Saat Hover: Jadi Berwarna */
    .img-hover-effect:hover {
        filter: grayscale(0%) !important; /* !important MEMAKSA biar jalan */
    }
    
    /* 4. NAVBAR STYLE (SAMA PERSIS DENGAN GENERATOR) */
    div[data-testid="stPageLink-NavLink"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    div[data-testid="stPageLink-NavLink"] p {
        font-family: 'Lato', sans-serif;
        font-size: 1rem;
        font-weight: 700;
        color: #666 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div[data-testid="stPageLink-NavLink"]:hover p {
        color: #000 !important;
        text-decoration: underline;
    }
    div[data-testid="stPageLink-NavLink"] svg { display: none; }

    /* --- MOBILE RESPONSIVE (LAYAR KECIL) --- */
    @media only screen and (max-width: 768px) {
        /* 1. Judul Mengecil Drastis biar muat */
        .hero-title {
            font-size: 4rem !important; /* Dari 10rem jadi 4rem */
            margin-top: 0px !important;
            letter-spacing: -2px !important;
            text-align: center;
        }
        
        /* 2. Navbar jadi rata tengah saat ditumpuk */
        div[data-testid="column"] {
            text-align: center !important;
            margin-bottom: 10px;
        }
        
        /* 4. Harga & Deskripsi turun ke bawah */
        .price-tag { text-align: center; margin-top: 20px; }
        
        /* 5. Gambar Full Width */
        img { width: 100% !important; margin-top: 20px;}
    }
    
    /* HILANGKAN PADDING ATAS AGAR NAVBAR NAIK */
    .block-container { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# =========================================
# SECTION 1: HERO
# =========================================
# --- NAVBAR ---
c_nav1, c_nav2, c_nav3, c_nav4 = st.columns([3, 1, 1, 1])
with c_nav1:
    st.markdown("<h3 style='margin:0; font-family: Playfair Display; color:black;'>KELOMPOK 5</h3>", unsafe_allow_html=True)
with c_nav2:
    st.page_link("Home.py", label="HOME", use_container_width=True)
with c_nav3:
    st.page_link("pages/1_Generator.py", label="GENERATOR", use_container_width=True)
with c_nav4:
    st.page_link("pages/2_Tentang_Kami.py", label="ABOUT", use_container_width=True)

st.write("---")

col1, col2 = st.columns([1.3, 1]) 

with col1:
    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
    
    # JUDUL BESAR 160px
    st.markdown("""
    <p style="
        font-family: 'Playfair Display', serif; 
        font-size: 160px; 
        font-weight: 700; 
        line-height: 0.8; 
        color: black; 
        margin: 0;
        letter-spacing: -5px;">
        AI<br>MUSIC
    </p>
    """, unsafe_allow_html=True)
    
    c_price, c_desc = st.columns([1, 2])
    with c_price:
        st.markdown('<p class="price-tag">Kelompok 5</p>', unsafe_allow_html=True)
        st.caption("Version 1.0")
    with c_desc:
        st.markdown("### Royalty Free")
        st.write("Miliki hak cipta sepenuhnya atas musik yang Anda buat. Cocok untuk kreator konten, developer game, dan pemimpi.")
        
        st.markdown("""
        <div style="margin-top: -15px; font-weight: 700; color: #000;">
            Tanpa Lisensi. Tanpa Batas.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("Mulai Sekarang ->", key="btn_hero"):
            st.switch_page("pages/1_Generator.py")

with col2:
    st.markdown("""
        <div class="hero-right">
            <img src="https://images.unsplash.com/photo-1550291652-6ea9114a47b1?q=80&w=1000&auto=format&fit=crop" 
                 class="img-hover-effect"
                 style="width: 550px; max-width: 100%; height: 700px; object-fit: cover;">
        </div>
    """, unsafe_allow_html=True)
    
st.write("")
st.write("")

# =========================================
# SECTION 2: CATALOG (4 PRESETS)
# =========================================
st.markdown("""
<div class="custom-divider">
    <span class="section-letter">M</span>
    <span style="flex-grow: 1; height: 1px; background-color: black;"></span>
    <span class="section-title">Mood Collection</span>
</div>
""", unsafe_allow_html=True)

# Layout 4 Kolom
p1, p2, p3, p4 = st.columns(4)

# --- PRESET 1: HAPPY ---
with p1:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1619983081563-430f63602796?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bXVzaWN8ZW58MHx8MHx8fDA%3D" 
             class="img-hover-effect" 
             style="width: 100%; height: 200px; object-fit: cover;">
    """, unsafe_allow_html=True)
    st.markdown('<div class="preset-title">Morning Pop</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-meta">120 BPM • MAJOR SCALE</div>', unsafe_allow_html=True)
    # Typography Deskripsi yang sudah diperbaiki (font agak tipis, spasi lega)
    st.markdown('<div class="preset-desc">Energi positif dengan ritme yang memikat. Cocok untuk vlog travel atau pembukaan yang ceria.</div>', unsafe_allow_html=True)
    if st.button("PILIH POP", key="btn_happy"):
        st.switch_page("pages/1_Generator.py")

# --- PRESET 2: SAD ---
with p2:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?q=80&w=600&auto=format&fit=crop" 
             class="img-hover-effect" 
             style="width: 100%; height: 350px; object-fit: cover;">
    """, unsafe_allow_html=True)
    st.markdown('<div class="preset-title">Melancholy</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-meta">65 BPM • BALLAD</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-desc">Sentuhan piano lembut yang menyentuh hati. Sempurna untuk adegan emosional yang mendalam.</div>', unsafe_allow_html=True)
    if st.button("PILIH BALLAD", key="btn_sad"):
        st.switch_page("pages/1_Generator.py")

# --- PRESET 3: JAZZ ---
with p3:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1629907451365-6731862a0d32?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDN8fGphenp8ZW58MHx8MHx8fDA%3D" 
             class="img-hover-effect" 
             style="width: 100%; height: 350px; object-fit: cover;">
    """, unsafe_allow_html=True)
    st.markdown('<div class="preset-title">Midnight Jazz</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-meta">90 BPM • SWING</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-desc">Suasana lounge santai dengan harmoni chord 7th yang kompleks dan elegan.</div>', unsafe_allow_html=True)
    if st.button("PILIH JAZZ", key="btn_jazz"):
        st.switch_page("pages/1_Generator.py")

# --- PRESET 4: CINEMATIC ---
with p4:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1708164333066-dabc2dac17d2?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" 
             class="img-hover-effect" 
             style="width: 100%; height: 200px; object-fit: cover;">
    """, unsafe_allow_html=True)
    st.markdown('<div class="preset-title">The Epic Saga</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-meta">135 BPM • HARMONIC MINOR</div>', unsafe_allow_html=True)
    st.markdown('<div class="preset-desc">Ketegangan orkestra dan violin yang intens. Dirancang untuk momen klimaks dramatis.</div>', unsafe_allow_html=True)
    if st.button("PILIH CINE", key="btn_cine"):
        st.switch_page("pages/1_Generator.py")

st.write("")
st.write("")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem; margin-top: 50px; border-top: 1px solid #ccc; padding-top: 20px;">
    © 2025 Kelompok 5 • Engineering Art
</div>
""", unsafe_allow_html=True)