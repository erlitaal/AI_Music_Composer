import streamlit as st
import graphviz

st.markdown("""
<style>
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    .stApp {
        background: #f5f1e8;
        font-family: 'Georgia', 'Times New Roman', serif;
        color: #3c3c3c;
    }
    
    /* Reset Streamlit default styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }
    
    /* Elegant border */
    .page-border {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: 9999;
        border: 8px solid transparent;
        background: linear-gradient(#f5f1e8, #f5f1e8) padding-box,
                    linear-gradient(45deg, #8B7355, #D4AF37, #8B7355) border-box;
    }
    
    /* Music note decorations */
    .music-note {
        position: fixed;
        font-size: 2rem;
        color: rgba(139, 115, 85, 0.15);
        z-index: -1;
        opacity: 0.4;
    }
    
    .note-1 { top: 10%; left: 5%; transform: rotate(-15deg); }
    .note-2 { top: 20%; right: 8%; transform: rotate(10deg); }
    .note-3 { bottom: 25%; left: 10%; transform: rotate(-20deg); }
    .note-4 { bottom: 15%; right: 12%; transform: rotate(15deg); }
    
    /* Main container */
    .classic-container {
        background: rgba(255, 253, 248, 0.95);
        padding: 3rem;
        margin: 2rem auto;
        border-radius: 4px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.05);
        position: relative;
        z-index: 1;
        border: 1px solid #e8e0d0;
    }
    
    /* Header */
    .elegant-header {
        text-align: center;
        margin-bottom: 3rem;
        padding-bottom: 1.5rem;
        border-bottom: 2px solid #e8e0d0;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #2c2c2c;
        margin-bottom: 0.5rem;
        font-family: 'Garamond', serif;
        letter-spacing: 0.5px;
    }
    
    .title-accent {
        color: #8B7355;
        font-style: italic;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #666;
        line-height: 1.6;
        max-width: 700px;
        margin: 0 auto;
        font-style: italic;
    }
    
    /* Section styling */
    .section-container {
        margin: 2.5rem 0;
        padding: 2rem;
        background: white;
        border-radius: 4px;
        border: 1px solid #e8e0d0;
        position: relative;
    }
    
    .section-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #D4AF37, #8B7355);
    }
    
    /* Section header */
    .section-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 1.5rem;
    }
    
    .section-number {
        width: 36px;
        height: 36px;
        background: #8B7355;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    .section-title {
        font-size: 1.6rem;
        font-weight: 600;
        color: #3c3c3c;
        margin: 0;
    }
    
    /* Role badge */
    .role-badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        background: #f8f4e9;
        border: 1px solid #D4AF37;
        border-radius: 20px;
        font-style: italic;
        color: #8B7355;
        margin: 0.5rem 0 1.5rem 0;
        font-size: 0.9rem;
    }
    
    /* Content */
    .content-text {
        color: #3c3c3c;
        line-height: 1.7;
        font-size: 1.05rem;
        margin-bottom: 1rem;
    }
    
    .content-list {
        color: #3c3c3c;
        line-height: 1.7;
        padding-left: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .content-list li {
        margin-bottom: 0.8rem;
    }
    
    /* Example box */
    .example-box {
        background: #f9f7f1;
        padding: 1.5rem;
        border-radius: 4px;
        border-left: 4px solid #8B7355;
        margin: 1.5rem 0;
        font-style: italic;
    }
    
    /* Graph container */
    .graph-container {
        background: white;
        padding: 1.5rem;
        border-radius: 4px;
        border: 1px solid #e8e0d0;
        margin-top: 2rem;
    }
    
    /* Metric cards */
    .metric-container {
        display: flex;
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        flex: 1;
        background: white;
        padding: 1.5rem;
        border-radius: 4px;
        border: 1px solid #e8e0d0;
        text-align: center;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #8B7355;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #3c3c3c;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Table */
    .pattern-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5rem 0;
    }
    
    .pattern-table th {
        background: #f8f4e9;
        padding: 0.8rem;
        text-align: left;
        font-weight: 600;
        color: #8B7355;
        border: 1px solid #e8e0d0;
    }
    
    .pattern-table td {
        padding: 0.8rem;
        border: 1px solid #e8e0d0;
        color: #666;
    }
    
    /* Footer */
    .elegant-footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e8e0d0;
        color: #8B7355;
        font-size: 0.9rem;
    }
    
    /* Piano decoration */
    .piano-keys {
        height: 20px;
        background: repeating-linear-gradient(
            90deg,
            #000,
            #000 2%,
            #fff 2%,
            #fff 4%
        );
        margin: 2rem 0;
        border-radius: 2px;
    }
</style>

<!-- Border -->
<div class="page-border"></div>

<!-- Music notes -->
<div class="music-note note-1">♪</div>
<div class="music-note note-2">♫</div>
<div class="music-note note-3">♬</div>
<div class="music-note note-4">🎵</div>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Cara Kerja AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main container
st.markdown('<div class="classic-container">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="elegant-header">
    <h1 class="main-title">Di Balik Layar: <span class="title-accent">Bedah Logika AI</span></h1>
    <p class="subtitle">
        Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan Teori Musik dengan Ilmu Komputer (TBO) 
        untuk menciptakan komposisi yang harmonis. Berikut adalah 3 pilar utamanya:
    </p>
</div>
""", unsafe_allow_html=True)

# Piano decoration
st.markdown('<div class="piano-keys"></div>', unsafe_allow_html=True)

