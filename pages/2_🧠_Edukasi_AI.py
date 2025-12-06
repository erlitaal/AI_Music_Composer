import streamlit as st
import graphviz

st.set_page_config(
    page_title="Cara Kerja AI",
    page_icon="🧠",
    layout="wide"
)

# -------------------- GLOBAL STYLING (PREMIUM CLASSIC) --------------------
st.markdown("""
<style>

    body {
        background-color: #F7F2E8 !important;
    }

    /* Header title */
    h1, h2, h3, h4 {
        font-family: 'Georgia', serif;
        color: #5A4636 !important;
    }

    /* Paragraph */
    p, li, td, th {
        font-family: 'Georgia', serif;
        color: #4A3B2A;
        font-size: 1.05rem;
    }

    /* Divider warna gold */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(to right, #D4AF37, #8B6F47);
        margin-top: 20px;
        margin-bottom: 30px;
    }

    /* Box info/warning/success custom */
    .stAlert {
        background-color: #F5EAD5 !important;
        border-left: 5px solid #D4AF37 !important;
        color: #4A3B2A !important;
    }

    /* Metric cards */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #5A4636 !important;
        font-family: 'Georgia', serif;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #EFE6D9 !important;
        color: #5A4636 !important;
        font-family: 'Georgia', serif;
        font-size: 1.1rem !important;
        border-radius: 8px;
        padding: 8px !important;
    }

    /* Footnote */
    .footer {
        text-align: center;
        color: #7A6A58;
        font-family: 'Georgia';
        margin-top: 40px;
    }

</style>
""", unsafe_allow_html=True)

# ----------------------- JUDUL HALAMAN -----------------------
st.title("🧠 Di Balik Layar: Bedah Logika AI")
st.markdown("""
Aplikasi ini tidak hanya mengacak nada, tapi menggabungkan **Teori Musik** dan **Ilmu Komputer (TBO)**
untuk menghasilkan harmoni yang cerdas. Berikut 3 pilar yang menjadi otak di balik AI ini:
""")

st.divider()

# ----------------------- BAGIAN 1: FSA -----------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.header("1. Finite State Automata (FSA)")
    st.info("**Peran:** Polisi Lalu Lintas Nada 👮‍♂️")
    st.markdown("""
    Dalam TBO, FSA adalah mesin dengan **State** dan **Transisi**.

    Di aplikasi ini:
    - **State ($Q$):** Nada piano (C, D, E, F, G, A, B)
    - **Input ($\\Sigma$):** Mood Mayor/Minor
    - **Transisi ($\\delta$):** Aturan yang mencegah AI memilih nada fals

    > Jika mood = **Sedih (C Minor)**  
    > maka state **E Natural** menjadi *Dead State*  
    > dan AI dipaksa memilih **Eb**.
    """)

with col2:
    st.caption("Visualisasi FSA:")
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

st.divider()

# ----------------------- BAGIAN 2: MARKOV -----------------------
st.header("2. Markov Chain (Probabilitas)")
st.warning("**Peran:** Pengarang Melodi yang Kreatif 🎲")

st.markdown("""
Markov Chain membantu AI memilih langkah nada berikutnya berdasarkan probabilitas.
Bayangkan setiap ketukan AI seperti melempar dadu:
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(label="Stepwise (Pendek)", value="60%", delta="Dominan")
    st.caption("Melangkah ke nada tetangga. Hasilnya lebih halus dan mengalir.")

with c2:
    st.metric(label="Harmonic Leap", value="30%")
    st.caption("Lompatan ke nada chord untuk variasi.")

with c3:
    st.metric(label="Rhythmic Variation", value="10%")
    st.caption("Variasi ritme cepat/lambat.")

st.divider()

# ----------------------- BAGIAN 3: PATTERN -----------------------
st.header("3. Pattern-Based Accompaniment")
st.success("**Peran:** Penentu Identitas Genre 🥁")

st.markdown("""
Berbeda dengan melodi yang bersifat *generative*, pengiring musik seperti drum dan bass
menggunakan pola statis untuk mempertahankan identitas genre.
""")

with st.expander("🔍 Lihat Detail Pola (Pattern Library)"):
    st.markdown("""
    | Genre | Pola Drum | Gaya Bass | Gaya Piano |
    | :--- | :--- | :--- | :--- |
    | **Pop** | Straight Beat | Root Notes | Block Chords |
    | **Jazz** | Swing Beat | Walking Bass | Comping |
    | **Ballad** | Soft Beat | Root + 5th | Arpeggio |
    """)

st.markdown(
    "<div class='footer'>© 2025 Kelompok 5 - Teknik Informatika</div>",
    unsafe_allow_html=True
)
