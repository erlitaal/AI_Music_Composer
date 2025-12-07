import streamlit as st
import graphviz

st.markdown("""
<style>
    /* IMPORT GOOGLE FONT - DROID SERIF */
    @import url('https://fonts.googleapis.com/css2?family=Droid+Serif:wght@700&display=swap');
    
    /* HILANGKAN IKON RANTAI DI HEADER */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    /* BACKGROUND CREAM MUDA DENGAN SENTUHAN ABU-ABU */
    .stApp {
        background-color: #FAF9F6 !important;  /* Cream muda dengan sedikit abu-abu */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* JUDUL UTAMA - DROID SERIF BOLD */
    h1 {
        font-family: 'Droid Serif', serif !important;
        font-weight: 700 !important;
        color: #2C3E50 !important;
        font-size: 2.5rem !important;
        margin-bottom: 1rem !important;
        letter-spacing: -0.5px;
    }
    
    /* JUDUL BAGIAN - DROID SERIF BOLD */
    h2 {
        font-family: 'Droid Serif', serif !important;
        font-weight: 700 !important;
        color: #2C3E50 !important;
        font-size: 1.8rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #ECF0F1;
    }
    
    /* SUB-JUDUL */
    h3, h4, h5, h6 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        color: #2C3E50 !important;
        font-weight: 600;
    }
    
    /* WARNA TEKS UTAMA */
    p, div, span, label, .stMarkdown, .stTitle, .stHeader {
        color: #2C3E50 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* TEKS BOLD/TEBAL */
    strong, b {
        color: #1A1A1A !important;  /* Sedikit lebih gelap untuk bold text */
        font-weight: 700;
    }
    
    /* WARNA DIVIDER - ABU-ABU MUDA */
    hr {
        border-color: #BDC3C7 !important;  /* Abu-abu muda */
        opacity: 0.5;
        margin: 2rem 0;
    }
    
    /* WARNA METRIC CARD */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #2C3E50 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
        font-weight: 600;
    }
    
    [data-testid="stMetricDelta"] svg {
        color: #2C3E50 !important;
    }
    
    /* WARNA ALERT BOXES */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.85) !important;
        border: 1px solid #ECF0F1 !important;
        border-left: 4px solid;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .stAlert [data-testid="stMarkdownContainer"] {
        color: #2C3E50 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* JUDUL DALAM ALERT BOX */
    .stAlert h3, .stAlert h4 {
        font-family: 'Droid Serif', serif !important;
        font-weight: 700 !important;
        margin-top: 0;
    }
    
    /* INFO BOX - Blue soft */
    div[data-testid="stAlert"] div:has(> div[data-testid="stMarkdownContainer"]:contains("Polisi")) {
        border-left-color: #3498DB !important;
    }
    
    /* WARNING BOX - Orange soft */
    div[data-testid="stAlert"] div:has(> div[data-testid="stMarkdownContainer"]:contains("Pengarang")) {
        border-left-color: #E67E22 !important;
    }
    
    /* SUCCESS BOX - Green soft */
    div[data-testid="stAlert"] div:has(> div[data-testid="stMarkdownContainer"]:contains("Penentu")) {
        border-left-color: #2ECC71 !important;
    }
    
    /* WARNA EXPANDER */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #2C3E50 !important;
        border: 1px solid #ECF0F1 !important;
        border-radius: 6px;
        font-weight: 600;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .streamlit-expanderContent {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid #ECF0F1 !important;
        border-top: none;
        border-radius: 0 0 6px 6px;
    }
    
    /* WARNA TABLE */
    table {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid #ECF0F1 !important;
        border-radius: 6px;
        overflow: hidden;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    th {
        background-color: #F8F9FA !important;
        color: #2C3E50 !important;
        font-weight: 700;
        border-bottom: 2px solid #ECF0F1 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    td {
        color: #2C3E50 !important;
        border-bottom: 1px solid #ECF0F1 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* CAPTION TEXT - Abu-abu medium */
    .stCaption {
        color: #7F8C8D !important;
        font-size: 0.85rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* QUOTE/BLOCKQUOTE STYLE */
    blockquote {
        border-left: 3px solid #BDC3C7;
        padding-left: 1rem;
        margin-left: 0;
        color: #5D6D7E;
        font-style: italic;
        background-color: rgba(236, 240, 241, 0.3);
        padding: 0.5rem 1rem;
        border-radius: 0 4px 4px 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* TITLE SPACING */
    .stTitle h1 {
        margin-bottom: 1.5rem !important;
    }
    
    /* GRAPHVIZ STYLING */
    .stGraphviz {
        border: 1px solid #ECF0F1;
        border-radius: 8px;
        padding: 1rem;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* TEXT DALAM GRAPHVIZ */
    .stGraphviz text {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    /* METRIC CARDS STYLING */
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.9);
        border: 1px solid #ECF0F1;
        border-radius: 8px;
        padding: 1rem;
        height: 100%;
    }
    
    /* FOOTER STYLING */
    .footer {
        text-align: center;
        color: #95A5A6 !important;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding: 1.5rem 0;
        border-top: 1px solid #ECF0F1;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* SCROLLBAR STYLING */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #FAF9F6;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #BDC3C7;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #95A5A6;
    }
    
    /* EMOJI DI JUDUL */
    h1 .emoji, h2 .emoji {
        font-family: "Segoe UI Emoji", "Apple Color Emoji", sans-serif !important;
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
col1, col2 = st.columns([2, 1])

with col1:
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

with col2:
    st.caption("Visualisasi FSA Sederhana:")
    # Membuat Diagram FSA menggunakan Graphviz
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='3')
    
    # Node
    graph.node('C', 'Start (C)', shape='doublecircle')
    graph.node('D', 'Nada D')
    graph.node('E', 'Nada E')
    graph.node('F', 'Nada F')
    
    # Edge (Transisi)
    graph.edge('C', 'D', label='1')
    graph.edge('D', 'E', label='1')
    graph.edge('E', 'F', label='0.5')
    graph.edge('F', 'C', label='Loop')
    
    st.graphviz_chart(graph)

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

with st.expander("🔍 Lihat Detail Pola (Pattern Library)"):
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
