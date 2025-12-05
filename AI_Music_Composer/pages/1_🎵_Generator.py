import streamlit as st
import random
import numpy as np
from scipy.io.wavfile import write
from midiutil import MIDIFile
from io import BytesIO

st.set_page_config(page_title="Generator Musik", page_icon="🎵", layout="wide")

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
    "😊 Ceria (Happy)": {
        "scale": "Major", "prog": "The Golden Loop (I-V-vi-IV)", 
        "bpm": 120, "style": "Pop", "instr": "Grand Piano",
        "tracks": ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        "desc": "Pop ceria dengan tempo cepat."
    },
    "😢 Sedih (Sad)": {
        "scale": "Major", "prog": "Emotional Turn (vi-IV-I-V)", 
        "bpm": 65, "style": "Ballad", "instr": "Grand Piano",
        "tracks": ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        "desc": "Ballad lambat dengan nuansa melankolis."
    },
    "😎 Santai (Jazz)": {
        "scale": "Major", "prog": "Jazz Standard (ii-V-I)", 
        "bpm": 90, "style": "Jazz", "instr": "Electric Piano (Rhodes)",
        "tracks": ["Melodi", "Chord", "Bass", "Drum"], 
        "desc": "Swing feel dengan chord 7th."
    },
    "😨 Tegang (Cinematic)": {
        "scale": "Harmonic Minor", "prog": "Dark Tension (i-ii-vii)", 
        "bpm": 135, "style": "Orchestra", "instr": "Violin",
        "tracks": ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
        "desc": "Nuansa orkestra yang intens dan cepat."
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

    midi_data = BytesIO()
    midi.writeFile(midi_data)
    return midi_data.getvalue()

def generate_preview_wav(melody):
    sample_rate = 44100
    audio_data = []
    for ev in melody:
        freq = 440 * (2 ** ((ev["note"] - 69) / 12))
        dur = ev["duration"] * 0.35 
        t = np.linspace(0, dur, int(sample_rate * dur), False)
        wave = 0.3 * np.sin(2 * np.pi * freq * t) * np.exp(-4 * t)
        audio_data.append(wave)
    return np.int16(np.concatenate(audio_data) * 32767)

# ==========================================
# 4. WEB UI
# ==========================================
st.title("🎵 AI Music Composer")

# HANYA 2 TAB (Simple & Advanced)
tab1, tab2 = st.tabs(["🚀 Simple Mode", "🛠️ Advanced Mode"])

# --- TAB 1: SIMPLE ---
with tab1:
    st.subheader("Pilih Mood & Durasi Lagu")
    c1, c2 = st.columns(2)
    with c1:
        preset_name = st.radio("Mood:", list(MOOD_PRESETS.keys()))
        dur_sim = st.slider("Durasi Lagu (Bar):", 4, 16, 8, key="d1")
    with c2:
        p = MOOD_PRESETS[preset_name]
        st.success(f"**Instrumen:** {p['instr']}")
        st.info(f"**Deskripsi:** {p['desc']}")
        
    if st.button("✨ Ciptakan Musik (Instan)", type="primary"):
        p = MOOD_PRESETS[preset_name]
        struct_song = generate_structure("C", p["scale"], p["prog"], dur_sim, p["style"])
        melody_song = generate_melody(struct_song, dur_sim, p["scale"])
        
        midi_bytes = create_final_midi(struct_song, melody_song, p["instr"], p["tracks"], p["bpm"])
        
        wav_buf = BytesIO()
        write(wav_buf, 44100, generate_preview_wav(melody_song))
        wav_buf.seek(0)
        st.audio(wav_buf, format='audio/wav')
        st.download_button("Download MIDI", midi_bytes, f"ai_{p['style']}.mid", "audio/midi")

# --- TAB 2: ADVANCED ---
with tab2:
    st.subheader("Konfigurasi Manual")
    st.write("Di mode ini, kamu bebas mencampur-adukkan teori musik.")
    
    # --- EXPANDER PANDUAN (SOLUSI REQUEST KAMU) ---
    with st.expander("Panduan Konfigurasi Manual"):
        st.markdown("""
        **1. Scale (Bahan Baku Nada)**
        - **Major:** Ceria, tegas (Pop/Rock).
        - **Minor:** Sedih, emosional.
        - **Dorian:** Elegan, sedikit miring (Jazz).
        - **Blues:** Keren, maskulin (Rock).

        **2. Progression (Alur Chord)**
        - **The Golden Loop (I-V-vi-IV):** Rumus lagu Pop paling hits sedunia.
        - **Emotional Turn (vi-IV-I-V):** Rumus lagu galau modern.
        - **Jazz Standard (ii-V-I):** Rumus wajib Jazz (Circle of Fifths).
        - **Dark Tension (i-ii-vii):** Menciptakan rasa takut/gelisah.
        
        **3. Style (Gaya Main)**
        - **Pop:** Bass lurus, chord panjang (Block), drum standar.
        - **Ballad:** Bass jarang, chord dipetik (Arpeggio), drum lembut.
        - **Jazz:** Bass jalan (Walking), chord putus-putus (Syncopated), drum Swing.
        - **Orchestra:** Fokus pada Strings section.
        """)

    # INPUT FIELD
    cc1, cc2 = st.columns(2)
    with cc1:
        adv_key = st.selectbox("Key (Nada Dasar):", list(KEYS.keys()), help="Nada awal lagu dimulai")
        adv_scale = st.selectbox("Scale (Bahan Nada):", list(SCALE_INTERVALS.keys()), help="Menentukan nuansa nada lagu")
        adv_prog = st.selectbox("Chord Formula:", list(PROGRESSIONS.keys()), help="Urutan chord progression")
    with cc2:
        adv_style = st.selectbox("Style (Gaya Main):", list(GROOVE_CONFIG.keys()), help="Menentukan pola Drum dan Bass")
        adv_instr = st.selectbox("Instrumen Melodi:", list(INSTRUMENTS.keys()), help="Pilih suara instrumen melodi")
        adv_bpm = st.number_input("Tempo (BPM):", 60, 180, 120, help="Kecepatan lagu")
        
    adv_tracks = st.multiselect("Active Tracks:", ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"], 
                        default=["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"])
    
    if st.button("🛠️ Generate Custom"):
        struct_song = generate_structure(adv_key, adv_scale, adv_prog, 8, adv_style)
        melody_song = generate_melody(struct_song, 8, adv_scale)
        midi_custom = create_final_midi(struct_song, melody_song, adv_instr, adv_tracks, adv_bpm)
        
        wb = BytesIO()
        write(wb, 44100, generate_preview_wav(melody_song))
        wb.seek(0)
        st.audio(wb, format='audio/wav')
        st.download_button("Download Custom MIDI", midi_custom, "custom.mid", "audio/midi")