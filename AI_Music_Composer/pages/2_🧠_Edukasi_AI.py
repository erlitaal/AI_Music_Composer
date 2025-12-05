import streamlit as st
import graphviz # Library bawaan Streamlit untuk diagram

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

st.markdown("---")
st.caption("© 2025 Kelompok 5 TBO - Dibuat dengan Python & Streamlit")