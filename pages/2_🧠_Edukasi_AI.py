import streamlit as st
import graphviz

st.markdown("""
<style>
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f1e8 0%, #f0ebe0 100%);
        font-family: 'Georgia', 'Times New Roman', serif;
        color: #3c3c3c;
    }
    
    /* Elegant border decoration */
    .page-border {
        position: fixed;
        pointer-events: none;
        z-index: 9999;
    }
    
    .border-top {
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #8B7355, #D4AF37, #8B7355);
    }
    
    .border-left {
        top: 0;
        left: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #8B7355, #D4AF37, #8B7355);
    }
    
    .border-right {
        top: 0;
        right: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #8B7355, #D4AF37, #8B7355);
    }
    
    .border-bottom {
        bottom: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #8B7355, #D4AF37, #8B7355);
    }
    
    /* Music note decorations */
    .music-note {
        position: absolute;
        font-size: 2rem;
        color: rgba(139, 115, 85, 0.2);
        z-index: -1;
        opacity: 0.4;
    }
    
    .note-1 { top: 10%; left: 5%; transform: rotate(-15deg); }
    .note-2 { top: 20%; right: 8%; transform: rotate(10deg); }
    .note-3 { bottom: 25%; left: 10%; transform: rotate(-20deg); }
    .note-4 { bottom: 15%; right: 12%; transform: rotate(15deg); }
    .note-5 { top: 45%; left: 15%; transform: rotate(5deg); }
    
    /* Main container */
    .classic-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 3rem 2rem;
        position: relative;
        background: rgba(255, 253, 248, 0.8);
        border-radius: 2px;
    }
    
    /* Header with decorative line */
    .elegant-header {
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        padding-bottom: 1.5rem;
    }
    
    .elegant-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 25%;
        right: 25%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #8B7355, transparent);
    }
    
    .main-title {
        font-size: 3.2rem;
        font-weight: 700;
        color: #2c2c2c;
        margin-bottom: 0.5rem;
        font-family: 'Garamond', serif;
        letter-spacing: 1px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .title-accent {
        color: #8B7355;
        font-style: italic;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #666;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto;
        font-style: italic;
    }
    
    /* Section styling */
    .section-container {
        margin: 3rem 0;
        padding: 2.5rem;
        background: white;
        border-radius: 4px;
        border: 1px solid #e0d8c9;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
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
    
    /* Section header with music icon */
    .section-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #e0d8c9;
    }
    
    .section-number {
        width: 40px;
        height: 40px;
        background: #8B7355;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
        font-family: 'Georgia', serif;
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #3c3c3c;
        margin: 0;
        font-family: 'Garamond', serif;
    }
    
    /* Role badge */
    .role-badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        background: #f8f4e9;
        border: 2px solid #D4AF37;
        border-radius: 20px;
        font-style: italic;
        color: #8B7355;
        margin: 0.5rem 0 1.5rem 0;
        font-size: 0.95rem;
    }
    
    /* Content box */
    .content-box {
        background: #f9f7f1;
        padding: 2rem;
        border-radius: 4px;
        border-left: 4px solid #8B7355;
        margin: 1.5rem 0;
    }
    
    /* Example box with musical border */
    .example-box {
        background: linear-gradient(to right, #fefcf6, #f9f7f1);
        padding: 1.5rem;
        border-radius: 4px;
        border: 1px solid #e0d8c9;
        margin: 2rem 0;
        position: relative;
    }
    
    .example-box::before {
        content: '🎵';
        position: absolute;
        top: -15px;
        left: 20px;
        background: white;
        padding: 0 10px;
        font-size: 1.2rem;
    }
    
    /* Metric cards with vintage style */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        background: white;
        padding: 1.8rem;
        border-radius: 4px;
        border: 1px solid #e0d8c9;
        text-align: center;
        position: relative;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    }
    
    .metric-value {
        font-size: 2.8rem;
        font-weight: 700;
        color: #8B7355;
        margin-bottom: 0.5rem;
        font-family: 'Georgia', serif;
    }
    
    /* Graphviz container */
    .graph-container {
        background: white;
        padding: 2rem;
        border-radius: 4px;
        border: 1px solid #e0d8c9;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    /* Table styling */
    .vintage-table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        border: 1px solid #e0d8c9;
        font-family: 'Georgia', serif;
    }
    
    .vintage-table th {
        background: #f8f4e9;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
        color: #8B7355;
        border-bottom: 2px solid #e0d8c9;
    }
    
    .vintage-table td {
        padding: 1rem;
        border-bottom: 1px solid #f0ebe0;
        color: #666;
    }
    
    /* Piano key decoration */
    .piano-decoration {
        height: 30px;
        background: linear-gradient(90deg, 
            #000 0%, #000 2%, 
            #fff 2%, #fff 4%, 
            #000 4%, #000 6%,
            #fff 6%, #fff 8%,
            #000 8%, #000 10%,
            #fff 10%, #fff 12%,
            #000 12%, #000 14%,
            #fff 14%, #fff 16%,
            #000 16%, #000 18%,
            #fff 18%, #fff 20%,
            #000 20%, #000 22%,
            #fff 22%, #fff 24%,
            #000 24%, #000 26%,
            #fff 26%, #fff 28%,
            #000 28%, #000 30%);
        margin: 2rem 0;
        border-radius: 2px;
    }
    
    /* Footer */
    .elegant-footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid #e0d8c9;
        color: #8B7355;
        font-size: 0.9rem;
        font-style: italic;
    }
    
    /* Decorative musical staff */
    .music-staff {
        height: 60px;
        background: 
            repeating-linear-gradient(
                to bottom,
                transparent,
                transparent 9px,
                #8B7355 9px,
                #8B7355 10px
            );
        background-size: 100% 50px;
        margin: 2rem 0;
        position: relative;
        opacity: 0.3;
    }
</style>

<!-- Border decorations -->
<div class="page-border border-top"></div>
<div class="page-border border-left"></div>
<div class="page-border border-right"></div>
<div class="page-border border-bottom"></div>

<!-- Music note decorations -->
<div class="music-note note-1">♪</div>
<div class="music-note note-2">♫</div>
<div class="music-note note-3">♬</div>
<div class="music-note note-4">🎵</div>
<div class="music-note note-5">🎶</div>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Cara Kerja AI", page_icon="🧠", layout="wide")

# Main container
st.markdown('<div class="classic-container">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="elegant-header">
    <h1 class="main-title">Di Balik Layar: <span class="title-accent">Bedah Logika AI</span></h1>
    <p class="subtitle">
    Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan <strong style="color:#8B7355">Teori Musik</strong> 
    dengan <strong style="color:#8B7355">Ilmu Komputer (TBO)</strong> untuk menciptakan komposisi yang harmonis.
    </p>
</div>
""", unsafe_allow_html=True)

