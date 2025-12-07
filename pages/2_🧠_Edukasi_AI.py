import streamlit as st
import graphviz

# Custom CSS dengan warna musik yang menarik
st.markdown("""
<style>
    /* HILANGKAN IKON RANTAI DI HEADER */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #312e81 100%);
        font-family: 'Poppins', 'Segoe UI', system-ui, sans-serif;
        color: #f1f5f9;
    }
    
    /* Title Styling */
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #8b5cf6, #3b82f6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        padding-top: 1rem;
    }
    
    .main-subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 1.2rem;
        max-width: 800px;
        margin: 0 auto 3rem auto;
        line-height: 1.6;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 15px;
        color: #f8fafc;
    }
    
    .section-icon {
        font-size: 2.5rem;
    }
    
    /* Card Designs */
    .info-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(139, 92, 246, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        margin: 1.5rem 0;
    }
    
    /* Role Badges */
    .role-badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }
    
    .fsa-badge {
        background: linear-gradient(90deg, rgba(139, 92, 246, 0.2), rgba(59, 130, 246, 0.2));
        border: 1px solid rgba(139, 92, 246, 0.5);
        color: #a78bfa;
    }
    
    .markov-badge {
        background: linear-gradient(90deg, rgba(245, 158, 11, 0.2), rgba(251, 191, 36, 0.2));
        border: 1px solid rgba(245, 158, 11, 0.5);
        color: #fbbf24;
    }
    
    .pattern-badge {
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.2), rgba(52, 211, 153, 0.2));
        border: 1px solid rgba(16, 185, 129, 0.5);
        color: #34d399;
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(139, 92, 246, 0.1);
        transition: transform 0.3s ease;
        height: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(139, 92, 246, 0.3);
    }
    
    /* Example Box */
    .example-box {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(59, 130, 246, 0.1));
        border-left: 4px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        font-style: italic;
    }
    
    /* List Styling */
    .styled-list {
        color: #cbd5e1;
        line-height: 1.8;
        padding-left: 1.2rem;
    }
    
    .styled-list li {
        margin-bottom: 0.8rem;
    }
    
    /* Table Styling */
    .pattern-table {
        width: 100%;
        background: rgba(30, 41, 59, 0.8);
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
    
    .pattern-table th {
        background: rgba(139, 92, 246, 0.2);
        color: #e2e8f0;
        padding: 1rem;
        font-weight: 600;
        text-align: left;
    }
    
    .pattern-table td {
        padding: 1rem;
        border-bottom: 1px solid rgba(139, 92, 246, 0.1);
        color: #cbd5e1;
    }
    
    /* Footer */
    .music-footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(139, 92, 246, 0.2);
        color: #94a3b8;
        font-size: 0.9rem;
    }
    
    /* Custom Divider */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #8b5cf6, #3b82f6, transparent);
        margin: 2.5rem 0;
        border: none;
    }
    
    /* Graphviz Container */
    .graph-container {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Cara Kerja AI", page_icon="🧠", layout="wide")

# Header Section
st.markdown('<h1 class="main-title">🧠 Di Balik Layar: Bedah Logika AI</h1>', unsafe_allow_html=True)
st.markdown("""
<p class="main-subtitle">
Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan <strong style="color:#8b5cf6">Teori Musik</strong> 
dengan <strong style="color:#3b82f6">Ilmu Komputer (TBO)</strong> untuk menciptakan komposisi yang harmonis. 
Berikut adalah 3 pilar utamanya:
</p>
""", unsafe_allow_html=True)

# Custom Divider
st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- BAGIAN 1: FSA ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown('<h2 class="section-header"><span class="section-icon">⚡</span>1. Finite State Automata (FSA)</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="role-badge fsa-badge">👮‍♂️ Peran: Polisi Lalu Lintas Nada</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("""
    <p style="color:#e2e8f0; font-size:1.05rem; line-height:1.7;">
    Dalam mata kuliah TBO, FSA didefinisikan sebagai mesin yang memiliki <strong style="color:#8b5cf6">State</strong> dan <strong style="color:#8b5cf6">Transisi</strong>. 
    Di aplikasi ini:
    </p>
    
    <ul class="styled-list">
        <li><strong style="color:#a78bfa">State ($Q$):</strong> Adalah nada-nada dalam piano (C, D, E, F, G, A, B).</li>
        <li><strong style="color:#a78bfa">Input ($\Sigma$):</strong> Adalah aturan Mood (Mayor/Minor).</li>
        <li><strong style="color:#a78bfa">Fungsi Transisi ($\delta$):</strong> Logika yang <em>melarang</em> AI memilih nada fals.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="example-box">', unsafe_allow_html=True)
    st.markdown("""
    <strong style="color:#f1f5f9">🎵 Contoh Implementasi:</strong><br>
    Jika Mood = <strong style="color:#fbbf24">Sedih (C Minor)</strong>, maka State <strong style="color:#fbbf24">E (Mi Natural)</strong> 
    adalah <em>Dead State</em> (Ditolak). AI dipaksa transisi ke <strong style="color:#34d399">Eb (Mi Mol)</strong>.
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="graph-container">', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#94a3b8; margin-bottom:1rem; font-weight:600;">🎼 Visualisasi FSA Sederhana</p>', unsafe_allow_html=True)
    
    # Membuat Diagram FSA menggunakan Graphviz
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='4', bgcolor='transparent', fontcolor='white')
    
    # Node styling
    graph.attr('node', style='filled', fillcolor='#1e293b', fontcolor='white', 
               color='#8b5cf6', fontname='Poppins')
    
    # Edge styling
    graph.attr('edge', color='#94a3b8', fontcolor='#cbd5e1')
    
    # Node
    graph.node('C', 'Start (C)', shape='doublecircle', fillcolor='#8b5cf6', color='#a78bfa')
    graph.node('D', 'Nada D')
    graph.node('E', 'Nada E')
    graph.node('F', 'Nada F')
    
    # Edge (Transisi)
    graph.edge('C', 'D', label='1')
    graph.edge('D', 'E', label='1')
    graph.edge('E', 'F', label='0.5')
    graph.edge('F', 'C', label='Loop')
    
    st.graphviz_chart(graph)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- BAGIAN 2: MARKOV CHAIN ---
st.markdown('<h2 class="section-header"><span class="section-icon">🎲</span>2. Markov Chain (Probabilitas)</h2>', unsafe_allow_html=True)

st.markdown('<div class="role-badge markov-badge">🎵 Peran: Pengarang Melodi yang Kreatif</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
<p style="color:#e2e8f0; font-size:1.05rem; line-height:1.7;">
Agar musik tidak kaku, kami menggunakan <strong style="color:#f59e0b">Markov Chain</strong> untuk menentukan <em>langkah selanjutnya</em> berdasarkan <em>langkah saat ini</em>.
Bayangkan AI melempar dadu untuk setiap ketukan:
</p>
</div>
""", unsafe_allow_html=True)

# Metrics Cards
c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<p style="color:#fbbf24; font-size:2.5rem; font-weight:800; margin:0;">60%</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#f8fafc; font-weight:600; font-size:1.1rem;">Stepwise<br><span style="color:#94a3b8; font-size:0.9rem;">Langkah Pendek</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#cbd5e1; font-size:0.9rem; margin-top:1rem;">Nada naik/turun ke tetangganya (misal: Do ke Re). Membuat melodi mengalir.</p>', unsafe_allow_html=True)
    st.markdown('<div style="height:4px; background:linear-gradient(90deg,#f59e0b,#fbbf24); border-radius:2px; margin-top:1rem;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<p style="color:#3b82f6; font-size:2.5rem; font-weight:800; margin:0;">30%</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#f8fafc; font-weight:600; font-size:1.1rem;">Harmonic Leap<br><span style="color:#94a3b8; font-size:0.9rem;">Lompatan</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#cbd5e1; font-size:0.9rem; margin-top:1rem;">Melompat ke nada Chord (misal: Do ke Sol). Memberikan variasi.</p>', unsafe_allow_html=True)
    st.markdown('<div style="height:4px; background:linear-gradient(90deg,#3b82f6,#06b6d4); border-radius:2px; margin-top:1rem;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<p style="color:#10b981; font-size:2.5rem; font-weight:800; margin:0;">10%</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#f8fafc; font-weight:600; font-size:1.1rem;">Rhythmic<br><span style="color:#94a3b8; font-size:0.9rem;">Variasi</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#cbd5e1; font-size:0.9rem; margin-top:1rem;">Variasi ritme cepat/lambat agar tidak monoton.</p>', unsafe_allow_html=True)
    st.markdown('<div style="height:4px; background:linear-gradient(90deg,#10b981,#34d399); border-radius:2px; margin-top:1rem;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- BAGIAN 3: PATTERN ---
st.markdown('<h2 class="section-header"><span class="section-icon">🥁</span>3. Pattern-Based Accompaniment</h2>', unsafe_allow_html=True)

st.markdown('<div class="role-badge pattern-badge">🎸 Peran: Penentu Identitas Genre</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
<p style="color:#e2e8f0; font-size:1.05rem; line-height:1.7;">
Berbeda dengan melodi yang <em>Generative</em> (dikarang di tempat), instrumen pengiring (Drum, Bass, Chord) menggunakan 
<strong style="color:#10b981">Pola Statis (Fixed Pattern)</strong> untuk menjaga identitas genre.
</p>
</div>
""", unsafe_allow_html=True)

# Expandable Pattern Library
with st.expander("🔍 **Lihat Detail Pola (Pattern Library)**", expanded=False):
    st.markdown("""
    <div class="pattern-table">
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="background:rgba(139, 92, 246, 0.3);">Genre</th>
                <th style="background:rgba(139, 92, 246, 0.3);">Pola Drum</th>
                <th style="background:rgba(139, 92, 246, 0.3);">Gaya Bass</th>
                <th style="background:rgba(139, 92, 246, 0.3);">Gaya Piano</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong style="color:#fbbf24">Pop</strong></td>
                <td>Straight Beat (Kick 1&3)</td>
                <td>Root Notes (Lurus)</td>
                <td>Block Chords (Panjang)</td>
            </tr>
            <tr>
                <td><strong style="color:#3b82f6">Jazz</strong></td>
                <td>Swing Beat (Ride Cymbal)</td>
                <td>Walking Bass (Jalan)</td>
                <td>Comping (Syncopated)</td>
            </tr>
            <tr>
                <td><strong style="color:#10b981">Ballad</strong></td>
                <td>Soft Beat (Rimshot)</td>
                <td>Root & 5th (Jarang)</td>
                <td>Arpeggio (Petikan)</td>
            </tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="music-footer">
    <p>© 2025 Kelompok 5 - Teknik Informatika. Dibuat dengan ❤️ menggunakan Python & Streamlit.</p>
    <p style="margin-top:0.5rem; color:#64748b; font-size:0.85rem;">
    AI Music Composer | Teori Bahasa dan Otomata | Semester 3
    </p>
</div>
""", unsafe_allow_html=True)

# Add some decorative elements
st.markdown("""
<style>
    /* Animasi not musik */
    @keyframes floatNote {
        0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.1; }
        50% { transform: translateY(-10px) rotate(5deg); opacity: 0.15; }
    }
    
    .decoration-note {
        position: fixed;
        font-size: 2rem;
        animation: floatNote 8s ease-in-out infinite;
        z-index: -1;
        pointer-events: none;
    }
    
    .note-1 { top: 20%; left: 5%; animation-delay: 0s; }
    .note-2 { top: 40%; right: 10%; animation-delay: 2s; }
    .note-3 { bottom: 30%; left: 15%; animation-delay: 4s; }
    .note-4 { bottom: 15%; right: 5%; animation-delay: 6s; }
</style>

<div class="decoration-note note-1">♪</div>
<div class="decoration-note note-2">♫</div>
<div class="decoration-note note-3">♬</div>
<div class="decoration-note note-4">🎵</div>
""", unsafe_allow_html=True)