# --- BAGIAN 1: FSA ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        <div class="section-number">1</div>
        <h2 class="section-title">Finite State Automata (FSA)</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="role-badge">👮‍♂️ Polisi Lalu Lintas Nada</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="content-text">
    Dalam mata kuliah TBO, FSA didefinisikan sebagai mesin yang memiliki <strong style="color:#8B7355">State</strong> 
    dan <strong style="color:#8B7355">Transisi</strong>. Di aplikasi ini:
    </p>
    
    <ul class="content-list">
        <li><strong style="color:#8B7355">State ($Q$):</strong> Adalah nada-nada dalam piano (C, D, E, F, G, A, B).</li>
        <li><strong style="color:#8B7355">Input ($\Sigma$):</strong> Adalah aturan Mood (Mayor/Minor).</li>
        <li><strong style="color:#8B7355">Fungsi Transisi ($\delta$):</strong> Logika yang <em>melarang</em> AI memilih nada fals.</li>
    </ul>
    
    <div class="example-box">
        <strong style="color:#8B7355">🎹 Contoh Implementasi:</strong><br>
        Jika Mood = <strong>Sedih (C Minor)</strong>, maka State <strong>E (Mi Natural)</strong> 
        adalah <em>Dead State</em> (Ditolak). AI dipaksa transisi ke <strong>Eb (Mi Mol)</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8B7355; font-style:italic; margin-bottom:1rem;">Diagram Transisi Nada</p>', unsafe_allow_html=True)
    
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='3', bgcolor='transparent')
    graph.attr('node', style='filled', fillcolor='#f9f7f1', 
               color='#8B7355', fontname='Georgia', fontsize='10')
    graph.attr('edge', color='#8B7355')
    
    graph.node('C', 'C', shape='doublecircle', fillcolor='#8B7355', fontcolor='white')
    graph.node('D', 'D')
    graph.node('E', 'E')
    graph.node('F', 'F')
    
    graph.edge('C', 'D', label='1')
    graph.edge('D', 'E', label='1')
    graph.edge('E', 'F', label='0.5')
    graph.edge('F', 'C', label='Loop')
    
    st.graphviz_chart(graph)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="piano-keys"></div>', unsafe_allow_html=True)

# --- BAGIAN 2: MARKOV CHAIN ---
st.markdown('<div class="section-container">', unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-number">2</div>
    <h2 class="section-title">Markov Chain (Probabilitas)</h2>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="role-badge">🎲 Pengarang Melodi yang Kreatif</div>', unsafe_allow_html=True)

st.markdown("""
<p class="content-text">
Agar musik tidak kaku, kami menggunakan <strong style="color:#8B7355">Markov Chain</strong> untuk menentukan 
<em>langkah selanjutnya</em> berdasarkan <em>langkah saat ini</em>. Bayangkan AI melempar dadu untuk setiap ketukan:
</p>
""", unsafe_allow_html=True)

# Metric cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">60%</div>
        <div class="metric-label">Stepwise</div>
        <p style="color:#666; font-size:0.9rem; margin:0;">
            Langkah Pendek<br>
            Nada naik/turun ke tetangganya
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">30%</div>
        <div class="metric-label">Harmonic Leap</div>
        <p style="color:#666; font-size:0.9rem; margin:0;">
            Lompatan<br>
            Melompat ke nada Chord
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">10%</div>
        <div class="metric-label">Rhythmic Variation</div>
        <p style="color:#666; font-size:0.9rem; margin:0;">
            Variasi<br>
            Variasi ritme cepat/lambat
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="piano-keys"></div>', unsafe_allow_html=True)

# --- BAGIAN 3: PATTERN ---
st.markdown('<div class="section-container">', unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-number">3</div>
    <h2 class="section-title">Pattern-Based Accompaniment</h2>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="role-badge">🥁 Penentu Identitas Genre</div>', unsafe_allow_html=True)

st.markdown("""
<p class="content-text">
Berbeda dengan melodi yang <em>Generative</em> (dikarang di tempat), instrumen pengiring (Drum, Bass, Chord) menggunakan 
<strong style="color:#8B7355">Pola Statis (Fixed Pattern)</strong> untuk menjaga identitas genre.
</p>
""", unsafe_allow_html=True)

with st.expander("🔍 **Lihat Detail Pola (Pattern Library)**", expanded=False):
    st.markdown("""
    <table class="pattern-table">
        <tr>
            <th>Genre</th>
            <th>Pola Drum</th>
            <th>Gaya Bass</th>
            <th>Gaya Piano</th>
        </tr>
        <tr>
            <td><strong>Pop</strong></td>
            <td>Straight Beat (Kick 1&3)</td>
            <td>Root Notes (Lurus)</td>
            <td>Block Chords (Panjang)</td>
        </tr>
        <tr>
            <td><strong>Jazz</strong></td>
            <td>Swing Beat (Ride Cymbal)</td>
            <td>Walking Bass (Jalan)</td>
            <td>Comping (Syncopated)</td>
        </tr>
        <tr>
            <td><strong>Ballad</strong></td>
            <td>Soft Beat (Rimshot)</td>
            <td>Root & 5th (Jarang)</td>
            <td>Arpeggio (Petikan)</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="elegant-footer">
    <p>© 2025 Kelompok 5 - Teknik Informatika</p>
    <p style="margin-top:0.5rem; color:#999; font-size:0.85rem;">
    Dibuat dengan Python & Streamlit | Teori Bahasa dan Otomata
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
