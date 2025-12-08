import streamlit as st

st.set_page_config(page_title="Tentang Kami", page_icon="👥", layout="wide")

# =================================================================
# KOMPONEN 1: STYLING GLOBAL & TEMA
# =================================================================
def styling_global_component(background_color="#e8e9e4", accent_color="#5a6a62"):
    st.markdown(f"""
    <style>
        /* 1. WARNA GLOBAL / BACKGROUND APLIKASI */
        .stApp {{
            background-color: {background_color};
            color: #333333;
        }}

        /* --- PENINGKATAN POIN 1 (HIRARKI VISUAL: Judul & Sub-judul) --- */
        h1 {{
            margin-bottom: 25px !important; 
        }}
        h3 {{
            color: #333333;
            border-bottom: 2px solid {accent_color}; 
            padding-bottom: 5px;
        }}
        /* ------------------------------------------- */

        /* HILANGKAN IKON RANTAI DI HEADER */
        [data-testid="stHeaderActionElements"] {{
            display: none !important;
        }}

        /* GAYA FOTO PROFIL */
        .profile-img {{
            width: 100%;             
            max-width: 120px;     
            height: 120px; 
            border-radius: 15px;     
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: block;
            margin: 0 auto 10px auto; 
            cursor: pointer;
            object-fit: cover; 
            border: 3px solid {accent_color}; 
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
            padding: 15px; /* Sedikit lebih besar */
            background-color: #ffffff; 
            border: 1px solid #d0d2cc; 
            border-radius: 10px; 
            height: 100%;
            transition: box-shadow 0.3s ease, transform 0.3s ease;
        }}

        /* EFEK HOVER PADA KARTU ANGGOTA */
        .profile-card:hover {{
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            transform: translateY(-3px);
        }}

        /* --- PENINGKATAN POIN 2 (ROLE BADGE) --- */
        .role-badge {{
            display: inline-block;
            padding: 4px 10px;
            margin: 5px 0;
            border-radius: 20px;
            background-color: {accent_color};
            color: white;
            font-size: 0.8rem;
            font-weight: bold;
            letter-spacing: 0.5px;
        }}
        /* ------------------------------------------- */


        /* 2. WARNA GARIS PEMISAH (DIVIDER) */
        hr {{
            border-top: 1px solid {accent_color}; 
            opacity: 0.5;
        }}
        
        /* GAYA TEKS NIM */
        .profile-card p.nim {{
            font-size: 0.8rem; 
            color: #888; 
            margin: 0;
        }}
        
        /* GAYA QUOTE */
        .profile-card .quote-text {{
            font-style: italic; 
            font-size: 0.75rem; 
            color: #6a6a6a !important; 
            margin-top: 10px;
        }}

        /* --- PENINGKATAN POIN 3 (TECH STACK GRID) --- */
        .tech-stack-grid {{
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 10px 20px;
            padding: 15px;
            border: 1px dashed #d0d2cc;
            border-radius: 8px;
        }}
        .tech-stack-grid div:nth-child(odd) {{
            font-weight: bold;
            color: {accent_color};
        }}
        /* ------------------------------------------- */
        
    </style>
    """, unsafe_allow_html=True)