# Piano decoration
st.markdown('<div class="piano-decoration"></div>', unsafe_allow_html=True)

# --- BAGIAN 1: FSA ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        <div class="section-number">I</div>
        <h2 class="section-title">Finite State Automata</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="role-badge">👮‍♂️ Polisi Lalu Lintas Nada</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-box">
        <p style="color:#3c3c3c; line-height:1.8; font-size:1.05rem;">
        Dalam mata kuliah TBO, FSA didefinisikan sebagai mesin yang memiliki <strong style="color:#8B7355">State</strong> dan <strong style="color:#8B7355">Transisi</strong>. 
        Di aplikasi ini:
        </p>
        
        <ul style="color:#3c3c3c; line-height:1.8; padding-left:1.2rem; margin:1.5rem 0;">
            <li><strong style="color:#8B7355">State ($Q$):</strong> Adalah nada-nada dalam piano (C, D, E, F, G, A, B).</li>
            <li><strong style="color:#8B7355">Input ($\Sigma$):</strong> Adalah aturan Mood (Mayor/Minor).</li>
            <li><strong style="color:#8B7355">Fungsi Transisi ($\delta$):</strong> Logika yang <em>melarang</em> AI memilih nada fals.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong style="color:#8B7355">🎹 Contoh Implementasi:</strong><br><br>
        Jika Mood = <strong>Sedih (C Minor)</strong>, maka State <strong>E (Mi Natural)</strong> 
        adalah <em>Dead State</em> (Ditolak). AI dipaksa transisi ke <strong>Eb (Mi Mol)</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8B7355; font-style:italic; margin-bottom:1.5rem;">Diagram Transisi Nada</p>', unsafe_allow_html=True)
    
    # Graphviz diagram dengan warna vintage
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='4', bgcolor='transparent')
    graph.attr('node', style='filled', fillcolor='#f9f7f1', fontname='Georgia', 
               color='#8B7355', fontsize='12', fontcolor='#3c3c3c')
    graph.attr('edge', color='#8B7355', fontcolor='#666')
    
    graph.node('C', 'Start (C)', shape='doublecircle', fillcolor='#8B7355', fontcolor='white')
    graph.node('D', 'Nada D', fillcolor='#f8f4e9')
    graph.node('E', 'Nada E', fillcolor='#f8f4e9')
    graph.node('F', 'Nada F', fillcolor='#f8f4e9')
    
    graph.edge('C', 'D', label='Transisi 1')
    graph.edge('D', 'E', label='Transisi 1')
    graph.edge('E', 'F', label='Transisi 0.5')
    graph.edge('F', 'C', label='Loop')
    
    st.graphviz_chart(graph)
    st.markdown('</div>', unsafe_allow_html=True)

