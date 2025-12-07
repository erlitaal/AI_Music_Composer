import streamlit as st
import graphviz

st.set_page_config(
    page_title="Cara Kerja AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS yang lebih sederhana dan pasti work
st.markdown("""
<style>
    /* Reset dasar */
    .stApp {
        background-color: #f5f1e8 !important;
    }
    
    /* Hilangkan header chain */
    [data-testid="stHeaderActionElements"] {
        display: none;
    }
    
    /* Container utama */
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fffef9;
        border: 1px solid #e8e0d0;
        border-radius: 4px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Judul */
    .main-title {
        text-align: center;
        color: #3c3c3c;
        font-family: 'Georgia', serif;
        font-size: 2.5rem;
        margin-bottom: 10px;
        padding-bottom: 15px;
        border-bottom: 2px solid #8B7355;
    }
    
    .title-accent {
        color: #8B7355;
        font-style: italic;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 40px;
        line-height: 1.6;
        font-style: italic;
    }
    
    /* Section */
    .section {
        background: white;
        padding: 25px;
        margin: 30px 0;
        border-radius: 4px;
        border: 1px solid #e8e0d0;
        border-top: 4px solid #8B7355;
    }
    
    .section-title {
        color: #3c3c3c;
        font-size: 1.5rem;
        font-family: 'Georgia', serif;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .section-number {
        background: #8B7355;
        color: white;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        background: #f8f4e9;
        color: #8B7355;
        padding: 8px 16px;
        border-radius: 20px;
        font-style: italic;
        margin: 10px 0 20px 0;
        border: 1px solid #D4AF37;
    }
    
    /* Content */
    .content {
        color: #444;
        line-height: 1.7;
        margin-bottom: 15px;
    }
    
    /* List */
    .content-list {
        color: #444;
        line-height: 1.7;
        padding-left: 20px;
        margin: 20px 0;
    }
    
    .content-list li {
        margin-bottom: 10px;
    }
    
    /* Example box */
    .example {
        background: #f9f7f1;
        padding: 20px;
        border-radius: 4px;
        border-left: 4px solid #8B7355;
        margin: 20px 0;
        font-style: italic;
    }
    
    /* Metrics */
    .metric-container {
        display: flex;
        gap: 20px;
        margin: 25px 0;
    }
    
    .metric-card {
        flex: 1;
        text-align: center;
        padding: 20px;
        background: white;
        border: 1px solid #e8e0d0;
        border-radius: 4px;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #8B7355;
        margin-bottom: 10px;
    }
    
    .metric-label {
        color: #3c3c3c;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .metric-desc {
        color: #666;
        font-size: 0.9rem;
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
        padding: 12px;
        text-align: left;
        border: 1px solid #e8e0d0;
    }
    
    .pattern-table td {
        padding: 12px;
        border: 1px solid #e8e0d0;
        color: #666;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e8e0d0;
        color: #8B7355;
        font-size: 0.9rem;
    }
    
    /* Piano decoration */
    .piano-keys {
        height: 15px;
        background: repeating-linear-gradient(90deg, 
            #000 0%, #000 8px, 
            #fff 8px, #fff 16px);
        margin: 30px 0;
        border-radius: 2px;
    }
    
    /* Graph container */
    .graph-box {
        padding: 20px;
        background: white;
        border: 1px solid #e8e0d0;
        border-radius: 4px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Mulai konten
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Header
st.markdown("""
<h1 class="main-title">Di Balik Layar: <span class="title-accent">Bedah Logika AI</span></h1>
<p class="subtitle">
Aplikasi ini bukan sekadar pemutar musik acak. Kami menggabungkan Teori Musik dengan Ilmu Komputer (TBO) 
untuk menciptakan komposisi yang harmonis. Berikut adalah 3 pilar utamanya:
</p>
""", unsafe_allow_html=True)

# Piano decoration
st.markdown('<div class="piano-keys"></div>', unsafe_allow_html=True)

# --- BAGIAN 1: FSA ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-title">
        <span class="section-number">1</span>
        <span>Finite State Automata (FSA)</span>
    </div>
    <div class="badge">👮‍♂️ Polisi Lalu Lintas Nada</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p class="content">
    Dalam mata kuliah TBO, FSA didefinisikan sebagai mesin yang memiliki <strong style="color:#8B7355">State</strong> 
    dan <strong style="color:#8B7355">Transisi</strong>. Di aplikasi ini:
    </p>
    
    <ul class="content-list">
        <li><strong style="color:#8B7355">State ($Q$):</strong> Adalah nada-nada dalam piano (C, D, E, F, G, A, B).</li>
        <li><strong style="color:#8B7355">Input ($\Sigma$):</strong> Adalah aturan Mood (Mayor/Minor).</li>
        <li><strong style="color:#8B7355">Fungsi Transisi ($\delta$):</strong> Logika yang <em>melarang</em> AI memilih nada fals.</li>
    </ul>
    
    <div class="example">
        <strong style="color:#8B7355">🎹 Contoh Implementasi:</strong><br>
        Jika Mood = <strong>Sedih (C Minor)</strong>, maka State <strong>E (Mi Natural)</strong> 
        adalah <em>Dead State</em> (Ditolak). AI dipaksa transisi ke <strong>Eb (Mi Mol)</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="graph-box">', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8B7355; font-style:italic;">Diagram Transisi Nada</p>', unsafe_allow_html=True)
    
    # Graphviz
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR', size='3')
    graph.attr('node', style='filled', fillcolor='#f9f7f1', color='#8B7355')
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
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    <span class="section-number">2</span>
    <span>Markov Chain (Probabilitas)</span>
</div>
<div class="badge">🎲 Pengarang Melodi yang Kreatif</div>
""", unsafe_allow_html=True)

st.markdown("""
<p class="content">
Agar musik tidak kaku, kami menggunakan <strong style="color:#8B7355">Markov Chain</strong> untuk menentukan 
<em>langkah selanjutnya</em> berdasarkan <em>langkah saat ini</em>. Bayangkan AI melempar dadu untuk setiap ketukan:
</p>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">60%</div>
        <div class="metric-label">Stepwise</div>
        <p class="metric-desc">Langkah Pendek<br>Nada ke tetangganya</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">30%</div>
        <div class="metric-label">Harmonic Leap</div>
        <p class="metric-desc">Lompatan<br>Melompat ke nada Chord</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">10%</div>
        <div class="metric-label">Rhythmic Variation</div>
        <p class="metric-desc">Variasi<br>Ritme cepat/lambat</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="piano-keys"></div>', unsafe_allow_html=True)

# --- BAGIAN 3: PATTERN ---
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    <span class="section-number">3</span>
    <span>Pattern-Based Accompaniment</span>
</div>
<div class="badge">🥁 Penentu Identitas Genre</div>
""", unsafe_allow_html=True)

st.markdown("""
<p class="content">
Berbeda dengan melodi yang <em>Generative</em> (dikarang di tempat), instrumen pengiring (Drum, Bass, Chord) menggunakan 
<strong style="color:#8B7355">Pola Statis (Fixed Pattern)</strong> untuk menjaga identitas genre.
</p>
""", unsafe_allow_html=True)

# Table dalam expander
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
    </table>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Kelompok 5 - Teknik Informatika</p>
    <p style="color:#999; margin-top:5px;">Dibuat dengan Python & Streamlit | Teori Bahasa dan Otomata</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Tambahkan sedikit JavaScript untuk animasi (opsional)
st.markdown("""
<script>
    // Animasi sederhana untuk metric cards
    document.addEventListener('DOMContentLoaded', function() {
        const cards = document.querySelectorAll('.metric-card');
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'all 0.5s ease';
            
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 300 + (index * 100));
        });
    });
</script>
""", unsafe_allow_html=True)
