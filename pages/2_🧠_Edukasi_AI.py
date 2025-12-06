import streamlit as st

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎹",
    layout="wide"
)

# ----------------------
# GLOBAL CSS STYLE
# ----------------------
st.markdown("""
<style>

    /* Background cream */
    body, .stApp {
        background-color: #F7EEDB !important; 
        font-family: 'Georgia', serif !important;
    }

    /* Judul */
    h1, h2, h3, h4 {
        font-family: 'Georgia', serif !important;
        color: #5E4024 !important;
    }

    /* Button style */
    .stButton>button {
        background-color: #E0C9A6 !important;
        color: #4A3B2A !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        border: none !important;
        font-family: 'Georgia', serif !important;
        font-size: 16px !important;
    }

    .stButton>button:hover {
        background-color: #D1B38A !important;
        color: #3E2E1E !important;
    }

    /* Input box */
    .stTextInput>div>div>input {
        background-color: #FFF8EE !important;
        border-radius: 8px !important;
        border: 1px solid #D8C4A2 !important;
        font-family: 'Georgia', serif !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F4E7D2 !important;
    }

</style>
""", unsafe_allow_html=True)

# ----------------------
# LAYOUT AWAL
# ----------------------
st.title("🎹 AI Music Composer")
st.write("Selamat datang! Ini adalah tampilan awal UI versi cream theme.")

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("Chat Area (Placeholder)")
    st.write("Nanti di sini area chat akan ditata lebih rapi…")

with col2:
    st.subheader("Sidebar / Panel Kanan")
    st.write("Ini panel tambahan, bisa untuk setting atau history.")

st.write("## Input Chat")
user_input = st.text_input("Ketik pesan di sini", "")
send = st.button("Send")

if send:
    st.write(f"Pesan terkirim: {user_input}")st.warning("**Peran:** Pengarang Melodi yang Kreatif 🎲")

st.markdown("""
Agar musik tidak kaku, kami menggunakan **Markov Chain** untuk menentukan *langkah selanjutnya* berdasarkan *langkah saat ini*.
Bayangkan AI melempar dadu untuk setiap ketukan:
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(label="Stepwise (Langkah Pendek)", value="60%", delta="Dominan")
    st.caption("Nada naik/turun ke tetangganya (misal: Do ke Re). Membuat melodi mengalir.")

with c2:
    st.metric(label="Harmonic Leap (Lompatan)", value="30%")
    st.caption("Melompat ke nada Chord (misal: Do ke Sol). Memberikan variasi.")

with c3:
    st.metric(label="Rhythmic Variation", value="10%")
    st.caption("Variasi ritme cepat/lambat agar tidak monoton.")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# -------------------------
# BAGIAN 3: PATTERN
# -------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("3. Pattern-Based Accompaniment")
st.success("**Peran:** Penentu Identitas Genre 🥁")

st.markdown("""
Berbeda dengan melodi yang *Generative* (dikarang di tempat), instrumen pengiring (Drum, Bass, Chord) menggunakan **Pola Statis (Fixed Pattern)** untuk menjaga identitas genre.
""")

with st.expander("🔍 Lihat Detail Pola (Pattern Library)"):
    st.markdown("""
    | Genre | Pola Drum | Gaya Bass | Gaya Piano |
    | :--- | :--- | :--- | :--- |
    | **Pop** | Straight Beat (Kick 1&3) | Root Notes (Lurus) | Block Chords (Panjang) |
    | **Jazz** | Swing Beat (Ride Cymbal) | Walking Bass (Jalan) | Comping (Syncopated) |
    | **Ballad** | Soft Beat (Rimshot) | Root & 5th (Jarang) | Arpeggio (Petikan) |
    """)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown("""
<div class='footer'>
    © 2025 Kelompok 5 - Teknik Informatika. Dibuat dengan Python & Streamlit.
</div>
""", unsafe_allow_html=True)
