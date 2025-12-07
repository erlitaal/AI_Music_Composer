import streamlit as st
import graphviz

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Droid+Serif:wght@700&display=swap');
    
    /* Sembunyikan ikon header */
    [data-testid="stHeaderActionElements"] { display: none !important; }
    
    /* Background cream */
    .stApp { background-color: #FAF9F6 !important; }
    
    /* Font judul */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Droid Serif', serif !important;
        font-weight: 700 !important;
        color: #2C3E50 !important;
    }
    
    h1 { font-size: 2.5rem !important; margin-bottom: 1rem !important; }
    h2 { font-size: 1.8rem !important; margin-top: 2rem !important; margin-bottom: 1rem !important; }
    
    /* Warna teks utama */
    .main .block-container {
        color: #2C3E50 !important;
    }
    
    p, li, td, th, span, div:not([class*="stAlert"]) {
        color: #2C3E50 !important;
    }
    
    /* Divider */
    hr {
        border-color: #BDC3C7 !important;
        margin: 2rem 0 !important;
        opacity: 0.5;
    }
    
    /* Container untuk graphviz */
    .graphviz-container {
        border: 1px solid #ECF0F1;
        border-radius: 12px;
        padding: 1.5rem;
        background-color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin: 1rem 0;
    }
    
    /* Alert boxes styling sederhana - tanpa mengubah struktur Streamlit */
    div[data-testid="stAlert"] {
        border: 1px solid #D1D5D8 !important;
        border-left: 4px solid #95A5A6 !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Info alert */
    div.stAlert:has(> div > div > svg[data-testid="InfoIcon"]) {
        border-left-color: #7F8C8D !important;
    }
    
    /* Warning alert */
    div.stAlert:has(> div > div > svg[data-testid="WarningIcon"]) {
        border-left-color: #95A5A6 !important;
    }
    
    /* Success alert */
    div.stAlert:has(> div > div > svg[data-testid="SuccessIcon"]) {
        border-left-color: #5D6D7E !important;
    }
    
    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.9);
        border: 1px solid #ECF0F1;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #95A5A6 !important;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding: 1.5rem 0;
        border-top: 1px solid #ECF0F1;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Cara Kerja AI", page_icon="🧠", layout="wide")

st.title("🧠 Di Balik Layar: Bedah Logika AI")
st.markdown("""
Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan **Teori Musik** dengan **Ilmu Komputer (TBO)** untuk menciptakan komposisi yang harmonis. Berikut adalah 3 pilar utamanya:
""")

st.divider()

# --- BAGIAN 1: FSA ---
st.header("1. Finite State Automata (FSA)")
st.info("**Peran:** Polisi Lalu Lintas Nada 👮‍♂️")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("""
    Dalam mata kuliah TBO, FSA didefinisikan sebagai mesin yang memiliki **State** dan **Transisi**. 
    Di aplikasi ini:
    
    * **State ($Q$):** Adalah nada-nada dalam piano (C, D, E, F, G, A, B).
    * **Input ($\Sigma$):** Adalah aturan Mood (Mayor/Minor).
    * **Fungsi Transisi ($\delta$):** Logika yang *melarang* AI memilih nada fals.
    
    > *Contoh:* Jika Mood = **Sedih (C Minor)**, maka State **E (Mi Natural)** adalah *Dead State* (Ditolak). 
    > AI dipaksa transisi ke **Eb (Mi Mol)**.
    """)

with col2:
    st.markdown('<div class="graphviz-container">', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-weight: bold; color: #2C3E50; margin-bottom: 1rem;">Visualisasi FSA Sederhana</div>', unsafe_allow_html=True)
    
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='8,4')
    
    graph.node('C', 'Start (C)', shape='doublecircle')
    graph.node('D', 'Nada D', shape='circle')
    graph.node('E', 'Nada E', shape='circle')
    graph.node('F', 'Nada F', shape='circle')
    
    graph.edge('C', 'D', label=' 1')
    graph.edge('D', 'E', label=' 1')
    graph.edge('E', 'F', label=' 0.5')
    graph.edge('F', 'C', label=' Loop')
    
    st.graphviz_chart(graph, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- BAGIAN 2: MARKOV CHAIN ---
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

st.divider()

# --- BAGIAN 3: PATTERN ---
st.header("3. Pattern-Based Accompaniment")
st.success("**Peran:** Penentu Identitas Genre 🥁")

st.markdown("""
Berbeda dengan melodi yang *Generative* (dikarang di tempat), instrumen pengiring (Drum, Bass, Chord) menggunakan **Pola Statis (Fixed Pattern)** untuk menjaga identitas genre.
""")

with st.expander("🔍 Lihat Detail Pola (Pattern Library)", expanded=False):
    st.markdown("""
    | Genre | Pola Drum | Gaya Bass | Gaya Piano |
    | :--- | :--- | :--- | :--- |
    | **Pop** | Straight Beat (Kick 1&3) | Root Notes (Lurus) | Block Chords (Panjang) |
    | **Jazz** | Swing Beat (Ride Cymbal) | Walking Bass (Jalan) | Comping (Syncopated) |
    | **Ballad** | Soft Beat (Rimshot) | Root & 5th (Jarang) | Arpeggio (Petikan) |
    """)

st.markdown("""
<div class="footer">
    © 2025 Kelompok 5 - Teknik Informatika. Dibuat dengan Python & Streamlit.
</div>
""", unsafe_allow_html=True)