# Music staff decoration
st.markdown('<div class="music-staff"></div>', unsafe_allow_html=True)

# --- BAGIAN 2: MARKOV CHAIN ---
st.markdown('<div class="section-container">', unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-number">II</div>
    <h2 class="section-title">Markov Chain</h2>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="role-badge">🎲 Pengarang Melodi yang Kreatif</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content-box">
    <p style="color:#3c3c3c; line-height:1.8; font-size:1.05rem;">
    Agar musik tidak kaku, kami menggunakan <strong style="color:#8B7355">Markov Chain</strong> untuk menentukan 
    <em>langkah selanjutnya</em> berdasarkan <em>langkah saat ini</em>. Bayangkan AI melempar dadu untuk setiap ketukan:
    </p>
</div>
""", unsafe_allow_html=True)

# Metric cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">60%</div>
        <h3 style="color:#3c3c3c; margin:0.5rem 0; font-weight:600;">Stepwise</h3>
        <p style="color:#666; font-size:0.9rem; margin:0;">Langkah Pendek</p>
        <div style="height:4px; background:#f0ebe0; border-radius:2px; margin:1rem 0;">
            <div style="width:60%; height:100%; background:#8B7355; border-radius:2px;"></div>
        </div>
        <p style="color:#666; font-size:0.9rem; margin-top:1rem;">Nada naik/turun ke tetangganya (misal: Do ke Re)</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">30%</div>
        <h3 style="color:#3c3c3c; margin:0.5rem 0; font-weight:600;">Harmonic Leap</h3>
        <p style="color:#666; font-size:0.9rem; margin:0;">Lompatan</p>
        <div style="height:4px; background:#f0ebe0; border-radius:2px; margin:1rem 0;">
            <div style="width:30%; height:100%; background:#D4AF37; border-radius:2px;"></div>
        </div>
        <p style="color:#666; font-size:0.9rem; margin-top:1rem;">Melompat ke nada Chord (misal: Do ke Sol)</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">10%</div>
        <h3 style="color:#3c3c3c; margin:0.5rem 0; font-weight:600;">Rhythmic</h3>
        <p style="color:#666; font-size:0.9rem; margin:0;">Variasi</p>
        <div style="height:4px; background:#f0ebe0; border-radius:2px; margin:1rem 0;">
            <div style="width:10%; height:100%; background:#8B7355; border-radius:2px;"></div>
        </div>
        <p style="color:#666; font-size:0.9rem; margin-top:1rem;">Variasi ritme cepat/lambat agar tidak monoton</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Piano decoration
st.markdown('<div class="piano-decoration"></div>', unsafe_allow_html=True)

# --- BAGIAN 3: PATTERN ---
st.markdown('<div class="section-container">', unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-number">III</div>
    <h2 class="section-title">Pattern-Based Accompaniment</h2>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="role-badge">🥁 Penentu Identitas Genre</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content-box">
    <p style="color:#3c3c3c; line-height:1.8; font-size:1.05rem;">
    Berbeda dengan melodi yang <em>Generative</em> (dikarang di tempat), instrumen pengiring (Drum, Bass, Chord) menggunakan 
    <strong style="color:#8B7355">Pola Statis (Fixed Pattern)</strong> untuk menjaga identitas genre.
    </p>
</div>
""", unsafe_allow_html=True)

with st.expander("🔍 **Lihat Detail Pola (Pattern Library)**", expanded=False):
    st.markdown("""
    <table class="vintage-table">
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
