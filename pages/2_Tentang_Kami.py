import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Tentang Kami", 
    page_icon="👥", 
    layout="wide"
)

# --- CSS CUSTOM (SAMA DENGAN HOME AGAR KONSISTEN) ---
st.markdown("""
<style>
    /* 1. IMPORT FONT */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400&display=swap');

    /* 1. SEMBUNYIKAN UI BAWAAN (SIDEBAR & HEADER) */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stHeader"] { background-color: transparent; }
    [data-testid="stToolbar"] { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }
    [data-testid="stHeaderActionElements"] { display: none !important; }
    
    /* 2. BACKGROUND */
    .stApp {
        background-color: #E8E8E5;
    }

    /* 3. TYPOGRAPHY */
    h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #000; }
    p, span, div { font-family: 'Lato', sans-serif; color: #333; }

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
    
    /* 5. CARD PROFIL (GAYA ALBUM/POSTER) */
    .profile-card {
        background-color: #fff;
        border: 1px solid #000;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 10px 10px 0px rgba(0,0,0,0.8); /* Efek bayangan kasar/retro */
    }

    /* Gambar di dalam card */
    .card-img {
        width: 150px;
        aspect-ratio: 1 / 1; /* Kotak Sempurna */
        object-fit: cover;
        border-bottom: 2px solid #000;
        margin: 0 auto 15px auto;
        filter: grayscale(100%);
        transition: filter 0.3s ease;
        display: block;
    }
    
    .profile-card:hover .card-img {
        filter: grayscale(0%);
    }

    /* Teks dalam card */
    .card-role {
        font-family: 'Lato', sans-serif;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        background-color: #000;
        color: #fff !important;
        display: inline-block;
        padding: 2px 8px;
        margin-bottom: 10px;
    }
    
    .card-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.1;
    }
    
    .card-nim {
        font-size: 0.8rem;
        color: #666;
        margin-bottom: 10px;
    }

    .card-quote {
        font-style: italic;
        font-size: 0.85rem;
        border-top: 1px dashed #ccc;
        padding-top: 10px;
        margin-top: 10px;
    }

    /* Sticker Hiasan */
    .sticker {
        font-size: 1.5rem;
        position: absolute;
        opacity: 0.2;
        z-index: 0;
    }
    
    /* --- MOBILE RESPONSIVE --- */
    @media only screen and (max-width: 768px) {
        /* Judul Besar */
        div[class*="stMarkdown"] h1 { font-size: 2.5rem !important; text-align: center; }
        
        /* Navbar Rata Tengah */
        div[data-testid="column"] { text-align: center !important; margin-bottom: 5px; }
        
        /* Card ada jarak bawahnya saat ditumpuk */
        .profile-card { margin-bottom: 30px; }
        
        /* Code text rata tengah */
        div[style*="font-family: 'Courier New'"] { text-align: center !important; margin-top: 20px; }
    }
    
    /* HILANGKAN PADDING ATAS AGAR NAVBAR NAIK */
    .block-container { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

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

# =========================================
# INTRO MISSION
# =========================================
c_intro1, c_intro2 = st.columns([1.5, 1])

with c_intro1:
    st.markdown('<div style="font-size: 4rem; font-family: Playfair Display; font-weight: 900; line-height: 1;">THE<br>CREATORS</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    **Misi Kami:** Mencari 19 juta lapangan pekerjaan.
    """)

with c_intro2:
    # Dekorasi elemen musik/IT
    st.markdown("""
    <div style="text-align: right; opacity: 0.6; font-family: 'Courier New'; font-size: 0.9rem;">
        import creativity<br>
        import logic<br>
        <br>
        def create_harmony():<br>
        &nbsp;&nbsp;return "Beautiful"<br>
        <br>
        // Status: Ready<br>
        // System: Online
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================
# TEAM GRID (LAYOUT KARTU)
# =========================================

def team_card(nama, nim, role, img_url, quote, link):
    # Menggunakan HTML Card Custom agar desainnya kotak & punya border hitam
    st.markdown(f"""
    <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">
        <div class="profile-card">
            <div class="card-role">{role}</div>
            <img src="{img_url}" class="card-img">
            <div class="card-name">{nama}</div>
            <div class="card-nim">{nim}</div>
            <div class="card-quote">"{quote}"</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# --- BARIS 1: LEADERS (2 Orang) ---
# Menggunakan columns memastikan responsif di HP (Stacking)
l1, l2 = st.columns(2)

with l1:
    team_card(
        "Fahri Khairun A.", "1247050084", "PROJECT LEAD",
        "https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/fahrii.png",
        "People can only save themselves. One person saving another is impossible.",
        "https://instagram.com/p_ftttt"
    )

with l2:
    team_card(
        "Erlita Amelia", "1247050088", "DATA EXPERT",
        "https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto erlita2.jpg", # Ganti foto nanti
        "Fear kills more dreams than failure ever will.",
        "https://instagram.com/erlitaall"
    )

st.write("") # Spacer

# --- BARIS 2: SPECIALISTS (3 Orang) ---
m1, m2, m3 = st.columns(3)

with m1:
    team_card(
        "Azmi Putri K.", "1247050126", "BACKEND DEV",
        "https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto azmi.jpg", # Ganti foto nanti
        "Good things take time.",
        "https://instagram.com/azmiptr_"
    )

with m2:
    team_card(
        "Alden Shalih F.", "1247050050", "FRONTEND DEV",
        "https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto alden.jpg", # Ganti foto nanti
        "The moment you drop ‘if’ is the moment your life starts moving forward.",
        "https://instagram.com/dennn.26sf"
    )

with m3:
    team_card(
        "Ahmad Maftuh R.", "1247050100", "FRONTEND DEV",
        "https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto maftuh.jpg", # Ganti foto nanti
        "Bertumbuh bebas.",
        "https://instagram.com/stagarling"
    )

# Footer
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem; margin-top: 50px; border-top: 1px solid #ccc; padding-top: 20px;">
    © 2025 Kelompok 5 • Informatics Engineering
</div>
""", unsafe_allow_html=True)
