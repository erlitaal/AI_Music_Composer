import streamlit as st
import random
import numpy as np
import os
import requests
import tempfile
import subprocess
import uuid
import time
from midiutil import MIDIFile
from io import BytesIO
from datetime import datetime
from midi2audio import FluidSynth
from scipy.io import wavfile


# --- PAGE CONFIG ---
st.set_page_config(page_title="Generator Musik", page_icon="🎵", layout="wide", initial_sidebar_state="collapsed")

# --- INITIALIZE SESSION STATE ---
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'current_mood' not in st.session_state:
    st.session_state['current_mood'] = None
if 'is_generated' not in st.session_state:
    st.session_state['is_generated'] = False

# --- CSS HIDE UI & NAVBAR ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400&display=swap');
    
    /* SEMBUNYIKAN UI BAWAAN */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stHeader"] { background-color: transparent; }
    [data-testid="stToolbar"] { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }
    
    /* BACKGROUND */
    .stApp { background-color: #E8E8E5; }
    
    /* NAVBAR */
    div[data-testid="stPageLink-NavLink"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    div[data-testid="stPageLink-NavLink"] p {
        font-family: 'Lato', sans-serif;
        font-size: 1rem;
        font-weight: 700;
        color: #666 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div[data-testid="stPageLink-NavLink"]:hover p {
        color: #000 !important;
        text-decoration: underline;
    }
    div[data-testid="stPageLink-NavLink"] svg { display: none; }
    
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
c_nav1, c_nav2, c_nav3, c_nav4 = st.columns([3, 1, 1, 1])
with c_nav1:
    st.markdown("<h3 style='margin:0; font-family: Playfair Display; color:black;'>KELOMPOK 5</h3>", unsafe_allow_html=True)
with c_nav2:
    st.page_link("Home.py", label="HOME", use_container_width=True)
with c_nav3:
    st.page_link("pages/1_Generator.py", label="GENERATOR", use_container_width=True)
with c_nav4:
    st.page_link("pages/2_Tentang_Kami.py", label="ABOUT", use_container_width=True)

st.write("---")

# ==========================================
# 1. DATABASE & CONFIG
# ==========================================

KEYS = {
    "C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, 
    "F": 65, "F#": 66, "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71
}

SCALE_INTERVALS = {
    "Major": [0, 2, 4, 5, 7, 9, 11],
    "Minor": [0, 2, 3, 5, 7, 8, 10],
    "Harmonic Minor": [0, 2, 3, 5, 7, 8, 11],
    "Dorian": [0, 2, 3, 5, 7, 9, 10], 
    "Blues": [0, 3, 5, 6, 7, 10]      
}

MOOD_PRESETS = {
    "Morning Pop": {
        "scale": "Major", "prog": "The Golden Loop (I-V-vi-IV)", 
        "bpm": 120, "style": "Pop", "instr": "Grand Piano",
        "tracks": ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        "desc": "Pop ceria dengan tempo cepat.",
        "color": "#E6B800" # Emas Tua (Elegan)
    },
    "Melancholy": {
        "scale": "Major", "prog": "Emotional Turn (vi-IV-I-V)", 
        "bpm": 65, "style": "Ballad", "instr": "Grand Piano",
        "tracks": ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        "desc": "Ballad lambat dengan nuansa melankolis.",
        "color": "#5D6D7E" # Abu-abu Biru (Kalem)
    },
    "Midnight Jazz": {
        "scale": "Major", "prog": "Jazz Standard (ii-V-I)", 
        "bpm": 90, "style": "Jazz", "instr": "Electric Piano (Rhodes)",
        "tracks": ["Melodi", "Chord", "Bass", "Drum"], 
        "desc": "Swing feel dengan chord 7th.",
        "color": "#8D6E63" # Coklat Kopi
    },
    "The Epic Saga": {
        "scale": "Harmonic Minor", "prog": "Dark Tension (i-ii-vii)", 
        "bpm": 135, "style": "Orchestra", "instr": "Violin",
        "tracks": ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        "desc": "Nuansa orkestra yang intens dan cepat.",
        "color": "#800000" # Merah Marun Gelap
    }
}

PROGRESSIONS = {
    "The Golden Loop (I-V-vi-IV)": [0, 4, 5, 3],
    "Emotional Turn (vi-IV-I-V)": [5, 3, 0, 4],
    "Jazz Standard (ii-V-I)": [1, 4, 0, 0], 
    "Dark Tension (i-ii-vii)": [0, 1, 6, 0],   
    "Canon Walk (I-V-vi-iii)": [0, 4, 5, 2] 
}

INSTRUMENTS = {
    "Grand Piano": 0, "Electric Piano (Rhodes)": 4, 
    "Nylon Guitar": 24, "Steel Guitar": 25, "Overdrive Guitar": 29,
    "Violin": 40, "Strings": 48,
    "Saxophone": 65, "Trumpet": 56,
    "Synth Lead": 81
}

GROOVE_CONFIG = {
    "Pop": {"swing": 0.0, "strum": 0.05, "comping": "Block", "drum": "Standard"},
    "Ballad": {"swing": 0.0, "strum": 0.02, "comping": "Arpeggio", "drum": "Soft"},
    "Jazz": {"swing": 0.15, "strum": 0.0, "comping": "Syncopated", "drum": "Jazz"},
    "Orchestra": {"swing": 0.0, "strum": 0.0, "comping": "Block", "drum": "Orchestral"}
}

DRUM_PATTERNS = {
    "Standard": [1,0,3,0, 2,0,3,0, 1,0,3,0, 2,0,3,0],
    "Soft":     [1,0,0,0, 0,0,0,0, 2,0,0,0, 0,0,0,0],
    "Jazz":     [1,0,0,4, 0,0,4,0, 0,0,0,4, 0,0,4,0],
    "Orchestral": [1,0,0,0, 2,0,0,0, 1,0,0,0, 2,0,0,0] 
}

# ==========================================
# 2. LOGIC ENGINE
# ==========================================

def get_chord_notes(root, scale_name, degree, style="Pop"):
    intervals = SCALE_INTERVALS[scale_name]
    scale_len = len(intervals)
    chord_root = root + intervals[degree % scale_len]
    
    n1 = chord_root
    n2 = root + intervals[(degree + 2) % scale_len] + (12 if (degree+2)>=scale_len else 0)
    n3 = root + intervals[(degree + 4) % scale_len] + (12 if (degree+4)>=scale_len else 0)
    notes = [n1, n2, n3]
    
    if style == "Jazz":
        n4 = root + intervals[(degree + 6) % scale_len] + (12 if (degree+6)>=scale_len else 0)
        notes.append(n4)
    return notes

def generate_structure(key, scale, prog_name, bars, style):
    root = KEYS[key]
    prog_list = PROGRESSIONS[prog_name]
    structure = []
    for i in range(bars):
        deg = prog_list[i % len(prog_list)]
        c_notes = get_chord_notes(root, scale, deg, style)
        structure.append({
            "bar_index": i, "chord_notes": c_notes, "root_note": c_notes[0], "style": style
        })
    return structure

def generate_melody(structure, bars, scale_name):
    melody_events = []
    total_beats = bars * 4
    current_time = 0
    
    root_base = structure[0]["root_note"]
    intervals = SCALE_INTERVALS[scale_name]
    full_scale = []
    for i in range(2):
        for val in intervals: full_scale.append(root_base + val + (i*12))
        
    last_note = full_scale[len(full_scale)//2]
    style = structure[0]["style"]
    
    while current_time < total_beats:
        if style == "Jazz": dur = random.choices([0.5, 1.0], weights=[0.6, 0.4])[0]
        elif style == "Ballad": dur = random.choices([0.5, 1.0, 2.0], weights=[0.2, 0.5, 0.3])[0]
        else: dur = random.choices([0.5, 1.0], weights=[0.4, 0.6])[0]
            
        if current_time + dur > total_beats: dur = total_beats - current_time
        
        bar_idx = int(current_time // 4)
        if bar_idx >= len(structure): bar_idx = len(structure)-1
        curr_chord = structure[bar_idx]["chord_notes"]
        
        chord_pcs = [n%12 for n in curr_chord]
        candidates = [n for n in full_scale if (n%12) in chord_pcs]
        candidates = [n for n in candidates if abs(n - last_note) <= 9]
        if not candidates: candidates = [last_note]
        
        if dur < 1.0 and random.random() < 0.3:
            pass_cands = [n for n in full_scale if abs(n - last_note) <= 4]
            note = random.choice(pass_cands) if pass_cands else last_note
        else:
            note = random.choice(candidates)
            
        melody_events.append({"note": note, "duration": dur})
        last_note = note
        current_time += dur
        
    return melody_events

# ==========================================
# 3. AUDIO ENGINE
# ==========================================

def apply_swing(time, amount):
    if amount > 0 and (time % 1.0) >= 0.5: return time + amount
    return time

def create_final_midi(structure, melody, instr_name, active_tracks, bpm):
    midi = MIDIFile(5)
    style = structure[0]["style"]
    conf = GROOVE_CONFIG[style]
    swing = conf["swing"]
    
    midi.addTempo(0, 0, bpm)
    
    # 0. MELODI
    if "Melodi" in active_tracks:
        midi.addProgramChange(0, 0, 0, INSTRUMENTS[instr_name])
        t = 0
        for ev in melody:
            real_t = apply_swing(t, swing)
            vel = 110 + random.randint(-5, 5)
            midi.addNote(0, 0, ev["note"], real_t, ev["duration"], vel)
            t += ev["duration"]

    # 1. CHORD
    if "Chord" in active_tracks:
        c_inst = 4 if style == "Jazz" else 0
        if style == "Ballad": c_inst = 24
        if style == "Orchestra": c_inst = 48
        midi.addProgramChange(1, 1, 0, c_inst)
        
        for bar in structure:
            start_t = bar["bar_index"] * 4
            notes = bar["chord_notes"]
            
            if conf["comping"] == "Arpeggio":
                offsets = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
                arp = [notes[0], notes[1], notes[2], notes[1]] * 2
                for i, off in enumerate(offsets):
                    if i < len(arp): midi.addNote(1, 1, arp[i], start_t+off, 0.5, 70)
            elif conf["comping"] == "Syncopated":
                t1 = apply_swing(start_t + 1, swing)
                t2 = apply_swing(start_t + 2.5, swing)
                for n in notes:
                    midi.addNote(1, 1, n, t1, 0.5, 75)
                    midi.addNote(1, 1, n, t2, 0.5, 70)
            else:
                delay = conf["strum"]
                for i, n in enumerate(notes):
                    midi.addNote(1, 1, n, start_t + (i*delay), 4, 75)

    # 2. BASS
    if "Bass" in active_tracks:
        midi.addProgramChange(2, 2, 0, 33)
        for bar in structure:
            start_t = bar["bar_index"] * 4
            root = bar["root_note"] - 12
            if style == "Jazz":
                walk = [root, root+7, root+9, root+7] 
                for i, n in enumerate(walk):
                    midi.addNote(2, 2, n, apply_swing(start_t+i, swing), 1, 95)
            else:
                midi.addNote(2, 2, root, start_t, 2, 95)
                midi.addNote(2, 2, root, start_t+2.5, 0.5, 95)

    # 3. DRUM
    if "Drum" in active_tracks:
        pat_name = conf["drum"]
        pattern = DRUM_PATTERNS.get(pat_name, DRUM_PATTERNS["Standard"])
        for i in range(len(structure)):
            start_t = i * 4
            for s in range(16):
                code = pattern[s]
                if code == 0: continue
                real_t = apply_swing(start_t + (s*0.25), swing)
                note = 36
                if code == 2: note = 38
                if code == 3: note = 42
                if code == 4: note = 51
                midi.addNote(3, 9, note, real_t, 0.25, 100)

    # 4. STRINGS/PAD
    if "Strings/Pad" in active_tracks and style != "Jazz":
        midi.addProgramChange(4, 4, 0, 48)
        for bar in structure:
            start_t = bar["bar_index"] * 4
            pad_notes = [bar["root_note"], bar["chord_notes"][-1]]
            for n in pad_notes:
                midi.addNote(4, 4, n, start_t, 4, 55)
                
    total_duration_beats = len(structure) * 4
    midi.addNote(0, 0, 0, total_duration_beats, 0.1, 0)
    
    midi_data = BytesIO()
    midi.writeFile(midi_data)
    return midi_data.getvalue()

# --- FUNGSI RENDER AUDIO ---
# --- FUNGSI RENDER AUDIO (FIXED DTYPE CASTING) ---
def render_audio(midi_bytes, bpm, bars):
    
    # 1. SETUP PATH SOUNDFONT
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    
    sf_candidates = [
        os.path.join(root_dir, "soundfont.sf2"),
        "soundfont.sf2",
        "../soundfont.sf2"
    ]
    
    sf_path = None
    for p in sf_candidates:
        if os.path.exists(p):
            sf_path = os.path.abspath(p)
            break
            
    if not sf_path:
        st.warning("⚠️ SoundFont tidak ditemukan. Sedang download...")
        try:
            url = "https://github.com/freepats/GeneralUser-GS/raw/master/GeneralUser_GS_1.471/GeneralUser_GS_1.471.sf2"
            r = requests.get(url)
            save_path = os.path.join(root_dir, "soundfont.sf2")
            with open(save_path, "wb") as f:
                f.write(r.content)
            sf_path = save_path
            st.success("✅ SoundFont berhasil didownload!")
        except Exception as e:
            return None, f"Gagal download SoundFont: {e}"

    # 2. GUNAKAN FOLDER TEMP SYSTEM
    temp_dir = tempfile.gettempdir()
    unique_id = str(uuid.uuid4())
    
    temp_midi_path = os.path.join(temp_dir, f"ai_music_{unique_id}.mid")
    temp_wav_path = os.path.join(temp_dir, f"ai_music_{unique_id}.wav")

    try:
        # 3. TULIS FILE MIDI
        with open(temp_midi_path, "wb") as f:
            f.write(midi_bytes)
            
        # 4. CEK FLUIDSYNTH
        if os.name == 'nt': 
            try:
                subprocess.run(["fluidsynth", "--version"], check=True, stdout=subprocess.DEVNULL)
            except:
                return None, "FluidSynth tidak terinstall di Environment Variable."

        # 5. JALANKAN COMMAND
        # Urutan Benar: fluidsynth -ni -F output.wav -r 44100 soundfont.sf2 input.mid
        cmd = [
            "fluidsynth", 
            "-ni", 
            "-F", temp_wav_path,
            "-r", "44100",
            sf_path,
            temp_midi_path
        ]
        
        result = subprocess.run(
            cmd, 
            check=False, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 6. CEK HASIL
        if not os.path.exists(temp_wav_path):
            error_log = result.stderr if result.stderr else result.stdout
            return None, f"FluidSynth Gagal Render:\n{error_log}"

        # 7. TRIMMING LOGIC (DENGAN FIX CASTING)
        total_beats = bars * 4
        expected_sec = total_beats / (bpm / 60)
        target_samples = int((expected_sec + 0.1) * 44100) 
        
        sample_rate, audio_data = wavfile.read(temp_wav_path)
        
        if len(audio_data) > target_samples:
            trimmed = audio_data[:target_samples]
            
            # FADE OUT
            fade_len = int(0.2 * sample_rate)
            if len(trimmed) > fade_len:
                fade_curve = np.linspace(1.0, 0.0, fade_len)
                
                # --- PERBAIKAN DI SINI (ASTYPE INT16) ---
                if len(trimmed.shape) == 2: # Stereo
                    # Kalikan lalu ubah paksa jadi int16
                    trimmed[-fade_len:, 0] = (trimmed[-fade_len:, 0] * fade_curve).astype(np.int16)
                    trimmed[-fade_len:, 1] = (trimmed[-fade_len:, 1] * fade_curve).astype(np.int16)
                else: # Mono
                    trimmed[-fade_len:] = (trimmed[-fade_len:] * fade_curve).astype(np.int16)
            
            buf = BytesIO()
            wavfile.write(buf, sample_rate, trimmed.astype(np.int16))
            final_data = buf.getvalue()
        else:
            with open(temp_wav_path, "rb") as f:
                final_data = f.read()
        
        # 8. BERSIH-BERSIH
        try:
            if os.path.exists(temp_midi_path): os.remove(temp_midi_path)
            if os.path.exists(temp_wav_path): os.remove(temp_wav_path)
        except: pass
        
        return final_data, None
        
    except Exception as e:
        return None, f"System Error: {e}"

# ==========================================
# 3. WEB UI 
# ==========================================

# -- CSS CUSTOM --
st.markdown("""
<style>
    /* BASIC SETUP */
    [data-testid="stHeaderActionElements"] { display: none !important; }
    .block-container { padding-top: 2rem; }
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap');
    .stApp { background-color: #E8E8E5; }
    h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #000; }
    p, div, label { font-family: 'Lato', sans-serif; color: #333; }

    /* VINYL SVG CONTAINER */
    .vinyl-wrapper {
        position: relative;
        width: 300px;
        height: 300px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* ANIMASI SPIN */
    @keyframes spin { 
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); } 
    }
    
    .spinning {
        animation: spin 8s linear infinite;
    }

    /* TONEARM (JARUM) */
    .tonearm {
        position: absolute;
        top: -30px;
        right: -30px;
        width: 140px;
        height: 12px;
        background: silver;
        transform-origin: 80% 20%;
        z-index: 10;
        border-radius: 5px;
        box-shadow: 2px 5px 10px rgba(0,0,0,0.4);
        transition: transform 1s ease-in-out;
    }
    .tonearm.idle { transform: rotate(20deg); }
    .tonearm.playing { transform: rotate(-35deg); }

    .tonearm::after {
        content: '';
        position: absolute;
        left: 0; top: 2px;
        width: 25px; height: 18px;
        background: #333;
        transform: rotate(-15deg);
        border-radius: 2px;
    }

    /* TOMBOL GENERATE */
    .stButton > button {
        width: 100%;
        border: 1px solid #000;
        background-color: transparent;
        padding: 12px;
        font-family: 'Playfair Display', serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
        color: #000 !important;
        border-radius: 0px;
    }
    /* Efek Hover */
    .stButton > button:hover {
        background-color: #000 !important;
        border-color: #000 !important;
        color: #fff !important; /* Paksa putih saat hover */
    }
    .stButton > button:hover p {
        color: #fff !important;
    }
    [data-testid="stButton"] button[kind="primary"] {
        background-color: #000000 !important; /* Hitam pekat */
        border: 2px solid #000000 !important;
        color: #ffffff !important;
        transition: all 0.3s ease; /* Animasi transisi halus */
    }
    [data-testid="stButton"] button[kind="primary"]:hover {
        background-color: #333333 !important; /* Jadi abu-abu gelap */
        border-color: #333333 !important;
        transform: translateY(-2px); /* Efek tombol naik sedikit */
        box-shadow: 0 5px 15px rgba(0,0,0,0.3); /* Ada bayangan */
    }
    [data-testid="stButton"] button[kind="primary"]:disabled {
        background-color: #cccccc !important;
        border-color: #cccccc !important;
        color: #888888 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
        opacity: 0.7;
    }
    [data-testid="stButton"] button[kind="primary"]:disabled:hover {
        background-color: #cccccc !important;
        color: #888888 !important;
    }
    
    /* Tombol Pilihan Mood */
    [data-testid="stButton"] button[kind="secondary"] {
        border: 1px solid #ccc;
        color: #000;
        background: transparent;
    }
    [data-testid="stButton"] button[kind="primary"] {
        background: #000 !important;
        border: 1px solid #000 !important;
        color: #fff !important; /* Paksa putih saat dipilih */
        font-weight: bold;
    }
    /* Memastikan teks pada tombol Primary ikut putih */
    [data-testid="stButton"] button[kind="primary"] p {
        color: #fff !important;
    }
    
    /* --- 2. TOMBOL DOWNLOAD --- */
    /* Target khusus tombol download (.stDownloadButton) */
    .stDownloadButton > button {
        background-color: #000 !important; /* Background Hitam */
        border: 2px solid #000 !important;
        color: #fff !important; /* Teks Putih (Sesuai Request) */
        border-radius: 0px;
        font-weight: bold;
        transition: 0.3s;
    }
    /* Memastikan elemen teks (p) di dalamnya juga putih */
    .stDownloadButton > button p {
        color: #fff !important;
    }
    /* State Hover Download: Jadi transparan dengan teks hitam (Efek kebalikan) */
    .stDownloadButton > button:hover {
        background-color: transparent !important;
        color: #000 !important;
    }
    .stDownloadButton > button:hover p {
        color: #000 !important;
    }
    
    /* --- PERBAIKAN WARNA TEKS ADVANCED MODE --- */
    /* Mengubah warna nilai yang DIPILIH di dalam kotak menjadi Putih */
    .stSelectbox div[data-baseweb="select"] div {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .stSelectbox svg {
        fill: #ffffff !important;
    }
    div[data-baseweb="popover"] ul {
        background-color: #262730 !important;
    }
    div[data-baseweb="popover"] li div, 
    div[data-baseweb="popover"] li span {
        color: #ffffff !important;
    }
    /* Warna saat mouse diarahkan ke opsi (Hover) di dropdown */
    div[data-baseweb="popover"] li:hover {
        background-color: #444444 !important;
    }
    
    /* --- CUSTOM TOOLTIP (HELP) --- */
    /* 1. Ikon Tanda Tanya (?) */
    /* Membuat latar belakang lingkaran hitam di belakang ikon */
    [data-testid="stTooltipIcon"] {
        background-color: #000000 !important;
        border-radius: 50%;
        width: 18px;
        height: 18px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    /* Mengubah warna tanda tanyanya jadi Putih */
    [data-testid="stTooltipIcon"] svg {
        fill: #000000 !important;
        width: 12px !important;
        height: 12px !important;
    }
    /* 2. Kotak Penjelasan (Popup) */
    /* Mengubah background kotak menjadi Hitam Pekat */
    div[data-baseweb="tooltip"],
    div[data-baseweb="tooltip"] > div {
        background-color: #000000 !important;
        border-radius: 6px;
        border: 1px solid #333;
    }
    /* Mengubah SEMUA teks di dalam tooltip menjadi Putih */
    div[data-baseweb="tooltip"] * {
        color: #ffffff !important;
    }
    
    /* --- CUSTOM EXPANDER (FIXED COLOR) --- */
    /* 1. Container Utama */
    details {
        background-color: transparent !important;
        border: 1px solid #444 !important;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    /* 2. Bagian Judul (Summary) - KONDISI NORMAL */
    summary {
        background-color: transparent !important; /* Hitam */
        color: #ffffff !important;             /* Putih */
        font-family: 'Lato', sans-serif !important;
        font-weight: bold;
        padding: 10px !important;
        border-radius: 5px;
    }
    /* 3. KONDISI TERBUKA ([open]) - Paksa Tetap Hitam */
    details[open] > summary {
        background-color: transparent !important;
        color: #ffffff !important;
    }
    /* 4. KONDISI FOKUS/KLIK (:focus) - Hapus Outline Biru & Paksa Hitam */
    summary:focus, summary:active {
        background-color: transparent !important;
        color: #ffffff !important;
        outline: none !important;     /* Hapus garis biru bawaan browser */
        box-shadow: none !important;  /* Hapus efek bayangan fokus */
    }
    /* 5. KONDISI HOVER (Mouse di atasnya) - Ubah dikit biar interaktif */
    summary:hover {
        background-color: #D3D3D3 !important; /* Abu sangat gelap (sedikit beda) */
        color: #dddddd !important;
    }
    /* 6. Ikon Panah */
    summary svg {
        fill: #000000 !important;
    }
    /* 7. Isi Konten */
    details > div {
        background-color: transparent !important;
        color: #dddddd !important;
        padding: 15px;
        border-top: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<h1 style="font-size: 3rem; margin-bottom: 10px;">Generator</h1>', unsafe_allow_html=True)
st.markdown('<div style="height: 2px; background: #000; width: 50px; margin-bottom: 40px;"></div>', unsafe_allow_html=True)

# TABS
tab1, tab2, tab3 = st.tabs(["Simple Mode", "Advanced Mode", "History"])

# --- TAB 1: PLAYER MODE ---
with tab1:
    c_left, c_center, c_right = st.columns([1, 1.3, 1], gap="large")
    
    # --- LOGIKA TOMBOL TOGGLE (DESELECT) ---
    def set_mood(selected_mood_name):
        if st.session_state['current_mood'] == selected_mood_name:
            st.session_state['current_mood'] = None
            st.session_state['is_generated'] = False
        else:
            st.session_state['current_mood'] = selected_mood_name
            st.session_state['is_generated'] = False

    # --- KOLOM 1: MOOD LIST ---
    with c_left:
        st.markdown("#### SELECT MOOD")
        st.caption("Klik untuk memilih, klik lagi untuk batal.")
        
        for mood_key in MOOD_PRESETS.keys():
            btn_type = "primary" if st.session_state['current_mood'] == mood_key else "secondary"
            if st.button(mood_key, key=f"btn_{mood_key}", type=btn_type, use_container_width=True):
                set_mood(mood_key)
                st.rerun()

        st.write("")
        dur_sim = st.slider("Duration (Bars)", 4, 32, 8, step=4)

    # --- KOLOM 2: VINYL ---
    with c_center:
        current_mood = st.session_state['current_mood']
        is_active = (current_mood is not None)
        
        if is_active:
            p = MOOD_PRESETS[current_mood]
            accent_color = p.get("color", "#000")
            tonearm_class = "playing" 
            spin_class = "spinning"
        else:
            accent_color = "#333"
            tonearm_class = "idle"
            spin_class = ""
            p = None

        # SVG FIXED (NO INDENTATION ISSUE)
        st.markdown(f'''
        <div class="vinyl-wrapper" style="margin-top: 20px; margin-bottom: 30px;">
            <div class="tonearm {tonearm_class}"></div>
            <svg viewBox="0 0 200 200" class="{spin_class}" style="width:100%; height:100%;">
                <circle cx="100" cy="100" r="98" fill="#111" />
                <circle cx="100" cy="100" r="95" fill="none" stroke="#222" stroke-width="2" />
                <circle cx="100" cy="100" r="85" fill="none" stroke="#1a1a1a" stroke-width="4" />
                <circle cx="100" cy="100" r="70" fill="none" stroke="#222" stroke-width="2" />
                <circle cx="100" cy="100" r="55" fill="none" stroke="#1a1a1a" stroke-width="3" />
                <circle cx="100" cy="100" r="35" fill="{accent_color}" />
                <text x="100" y="95" text-anchor="middle" fill="white" font-family="sans-serif" font-size="8" font-weight="bold">KELOMPOK 5</text>
                <text x="100" y="110" text-anchor="middle" fill="white" font-family="sans-serif" font-size="8">RECORDS</text>
                <circle cx="100" cy="100" r="3" fill="#eee" />
            </svg>
        </div>
        ''', unsafe_allow_html=True)
        
        # Tombol Generate
        if st.button("GENERATE TRACK", type="primary", disabled=not is_active, use_container_width=True):
            if is_active:
                with st.spinner("Composing..."):
                    struct_song = generate_structure("C", p["scale"], p["prog"], dur_sim, p["style"])
                    melody_song = generate_melody(struct_song, dur_sim, p["scale"])
                    midi_bytes = create_final_midi(struct_song, melody_song, p["instr"], p["tracks"], p["bpm"])
                    wav_data, err = render_audio(midi_bytes, p["bpm"], dur_sim)
                    
                    if err:
                        st.error(err)
                    else:
                        st.success("Track Ready!")
                        st.session_state['last_wav'] = wav_data
                        st.session_state['last_midi'] = midi_bytes
                        st.session_state['is_generated'] = True
                        
                        ts = datetime.now().strftime("%H:%M")
                        entry = {"time": ts, "name": current_mood, "midi": midi_bytes, "wav": wav_data, "info": f"{p['style']}"}
                        st.session_state['history'].insert(0, entry)
                        st.rerun()

        # PLAYER & DOWNLOAD BUTTONS (CENTER)
        if st.session_state['is_generated'] and 'last_wav' in st.session_state:
            # Layout: Audio kiri (besar), Tombol Download kanan (kecil)
            st.audio(st.session_state['last_wav'], format='audio/wav')
            col_dl_wav, col_dl_mid = st.columns([2, 2], gap="small")
            with col_dl_wav:
                st.download_button("⬇ WAV", st.session_state['last_wav'], "song.wav", "audio/wav", use_container_width=True)
            with col_dl_mid:
                st.download_button("⬇ MIDI", st.session_state['last_midi'], "song.mid", "audio/midi", use_container_width=True)
                st.toast("Track saved to History!", icon="💾")
                
    # --- KOLOM 3: INFO DESCRIPTION ---
    with c_right:
        if not is_active:
             st.markdown("""
            <div style="text-align: center; color: #999; margin-top: 50px;">
                <h3>Select a Mood</h3>
                <p>Silakan pilih mood.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="text-align: left; padding-top: 20px;">
                <h1 style="font-size: 3.5rem; line-height: 1; margin-bottom: 10px; color: #000;">
                    {current_mood.split('(')[0]}
                </h1>
                <div style="font-family: 'Lato'; text-transform: uppercase; letter-spacing: 2px; color: {accent_color}; font-weight: bold; margin-bottom: 20px;">
                    {p['style'].upper()} • {p['bpm']} BPM
                </div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: #444; border-left: 3px solid {accent_color}; padding-left: 15px;">
                    {p['desc']}
                </p>
                <br>
                <div style="font-size: 0.9rem; color: #666;">
                    <b>Featured Instrument:</b><br>
                    {p['instr']}
                </div>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    def validate_bpm():
        if st.session_state.adv_bpm_val < 40:
            st.session_state.adv_bpm_val = 40
        elif st.session_state.adv_bpm_val > 240:
            st.session_state.adv_bpm_val = 240
        
    st.markdown("### Advanced Configuration")
    cc1, cc2 = st.columns(2)
    if 'adv_bpm_val' not in st.session_state:
        st.session_state.adv_bpm_val = 120
    with cc1:
        adv_key = st.selectbox(
            "Key", 
            list(KEYS.keys()), 
            help="Nada dasar lagu (Root Note). C adalah standar umum."
        )
        adv_scale = st.selectbox(
            "Scale", 
            list(SCALE_INTERVALS.keys()), 
            help="Tangga nada yang menentukan nuansa."
        )
        adv_prog = st.selectbox(
            "Progression", 
            list(PROGRESSIONS.keys()), 
            help="Urutan pergerakan chord (Progresi) yang menjadi kerangka lagu."
        )
    with cc2:
        adv_style = st.selectbox(
            "Style", 
            list(GROOVE_CONFIG.keys()), 
            help="Gaya permainan instrumen (Pola iringan dan drum)."
        )
        adv_instr = st.selectbox(
            "Instrument", 
            list(INSTRUMENTS.keys()), 
            help="Instrumen utama yang memainkan melodi."
        )
        adv_bpm = st.number_input(
            "BPM (Beats Per Minute)", 
            min_value=-2000000000, 
            max_value=2000000000,
            key="adv_bpm_val",            # Terhubung ke session_state
            on_change=validate_bpm,       # Panggil validasi saat berubah
            help="Kecepatan lagu (40-240). Nilai otomatis disesuaikan jika diluar batas."
        )
    
    adv_bars = st.slider(
        "Length (Bars)", 
        4, 32, 8, step=4, key="adv_b",
        help="Durasi lagu dalam jumlah bar (1 Bar = 4 ketukan)."
    )
    
    adv_tracks = st.multiselect(
        "Layers", 
        ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"], 
        default=["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        help="Pilih elemen instrumen yang ingin dimasukkan ke dalam lagu."
    )
    
    if st.button("Compose Custom Track", type="primary"):
        final_bpm = st.session_state.adv_bpm_val

        with st.spinner("Composing..."):
            struct = generate_structure(adv_key, adv_scale, adv_prog, adv_bars, adv_style)
            melody = generate_melody(struct, adv_bars, adv_scale)
            midi_b = create_final_midi(struct, melody, adv_instr, adv_tracks, final_bpm)
            wav_b, err_b = render_audio(midi_b, final_bpm, adv_bars)
            if err_b: st.error(err_b)
            else:
                # --- MULAI PERBAIKAN: SIMPAN KE HISTORY ---
                ts = datetime.now().strftime("%H:%M")
                # Memberi nama khusus untuk custom track
                custom_name = f"Custom ({adv_style} - {adv_key})"
                entry_id = str(uuid.uuid4())
                full_details = {
                    "Scale": adv_scale,
                    "Progression": adv_prog,
                    "Instrument": adv_instr,
                    "BPM": final_bpm,
                    "Length": f"{adv_bars} Bars",
                    "Active Tracks": ", ".join(adv_tracks)
                }
                
                entry = {
                    "id": entry_id,
                    "time": ts, 
                    "name": custom_name, 
                    "midi": midi_b, 
                    "wav": wav_b, 
                    "info": f"{final_bpm} BPM",
                    "details": full_details
                }
                
                # Masukkan ke awal list history
                st.session_state['history'].insert(0, entry)
                
                col_1, col_2, col_3 = st.columns([3, 1, 5])
                with col_1:
                    st.audio(wav_b, format='audio/wav')
                with col_2:
                    st.download_button("Download WAV", wav_b, "custom.wav", "audio/wav")
                with col_3:
                    st.download_button("Download MIDI", midi_b, "custom.mid", "audio/midi")
                    st.toast("Track saved to History!", icon="💾")
                    

with tab3:
    st.markdown("### Session History")
    
    if not st.session_state['history']:
        st.info("Belum ada riwayat lagu.")
        
    for i, item in enumerate(st.session_state['history']):
        with st.container():
            c1, c2, c3 = st.columns([0.5, 2, 3]) 
            with c1: 
                st.caption(item['time'])
            with c2: 
                st.write(f"**{item['name']}**")
                if 'info' in item:
                    st.caption(item['info'])
            with c3:
                st.audio(item['wav'], format='audio/wav')

            c_det, c_btn = st.columns([3, 2])
            
            with c_det:
                if 'details' in item and item['details']:
                    short_id = item['id'][:8]
                    expander_label = f"Lihat Detail (ID: {short_id})"
                    with st.expander(expander_label):
                        for k, v in item['details'].items():
                            st.markdown(f"**{k}:** {v}")
                else:
                    st.caption("Dibuat menggunakan Simple Mode")

            with c_btn:
                b1, b2 = st.columns(2)
                with b1: st.download_button("WAV", item['wav'], f"h_{i}.wav", key=f"dlw_{i}", use_container_width=True)
                with b2: st.download_button("MIDI", item['midi'], f"h_{i}.mid", key=f"dlm_{i}", use_container_width=True)
            
            st.divider()

# Footer
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem; margin-top: 50px; border-top: 1px solid #ccc; padding-top: 20px;">
    © 2025 Kelompok 5 • Informatics Engineering
</div>
""", unsafe_allow_html=True)
