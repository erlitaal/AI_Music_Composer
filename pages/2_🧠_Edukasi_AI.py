import streamlit as st
import graphviz

# ----------------------
# GLOBAL STYLE - PREMIUM
# ----------------------
st.set_page_config(page_title="Cara Kerja AI", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* FONT */
    html, body, [class*="css"] {
        font-family: 'Georgia', serif !important;
    }

    /* BACKGROUND PREMIUM */
    body {
        background: linear-gradient(135deg, #f2efe9, #e5dfd4);
    }

    /* CARD STYLE */
    .card {
        background: #ffffffdd;
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e6e1d8;
    }

    /* SECTION TITLE */
    .section-title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #4b3f34;
        text-align: center;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 60px;
        padding-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE HEADER
# -------------------------
st.markdown("<div class='section-title'>🧠 Di Balik Layar: Bedah Logika AI</div>", unsafe_allow_html=True)
st.markdown("""
Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan **Teori Musik** dengan **Ilmu Komputer (TBO)** untuk menciptakan komposisi yang harmonis. Berikut adalah 3 pilar utamanya:
""")

st.write("")

# -------------------------
# BAGIAN 1: FSA
# -------------------------
col1, col2 = st.columns([2.2, 1.3])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("1. Finite State Automata (FSA)")
    st.info("**Peran:** Polisi Lalu Lintas Nada 👮‍♂️")

    st.markdown("""
    Dalam mata kuliah TBO, FSA didefinisikan sebagai mesin yang memiliki **State** dan **Transisi**. 
    Di aplikasi ini:
    * **State ($Q$):** Adalah nada-nada dalam piano (C, D, E, F, G, A, B).
    * **Input ($\Sigma$):** Adalah aturan Mood (Mayor/Minor).
    * **Fungsi Transisi ($\delta$):** Logika yang *melarang* AI memilih nada fals.
    
    > *Contoh:* Jika Mood = **Sedih (C Minor)**, maka State **E (Mi Natural)** adalah *Dead State* (Ditolak). 
    > AI dipaksa transisi ke **Eb (Mi Mol)**.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.caption("Visualisasi FSA Sederhana:")
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='3')
    graph.node('C', 'Start (C)', shape='doublecircle')
    graph.node('D', 'Nada D')
    graph.node('E', 'Nada E')
    graph.node('F', 'Nada F')
    graph.edge('C', 'D', label='1')
    graph.edge('D', 'E', label='1')
    graph.edge('E', 'F', label='0.5')
    graph.edge('F', 'C', label='Loop')
    st.graphviz_chart(graph)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# -------------------------
# BAGIAN 2: MARKOV CHAIN
# -------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("2. Markov Chain (Probabilitas)")
st.warning("**Peran:** Pengarang Melodi yang Kreatif 🎲")

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