# =================================================================
# KOMPONEN 2: KARTU ANGGOTA (Versi Compact Anti-Bug)
# =================================================================
def kartu_anggota(nama, nim, peran, url_foto, quote, link_ig):
    # Membersihkan tanda kutip ganda dari quote
    cleaned_quote = quote.strip('"') 
    
    # Menghindari karakter khusus di nama dan peran agar tidak merusak HTML (jika ada)
    # Walaupun di sini kemungkinan kecil terjadi, ini praktik yang baik.
    safe_nama = nama.replace('<', '&lt;').replace('>', '&gt;')
    safe_peran = peran.replace('<', '&lt;').replace('>', '&gt;')

    # SELURUH KARTU DIRENDER DALAM SATU BLOK HTML
    html_code = f"""
    <div class="profile-card">
        <a href="{link_ig}" target="_blank" class="profile-link" title="Klik untuk ke Instagram">
            <img src="{url_foto}" class="profile-img">
        </a>
        <h4 style="margin: 5px 0 0px 0;">{safe_nama}</h4>
        <p class="nim">NIM: {nim}</p>
        
        <span class="role-badge">{safe_peran}</span> 
        
        <div class="quote-text">
            "{cleaned_quote}"
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


# =================================================================
# STRUKTUR UTAMA APLIKASI (MAIN APP LOGIC)
# =================================================================

# 1. Panggil Komponen Styling Global
styling_global_component(
    background_color="#e8e9e4", 
    accent_color="#5a6a62" 
) 

st.title("👥 Tim Pengembang")
st.markdown("Aplikasi ini dipersembahkan oleh **Kelompok 5** untuk memenuhi Tugas Besar Mata Kuliah **Teori Bahasa Otomata (TBO)**.")
st.write("---")

# 2. Kartu Anggota (Menggunakan 5 Kolom Kompak)
col_fahri, col_erlita, col_azmi, col_alden, col_ahmad = st.columns(5)

with col_fahri:
    kartu_anggota(
        nama="Fahri Khairun Ariansyah", 
        nim="1247050084", 
        peran="Lead Developer & Backend",
        # URL GAMBAR PENTING: Gunakan gambar yang benar-benar bisa diakses
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/fahrii.png", 
        quote="People can only save themselves. One person saving another is impossible.",
        link_ig="https://www.instagram.com/p_ftttt"
    )

with col_erlita:
    kartu_anggota(
        nama="Erlita Amelia", 
        nim="1247050088", 
        peran="Data search & QA",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto erlita.jpg",
        quote="Mengubah angka menjadi nada.",
        link_ig="https://www.instagram.com/erlitaall"
    )

with col_azmi:
    kartu_anggota(
        nama="Azmi Putri Kuswandi", 
        nim="1247050126", 
        peran="Backend & Audio Engineer",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto azmi.jpg",
        quote="Good things take time.",
        link_ig="https://www.instagram.com/azmiptr_"
    )

with col_alden:
    kartu_anggota(
        nama="Alden Shalih Falah", 
        nim="1247050050", 
        peran="Frontend & UI/UX",
        url_foto="https://raw.githubusercontent.com/erlitaal/ai_music_composer/main/images/foto alden.jpg",
        quote="The moment you drop 'if' is the moment your life starts moving forward.",
        link_ig="https://www.instagram.com/dennn.26sf"
    )

with col_ahmad:
    kartu_anggota(
        nama="Ahmad Maftuh Rojak", 
        nim="1247050100", 
        peran="Frontend & UI/UX",
        # URL GAMBAR ALTERNATIF (Avatar generator jika gambar utama bermasalah)
        url_foto="https://api.dicebear.com/7.x/avataaars/svg?seed=Jack",
        quote="growing freely.",
        link_ig="https://www.instagram.com/stagarling"
    )

st.write("---")

# 3. Tech Stack (Menggunakan Grid HTML)
st.markdown("### 🛠️ Tech Stack yang Digunakan")
st.markdown("""
<div class="tech-stack-grid">
    <div>🐍 **Python 3.10**</div> <div>Bahasa Pemrograman Utama.</div>
    <div>🌊 **Streamlit**</div> <div>Framework utama untuk Web App.</div>
    <div>🎹 **MidiUtil**</div> <div>Untuk Generasi File MIDI.</div>
    <div>🔊 **Scipy & NumPy**</div> <div>Pemrosesan Sinyal Audio Digital.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 50px;">
    © 2025 Kelompok 5 - Teknik Informatika. Dibuat dengan Python & Streamlit.
</div>
""", unsafe_allow_html=True)
