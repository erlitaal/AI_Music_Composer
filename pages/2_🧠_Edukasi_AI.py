import streamlit as st
import graphviz

st.set_page_config(
    page_title="Cara Kerja AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS yang lebih clean dan fix bug
st.markdown("""
<style>
    /* Reset Streamlit default */
    .stApp {
        background-color: #f5f1e8;
        font-family: 'Georgia', serif;
    }
    
    /* Hide chain icon */
    [data-testid="stHeaderActionElements"] {
        display: none;
    }
    
    /* Main container */
    .main-content {
        max-width: 1000px;
        margin: 40px auto;
        padding: 40px;
        background: #fffef9;
        border: 1px solid #e0d8c9;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(139, 115, 85, 0.1);
    }
    
    /* Judul - SATU WARNA saja (coklat emas) */
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #8B7355;
        margin-bottom: 10px;
        padding-bottom: 20px;
        border-bottom: 3px double #D4AF37;
        font-family: 'Garamond', serif;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.15rem;
        line-height: 1.7;
        margin: 20px auto 40px;
        max-width: 800px;
        font-style: italic;
    }
    
    /* Piano decoration - lebih jelas */
    .piano-decoration {
        height: 25px;
        background: repeating-linear-gradient(90deg, 
            #000 0%, #000 12px, 
            #fff 12px, #fff 24px,
            #000 24px, #000 36px,
            #fff 36px, #fff 48px);
        margin: 30px auto;
        width: 80%;
        border-radius: 3px;
        border: 1px solid #8B7355;
    }
    
    /* Section */
    .section-box {
        background: white;
        padding: 30px;
        margin: 40px 0;
        border-radius: 6px;
        border: 1px solid #e0d8c9;
        position: relative;
        overflow: hidden;
    }
    
    /* HAPUS garis coklat di atas yang kosong! */
    
    /* Section header */
    .section-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 2px solid #f0ebe0;
    }
    
    .section-number {
        background: #8B7355;
        color: white;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
        font-family: 'Georgia', serif;
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
        background: #f8f4e9;
        color: #8B7355;
        padding: 8px 20px;
        border-radius: 20px;
        font-style: italic;
        margin: 10px 0 25px 0;
        border: 1px solid #D4AF37;
        font-size: 1rem;
    }
    
    /* Content */
    .content-text {
        color: #444;
        line-height: 1.7;
        font-size: 1.05rem;
        margin-bottom: 15px;
    }
    
    /* List styling */
    .styled-list {
        color: #444;
        line-height: 1.7;
        padding-left: 20px;
        margin: 20px 0;
    }
    
    .styled-list li {
        margin-bottom: 12px;
        padding-left: 10px;
    }
    
    /* Example box - PERBAIKI yang kosong */
    .example-box {
        background: #f9f7f1;
        padding: 25px;
        border-radius: 6px;
        margin: 25px 0;
        border-left: 5px solid #8B7355;
        position: relative;
    }
    
    .example-title {
        color: #8B7355;
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Graph container */
    .graph-container {
        padding: 20px;
        background: #f9f7f1;
        border-radius: 6px;
        border: 1px solid #e0d8c9;
        margin-top: 20px;
    }
    
    /* Metric cards */
    .metrics-grid {
        display: flex;
        gap: 20px;
        margin: 30px 0;
    }
    
    .metric-item {
        flex: 1;
        text-align: center;
        padding: 25px 15px;
        background: white;
        border: 2px solid #e0d8c9;
        border-radius: 6px;
        transition: all 0.3s ease;
    }
    
    .metric-item:hover {
        border-color: #8B7355;
        transform: translateY(-5px);
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: bold;
        color: #8B7355;
        margin-bottom: 10px;
    }
    
    .metric-main-label {
        color: #3c3c3c;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 5px;
    }
    
    .metric-sub-label {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 10px;
    }
    
    .metric-desc {
        color: #777;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Table */
    .pattern-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        background: white;
    }
    
    .pattern-table th {
        background: #f8f4e9;
        color: #8B7355;
        padding: 15px;
        text-align: left;
        border: 1px solid #e0d8c9;
        font-weight: 600;
    }
    
    .pattern-table td {
        padding: 15px;
        border: 1px solid #e0d8c9;
        color: #555;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e0d8c9;
        color: #8B7355;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ====================
# KONTEN UTAMA
# ====================

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# HEADER
st.markdown('<h1 class="main-title">Di Balik Layar: Bedah Logika AI</h1>', unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan <strong>Teori Musik</strong> 
dengan <strong>Ilmu Komputer (TBO)</strong> untuk menciptakan komposisi yang harmonis. 
Berikut adalah 3 pilar utamanya:
</p>
""", unsafe_allow_html=True)

# Piano decoration
st.markdown('<div class="piano-decoration"></div>', unsafe_allow_html=True)

# ====================
# BAGIAN 1: FSA
# ====================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    
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
    
    <ul class="styled-list">
        <li><strong style="color:#8B7355">State ($Q$):</strong> Adalah nada-nada dalam piano (C, D, E, F, G, A, B).</li>
        <li><strong style="color:#8B7355">Input ($\Sigma$):</strong> Adalah aturan Mood (Mayor/Minor).</li>
        <li><strong style="color:#8B7355">Fungsi Transisi ($\delta$):</strong> Logika yang <em>melarang</em> AI memilih nada fals.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # CONTOH IMPLEMENTASI - TIDAK KOSONG LAGI
    st.markdown("""
    <div class="example-box">
        <div class="example-title">
            <span>🎹</span>
            <span>Contoh Implementasi</span>
        </div>
        <p style="color:#444; line-height:1.6; margin:0;">
            Jika Mood = <strong style="color:#8B7355">Sedih (C Minor)</strong>, maka State <strong style="color:#8B7355">E (Mi Natural)</strong> 
            adalah <em>Dead State</em> (Ditolak). AI dipaksa transisi ke <strong style="color:#8B7355">Eb (Mi Mol)</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8B7355; font-style:italic; margin-bottom:15px;">Diagram Transisi Nada</p>', unsafe_allow_html=True)
    
    # Graphviz diagram
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='3')
    graph.attr('node', style='filled', fillcolor='#f9f7f1', 
               color='#8B7355', fontname='Georgia', fontsize='11')
    graph.attr('edge', color='#8B7355', fontcolor='#666')
    
    graph.node('C', 'Start (C)', shape='doublecircle', fillcolor='#8B7355', fontcolor='white')
    graph.node('D', 'Nada D')
    graph.node('E', 'Nada E')
    graph.node('F', 'Nada F')
    
    graph.edge('C', 'D', label='Transisi 1')
    graph.edge('D', 'E', label='Transisi 1')
    graph.edge('E', 'F', label='Transisi 0.5')
    graph.edge('F', 'C', label='Loop')
    
    st.graphviz_chart(graph, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="piano-decoration"></div>', unsafe_allow_html=True)

# ====================
# BAGIAN 2: MARKOV CHAIN
# ====================
st.markdown('<div class="section-box">', unsafe_allow_html=True)

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

# Metrics - FIXED
st.markdown('<div class="metrics-grid">', unsafe_allow_html=True)

st.markdown("""
<div class="metric-item">
    <div class="metric-value">60%</div>
    <div class="metric-main-label">Stepwise</div>
    <div class="metric-sub-label">Langkah Pendek</div>
    <p class="metric-desc">Nada ke tetangganya (misal: Do ke Re)</p>
</div>

<div class="metric-item">
    <div class="metric-value">30%</div>
    <div class="metric-main-label">Harmonic Leap</div>
    <div class="metric-sub-label">Lompatan</div>
    <p class="metric-desc">Melompat ke nada Chord (misal: Do ke Sol)</p>
</div>

<div class="metric-item">
    <div class="metric-value">10%</div>
    <div class="metric-main-label">Rhythmic Variation</div>
    <div class="metric-sub-label">Variasi</div>
    <p class="metric-desc">Variasi ritme cepat/lambat agar tidak monoton</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close section-box

st.markdown('<div class="piano-decoration"></div>', unsafe_allow_html=True)

# ====================
# BAGIAN 3: PATTERN
# ====================
st.markdown('<div class="section-box">', unsafe_allow_html=True)

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

# Table dalam expander
with st.expander("🔍 **Lihat Detail Pola (Pattern Library)**", expanded=False):
    st.markdown("""
    <table class="pattern-table">
        <thead>
            <tr>
                <th>Genre</th>
                <th>Pola Drum</th>
                <th>Gaya Bass</th>
                <th>Gaya Piano</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong style="color:#8B7355">Pop</strong></td>
                <td>Straight Beat (Kick 1&3)</td>
                <td>Root Notes (Lurus)</td>
                <td>Block Chords (Panjang)</td>
            </tr>
            <tr>
                <td><strong style="color:#8B7355">Jazz</strong></td>
                <td>Swing Beat (Ride Cymbal)</td>
                <td>Walking Bass (Jalan)</td>
                <td>Comping (Syncopated)</td>
            </tr>
            <tr>
                <td><strong style="color:#8B7355">Ballad</strong></td>
                <td>Soft Beat (Rimshot)</td>
                <td>Root & 5th (Jarang)</td>
                <td>Arpeggio (Petikan)</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ====================
# FOOTER
# ====================
st.markdown("""
<div class="footer">
    <p>© 2025 Kelompok 5 - Teknik Informatika</p>
    <p style="color:#999; margin-top:8px; font-size:0.85rem;">
    Dibuat dengan Python & Streamlit | Teori Bahasa dan Otomata
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-content
