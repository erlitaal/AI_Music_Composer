import streamlit as st
import random
import numpy as np
import os
import requests
import tempfile
import subprocess
import uuid
from midiutil import MIDIFile
from io import BytesIO
from datetime import datetime
from midi2audio import FluidSynth
from scipy.io import wavfile

st.set_page_config(page_title="Generator Musik", page_icon="🎵", layout="wide")

if 'history' not in st.session_state:
    st.session_state['history'] = []
    
st.markdown("""
<style>
    /* HILANGKAN IKON RANTAI DI HEADER */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)
    
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
# 4. WEB UI
# ==========================================
st.title("🎵 AI Music Composer")

# HANYA 2 TAB (Simple & Advanced)
tab1, tab2, tab3 = st.tabs(["🚀 Simple Mode", "🛠️ Advanced Mode", "📜 Riwayat Sesi"])

# --- FUNGSI SAVE HISTORY ---
def save_to_history(name, midi_data, wav_data, info):
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = {
        "time": timestamp,
        "name": name,
        "midi": midi_data,
        "wav": wav_data,
        "info": info
    }
    st.session_state['history'].insert(0, entry)

# --- TAB 1: SIMPLE ---
with tab1:
    st.subheader("Pilih Mood & Durasi Lagu")
    c1, c2 = st.columns(2)
    with c1:
        preset_name = st.radio("Mood:", list(MOOD_PRESETS.keys()))
        dur_sim = st.slider("Durasi Lagu (Bar):", 4, 32, 8, step=4, key="d1")
    with c2:
        p = MOOD_PRESETS[preset_name]
        st.success(f"**Instrumen:** {p['instr']}")
        st.info(f"**Deskripsi:** {p['desc']}")
        
    if st.button("✨ Ciptakan Musik (Instan)", type="primary"):
        p = MOOD_PRESETS[preset_name]
        struct_song = generate_structure("C", p["scale"], p["prog"], dur_sim, p["style"])
        melody_song = generate_melody(struct_song, dur_sim, p["scale"])
        
        midi_bytes = create_final_midi(struct_song, melody_song, p["instr"], p["tracks"], p["bpm"])
        
        wav_data, err = render_audio(midi_bytes, p["bpm"], dur_sim)
        if err:
            st.error(err)
        else:
            st.audio(wav_data, format='audio/wav')
                
            col_d1, col_d2, col_d3 = st.columns([1, 1, 5], gap="small")
            with col_d1:
                st.download_button("💾 Download WAV", wav_data, f"ai_{p['style']}.wav", "audio/wav")
            with col_d2:
                st.download_button("🎹 Download MIDI", midi_bytes, f"ai_{p['style']}.mid", "audio/midi")
                
            save_to_history(f"{preset_name}", midi_bytes, wav_data, f"C Major - {p['style']}")
            st.toast("✅ Lagu berhasil disimpan!")
        
# --- TAB 2: ADVANCED ---
with tab2:
    st.subheader("Konfigurasi Manual")
    st.write("Di mode ini, kamu bebas mencampuradukkan teori musik.")
    
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
        - **Canon Walk (I-V-vi-iii):** Menciptakan rasa klasik, anggun, dan sentimental.
        
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

    adv_bars = st.slider("Durasi lagu (Bar):", 4, 32, 8, step=4, key="adv_bars", help="Panjang lagu")
    
    adv_tracks = st.multiselect("Active Tracks:", ["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"], 
                        default=["Melodi", "Chord", "Bass", "Drum", "Strings/Pad"],
                        help="Pilih Track (Layer) mana saja yang ingin dimasukkan ke dalam file MIDI.")
    
    if st.button("🛠️ Generate Custom"):
        struct_song = generate_structure(adv_key, adv_scale, adv_prog, adv_bars, adv_style)
        melody_song = generate_melody(struct_song, adv_bars, adv_scale)
        midi_custom = create_final_midi(struct_song, melody_song, adv_instr, adv_tracks, adv_bpm)
        
        wav_custom, err_custom = render_audio(midi_custom, adv_bpm, adv_bars)
        
        if err_custom:
            st.error(err_custom)
        else:
            st.audio(wav_custom, format='audio/wav')
                
            col_c1, col_c2, col_3 = st.columns([1, 1, 5], gap="small")
            with col_c1:
                st.download_button("💾 Download WAV", wav_custom, "custom.wav", "audio/wav")
            with col_c2:
                st.download_button("🎹 Download MIDI", midi_custom, "custom.mid", "audio/midi")
            
            save_to_history(f"Custom {adv_style}", midi_custom, wav_custom, f"{adv_key} {adv_scale}")
            st.toast("✅ Lagu berhasil disimpan!")

# --- TAB 3: HISTORY ---
with tab3:
    st.header("📜 Riwayat Sesi Ini")
    st.caption("Daftar lagu yang sudah kamu buat selama sesi ini. (Hilang jika browser di-refresh)")
    
    if len(st.session_state['history']) == 0:
        st.info("Belum ada riwayat. Buat lagu dulu yuk!")
    else:
        for i, item in enumerate(st.session_state['history']):
            with st.container():
                c1, c2, c3 = st.columns([1, 3, 1])
                with c1:
                    st.write(f"**#{len(st.session_state['history'])-i}**")
                    st.caption(item['time'])
                with c2:
                    st.write(f"**{item['name']}**")
                    st.caption(item['info'])
                    if item['wav']:
                        st.audio(item['wav'], format='audio/wav')
                    else:
                        st.warning("Audio Error")
                with c3:
                    st.write("")
                    if item['wav']:
                        st.download_button("💾 Download WAV", item['wav'], f"hist_{i}.wav", "audio/wav", key=f"dww_{i}")
                    st.download_button("🎹 Download MIDI", item['midi'], f"hist_{i}.mid", "audio/midi", key=f"dwm_{i}")
                st.divider()
