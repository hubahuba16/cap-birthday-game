import streamlit as st
import random
import time
import base64
import streamlit.components.v1 as components

# --- 1. WEBPAGE SETUP ---
st.set_page_config(page_title="S.H.I.E.L.D. Terminal", page_icon="🛡️", layout="centered")

# --- 2. VIDEO BACKGROUND & PREMIUM CINEMATIC CSS ---
@st.cache_data
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

video_base64 = get_base64_of_bin_file("marvel_intro.mp4")

if video_base64:
    bg_css = f"""
    <style>
    /* Import authentic Marvel poster fonts and High-Tech HUD fonts */
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@500;700&display=swap');

    .stApp {{ background: transparent !important; }}
    
    html, body, [class*="css"] {{
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    #my-video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100vw;
        min-height: 100vh;
        z-index: -1;
        opacity: 0.40;
        object-fit: cover;
        pointer-events: none;
    }}
    
    .block-container {{
        position: relative;
        background-color: rgba(10, 15, 25, 0.85); 
        padding: 4rem 3rem;
        border-radius: 20px;
        margin-top: 3rem;
        z-index: 1; 
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.9), inset 0 0 20px rgba(59, 130, 246, 0.2);
        border: 1px solid rgba(59, 130, 246, 0.3);
    }}

    /* CRT Scanline effect overlay */
    .block-container::after {{
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.15) 50%);
        background-size: 100% 4px;
        z-index: 10;
        pointer-events: none;
        border-radius: 20px;
    }}

    .marvel-title {{
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 3.8rem !important;
        letter-spacing: 4px;
        color: #60a5fa !important;
        text-shadow: 0 0 20px rgba(96, 165, 250, 0.6);
        text-align: center;
        margin-bottom: 20px;
        line-height: 1.1;
    }}
    
    .big-question {{
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 3.2rem !important;
        color: #ffffff !important;
        letter-spacing: 2px;
        text-shadow: 0px 4px 15px rgba(0,0,0,0.9);
        line-height: 1.2;
        margin-bottom: 40px;
        text-align: center;
    }}

    .bday-text {{
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 5rem !important;
        color: #fbbf24 !important; 
        text-align: center;
        text-shadow: 0 0 30px rgba(251, 191, 36, 0.8);
        margin: 40px 0;
        line-height: 1.1;
        letter-spacing: 3px;
    }}
    
    .mission-success {{
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 2.2rem !important;
        color: #10b981 !important; 
        text-align: center;
        font-weight: bold;
        letter-spacing: 4px;
        text-shadow: 0 0 15px rgba(16, 185, 129, 0.6);
        text-transform: uppercase;
    }}

    div[role="radiogroup"] {{
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 20px !important; 
        max-width: 800px;
        margin: 0 auto !important; 
        background: transparent !important;
        padding: 0 !important;
    }}
    
    div[role="radiogroup"] > label > div:first-child {{
        display: none !important; 
    }}

    div[role="radiogroup"] > label {{
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(30, 58, 138, 0.6)) !important;
        border: 2px solid rgba(59, 130, 246, 0.5) !important;
        border-radius: 12px !important;
        padding: 20px 15px !important;
        margin: 0 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(8px);
    }}
    
    div[role="radiogroup"] > label:hover {{
        background: rgba(59, 130, 246, 0.5) !important;
        border: 2px solid #60a5fa !important;
        box-shadow: 0 0 25px rgba(96, 165, 250, 0.8) !important;
        transform: translateY(-4px) scale(1.02);
    }}

    .stRadio p {{
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: #f8fafc !important;
        text-align: center !important;
        margin: 0 !important;
        width: 100%;
        letter-spacing: 1px;
    }}

    /* REAL ANIMATED HEALTH BARS */
    .health-container {{
        width: 100%;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 5px 0 25px 0;
        overflow: hidden;
        height: 20px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.8);
    }}
    .health-bar-red {{
        height: 100%;
        background: linear-gradient(90deg, #7f1d1d, #ef4444);
        box-shadow: 0 0 15px #ef4444;
        transition: width 0.5s ease-in-out;
    }}
    .health-bar-blue {{
        height: 100%;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        box-shadow: 0 0 15px #3b82f6;
        transition: width 0.5s ease-in-out;
    }}

    /* PULSING THROW SHIELD BUTTON */
    @keyframes pulseGlow {{
        0% {{ box-shadow: 0 0 15px rgba(59, 130, 246, 0.4); transform: scale(1); }}
        50% {{ box-shadow: 0 0 30px rgba(59, 130, 246, 0.9); transform: scale(1.03); }}
        100% {{ box-shadow: 0 0 15px rgba(59, 130, 246, 0.4); transform: scale(1); }}
    }}
    .stButton > button {{
        animation: pulseGlow 2.5s infinite;
        background: linear-gradient(145deg, #1e3a8a, #2563eb) !important;
        border: 2px solid #60a5fa !important;
        font-family: 'Rajdhani', sans-serif !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        font-weight: 700 !important;
        display: block;
        margin: 30px auto 0 auto !important;
        padding: 15px 50px !important;
        font-size: 1.4rem !important;
        border-radius: 50px !important;
        transition: all 0.2s ease;
        position: relative;
        z-index: 20;
    }}
    .stButton > button:hover {{
        background: linear-gradient(145deg, #2563eb, #3b82f6) !important;
        box-shadow: 0 0 40px rgba(96, 165, 250, 1) !important;
        transform: scale(1.08) !important;
        animation: none;
    }}
    </style>
    
    <video id="my-video" autoplay loop muted playsinline>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    """
    st.markdown(bg_css, unsafe_allow_html=True)
else:
    st.warning("Could not find 'marvel_intro.mp4'. Please ensure it is in the same folder.")

# --- 3. THE QUESTION BANK (67 Questions) ---
all_questions = [
    {"question": "What is Captain America's real name?", "options": ["Steve Rogers", "Tony Stark", "Bruce Banner", "Clint Barton"], "answer": "Steve Rogers", "diff": "Easy"},
    {"question": "What fictional metal is Cap's shield made of?", "options": ["Adamantium", "Vibranium", "Uru", "Titanium"], "answer": "Vibranium", "diff": "Easy"},
    {"question": "Who is Steve Rogers' best friend?", "options": ["Sam Wilson", "Bucky Barnes", "Tony Stark", "Thor"], "answer": "Bucky Barnes", "diff": "Easy"},
    {"question": "What food did the Avengers eat after the Battle of New York?", "options": ["Pizza", "Shawarma", "Burgers", "Tacos"], "answer": "Shawarma", "diff": "Easy"},
    {"question": "What is the name of Thor's hammer?", "options": ["Stormbreaker", "Mjolnir", "Gungnir", "Leviathan"], "answer": "Mjolnir", "diff": "Easy"},
    {"question": "What animal does Scott Lang ride?", "options": ["A flying ant", "A spider", "A beetle", "A wasp"], "answer": "A flying ant", "diff": "Easy"},
    {"question": "What color is the Time Stone?", "options": ["Red", "Blue", "Green", "Yellow"], "answer": "Green", "diff": "Easy"},
    {"question": "Who is the king of Wakanda?", "options": ["M'Baku", "T'Challa", "Killmonger", "N'Jobu"], "answer": "T'Challa", "diff": "Easy"},
    {"question": "What is Spider-Man's aunt's name?", "options": ["Mary", "May", "Martha", "Michelle"], "answer": "May", "diff": "Easy"},
    {"question": "Who said: 'I love you 3000'?", "options": ["Morgan Stark", "Pepper Potts", "Happy Hogan", "Peter Parker"], "answer": "Morgan Stark", "diff": "Easy"},
    {"question": "What is the name of Tony Stark's AI?", "options": ["J.A.R.V.I.S.", "F.R.I.D.A.Y.", "All", "E.D.I.T.H."], "answer": "All", "diff": "Easy"},
    {"question": "Which eye does Nick Fury wear a patch over?", "options": ["Left", "Right", "He doesn't wear one", "Both"], "answer": "Left", "diff": "Easy"},
    {"question": "Who is Peter Quill's alter ego?", "options": ["Star-Lord", "Drax", "Ronan", "Nova"], "answer": "Star-Lord", "diff": "Easy"},
    {"question": "During WWII, what was Cap's rank before becoming a Captain?", "options": ["Private", "Corporal", "Sergeant", "Lieutenant"], "answer": "Private", "diff": "Medium"},
    {"question": "What year was Steve Rogers frozen in ice?", "options": ["1943", "1945", "1947", "1950"], "answer": "1945", "diff": "Medium"},
    {"question": "Where did Steve and Peggy Carter promise to go dancing?", "options": ["The Stork Club", "Copacabana", "Cotton Club", "Rainbow Room"], "answer": "The Stork Club", "diff": "Medium"},
    {"question": "What organization did Peggy Carter help found?", "options": ["S.W.O.R.D.", "S.H.I.E.L.D.", "HYDRA", "A.I.M."], "answer": "S.H.I.E.L.D.", "diff": "Medium"},
    {"question": "What is Natasha Romanoff's alias?", "options": ["Black Cat", "Black Widow", "Scarlet Witch", "Mockingbird"], "answer": "Black Widow", "diff": "Medium"},
    {"question": "Which infinity stone was hidden in the Tesseract?", "options": ["Space Stone", "Mind Stone", "Reality Stone", "Power Stone"], "answer": "Space Stone", "diff": "Medium"},
    {"question": "What is the name of Peter Parker's high school?", "options": ["Midtown High", "Brooklyn Visions", "Queens Academy", "Empire State"], "answer": "Midtown High", "diff": "Medium"},
    {"question": "Who is Wanda Maximoff's twin brother?", "options": ["Pietro", "Tommy", "Billy", "Magneto"], "answer": "Pietro", "diff": "Medium"},
    {"question": "What species is Groot?", "options": ["Flora colossus", "Ent", "Yggdrasil", "Kree"], "answer": "Flora colossus", "diff": "Medium"},
    {"question": "What is the Wi-Fi password Karl Mordo gives to Doctor Strange?", "options": ["Shamballa", "Kamar-Taj", "Agamotto", "Vishanti"], "answer": "Shamballa", "diff": "Medium"},
    {"question": "Who directed Captain America: The First Avenger?", "options": ["Joe Johnston", "Russo Brothers", "Jon Favreau", "Joss Whedon"], "answer": "Joe Johnston", "diff": "Medium"},
    {"question": "What fake name does Natasha use in Iron Man 2?", "options": ["Natalie Rushman", "Nadia Roman", "Nancy Roberts", "Natalia Alianovna"], "answer": "Natalie Rushman", "diff": "Medium"},
    {"question": "What is the serial number on Bucky's metal arm in Civil War?", "options": ["73619", "04329", "It doesn't have one", "17492"], "answer": "It doesn't have one", "diff": "Hard"},
    {"question": "In what comic issue did Captain America make his first appearance?", "options": ["Captain America Comics #1", "Action Comics #1", "Tales of Suspense #39", "Avengers #4"], "answer": "Captain America Comics #1", "diff": "Hard"},
    {"question": "What is the name of the doctor who created the Super Soldier Serum?", "options": ["Abraham Erskine", "Arnim Zola", "Howard Stark", "Bruce Banner"], "answer": "Abraham Erskine", "diff": "Hard"},
    {"question": "Which villain killed Captain America in the comics (Civil War aftermath)?", "options": ["Crossbones", "Red Skull", "Baron Zemo", "Winter Soldier"], "answer": "Crossbones", "diff": "Hard"},
    {"question": "What is the name of the treaty that divided the Avengers?", "options": ["Sokovia Accords", "Wakandan Treaty", "Geneva Convention", "Superhuman Registration Act"], "answer": "Sokovia Accords", "diff": "Hard"},
    {"question": "In Thor: Ragnarok, what is the name of the rock-like creature?", "options": ["Korg", "Miek", "Surtur", "Valkyrie"], "answer": "Korg", "diff": "Hard"},
    {"question": "What is the full name of the organization HYDRA's founder?", "options": ["Johann Schmidt", "Heinrich Zemo", "Wolfgang von Strucker", "Alexander Pierce"], "answer": "Johann Schmidt", "diff": "Hard"},
    {"question": "What song plays at the beginning of Iron Man (2008)?", "options": ["Back in Black", "Iron Man", "Thunderstruck", "Highway to Hell"], "answer": "Back in Black", "diff": "Hard"},
    {"question": "What is the name of the dimension Dormammu rules?", "options": ["Dark Dimension", "Quantum Realm", "Mirror Dimension", "Astral Plane"], "answer": "Dark Dimension", "diff": "Hard"},
    {"question": "Which celestial being's severed head serves as the mining colony Knowhere?", "options": ["A Celestial", "Galactus", "Ego", "The Watcher"], "answer": "A Celestial", "diff": "Hard"},
    {"question": "What is the name of Black Panther's sister?", "options": ["Nakia", "Okoye", "Shuri", "Ayo"], "answer": "Shuri", "diff": "Easy"},
    {"question": "Who is the main villain in Thor: Ragnarok?", "options": ["Loki", "Malekith", "Surtur", "Hela"], "answer": "Hela", "diff": "Easy"},
    {"question": "What is the name of Star-Lord's ship?", "options": ["The Milano", "The Benatar", "The Statesman", "The Sanctuary"], "answer": "The Milano", "diff": "Medium"},
    {"question": "Who sacrificed themselves on Vormir for the Soul Stone in Endgame?", "options": ["Hawkeye", "Black Widow", "Gamora", "Nebula"], "answer": "Black Widow", "diff": "Medium"},
    {"question": "What alien race does Ronan the Accuser belong to?", "options": ["Skrull", "Kree", "Sovereign", "Chitauri"], "answer": "Kree", "diff": "Medium"},
    {"question": "Who created Ultron in the MCU?", "options": ["Hank Pym", "Tony Stark & Bruce Banner", "S.H.I.E.L.D.", "HYDRA"], "answer": "Tony Stark & Bruce Banner", "diff": "Easy"},
    {"question": "What is the name of Doctor Strange's cloak?", "options": ["Cloak of Levitation", "Cape of Sorcery", "Mantle of Agamotto", "Shroud of Shadows"], "answer": "Cloak of Levitation", "diff": "Easy"},
    {"question": "What is the real name of the Winter Soldier?", "options": ["Sam Wilson", "Bucky Barnes", "John Walker", "Clint Barton"], "answer": "Bucky Barnes", "diff": "Easy"},
    {"question": "What is the highest-grossing MCU movie?", "options": ["Infinity War", "The Avengers", "No Way Home", "Avengers: Endgame"], "answer": "Avengers: Endgame", "diff": "Medium"},
    {"question": "Who is the director of S.H.I.E.L.D. who forms the Avengers?", "options": ["Phil Coulson", "Alexander Pierce", "Nick Fury", "Maria Hill"], "answer": "Nick Fury", "diff": "Easy"},
    {"question": "What is the name of the dwarf who forged Stormbreaker?", "options": ["Eitri", "Sindri", "Brokkr", "Gimli"], "answer": "Eitri", "diff": "Hard"},
    {"question": "Which MCU movie features the character Goose the Flerken?", "options": ["Guardians of the Galaxy", "Captain Marvel", "Ant-Man", "Thor: Ragnarok"], "answer": "Captain Marvel", "diff": "Medium"},
    {"question": "What is the name of Wanda's reality-altering town?", "options": ["Eastview", "Rosewood", "Westview", "Fairview"], "answer": "Westview", "diff": "Medium"},
    {"question": "What type of radiation gave the Hulk his powers?", "options": ["Cosmic", "Solar", "Gamma", "Ultraviolet"], "answer": "Gamma", "diff": "Easy"},
    {"question": "What is the name of the realm where Ant-Man gets trapped?", "options": ["Microverse", "Quantum Realm", "Dark Dimension", "Mirror Dimension"], "answer": "Quantum Realm", "diff": "Easy"},
    {"question": "Who famously said 'We have a Hulk'?", "options": ["Tony Stark", "Steve Rogers", "Thor", "Nick Fury"], "answer": "Tony Stark", "diff": "Medium"},
    {"question": "What is the true identity of the Taskmaster in Black Widow?", "options": ["Yelena Belova", "Melina Vostokoff", "Antonia Dreykov", "Rick Mason"], "answer": "Antonia Dreykov", "diff": "Hard"},
    {"question": "What is the name of Cap's Howling Commandos friend with a bowler hat?", "options": ["Bucky Barnes", "Gabe Jones", "Jim Morita", "Dum Dum Dugan"], "answer": "Dum Dum Dugan", "diff": "Hard"},
    {"question": "Which character is known as the 'God of Mischief'?", "options": ["Thor", "Loki", "Odin", "Heimdall"], "answer": "Loki", "diff": "Easy"},
    {"question": "What did Tony Stark build in a cave with a box of scraps?", "options": ["Arc Reactor", "Mark I Armor", "J.A.R.V.I.S.", "Repulsors"], "answer": "Mark I Armor", "diff": "Easy"},
    {"question": "What is the name of the sinister organization that infiltrated S.H.I.E.L.D.?", "options": ["A.I.M.", "Ten Rings", "HYDRA", "Leviathan"], "answer": "HYDRA", "diff": "Easy"},
    {"question": "Who is the primary villain in Shang-Chi?", "options": ["The Mandarin / Wenwu", "Razor Fist", "Death Dealer", "Fin Fang Foom"], "answer": "The Mandarin / Wenwu", "diff": "Medium"},
    {"question": "What is the name of the magical book in Multiverse of Madness?", "options": ["Book of Cagliostro", "Darkhold", "Vishanti Book", "Necronomicon"], "answer": "Darkhold", "diff": "Medium"},
    {"question": "Who killed Tony Stark's parents?", "options": ["Red Skull", "Obadiah Stane", "The Winter Soldier", "Baron Zemo"], "answer": "The Winter Soldier", "diff": "Medium"},
    {"question": "What was the name of the protocol that destroyed S.H.I.E.L.D. from within?", "options": ["Project Pegasus", "Project Insight", "Operation Rebirth", "Ultron Program"], "answer": "Project Insight", "diff": "Hard"},
    {"question": "Who secretly founded the Time Variance Authority (TVA)?", "options": ["Kang the Conqueror", "He Who Remains", "Mobius", "Ravonna Renslayer"], "answer": "He Who Remains", "diff": "Hard"},
    {"question": "Which Avenger is a master archer?", "options": ["Hawkeye", "Black Widow", "Falcon", "Winter Soldier"], "answer": "Hawkeye", "diff": "Easy"},
    {"question": "What is the name of the substance used by the Dark Elves in Thor: The Dark World?", "options": ["Tesseract", "Aether", "Orb", "Scepter"], "answer": "Aether", "diff": "Medium"},
    {"question": "What is the real name of the Scarlet Witch?", "options": ["Natasha Romanoff", "Wanda Maximoff", "Carol Danvers", "Hope van Dyne"], "answer": "Wanda Maximoff", "diff": "Easy"},
    {"question": "What is the name of Peter Parker's best friend?", "options": ["Harry Osborn", "Flash Thompson", "Ned Leeds", "Miles Morales"], "answer": "Ned Leeds", "diff": "Easy"}
]

# --- 4. GAME MEMORY & LOGIC ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "boss_health" not in st.session_state:
    st.session_state.boss_health = 10
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = 0

if "feedback_state" not in st.session_state:
    st.session_state.feedback_state = None
if "last_correct_answer" not in st.session_state:
    st.session_state.last_correct_answer = ""
if "outro_played" not in st.session_state:
    st.session_state.outro_played = False

if "available_questions" not in st.session_state:
    st.session_state.available_questions = all_questions.copy()
    
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(st.session_state.available_questions)

def next_question():
    if st.session_state.current_question in st.session_state.available_questions:
        st.session_state.available_questions.remove(st.session_state.current_question)
    if len(st.session_state.available_questions) > 0:
        st.session_state.current_question = random.choice(st.session_state.available_questions)


# --- 5. PERSISTENT AUDIO INJECTION (THE iOS FIX) ---
if st.session_state.game_started and st.session_state.boss_health > 0 and st.session_state.wrong_answers < 3:
    audio_b64 = get_base64_of_bin_file("cap_voice.mp3")
    if audio_b64:
        ios_audio_fix = f"""
        <audio id="cap-audio" autoplay playsinline>
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("cap-audio");
            var introPlayed = false;
            var playPromise = audio.play();
            
            if (playPromise !== undefined) {{
                playPromise.then(function() {{
                    // Desktop browser allowed autoplay
                    introPlayed = true;
                }}).catch(function(error) {{
                    // iOS blocked autoplay; wait for tap
                    function forcePlay() {{
                        if (!introPlayed) {{
                            introPlayed = true;
                            audio.play();
                        }}
                    }}
                    window.parent.document.body.addEventListener('touchstart', forcePlay, {{ once: true }});
                    window.parent.document.body.addEventListener('click', forcePlay, {{ once: true }});
                }});
            }}
        </script>
        """
        st.markdown(ios_audio_fix, unsafe_allow_html=True)


# --- 6. START SCREEN ---
if not st.session_state.game_started:
    st.markdown("<h1 class='marvel-title'>S.H.I.E.L.D. TERMINAL</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align: center; color: #9ca3af; font-family: Rajdhani; font-size: 1.2rem;'>AWAITING CLEARANCE FROM STEVE ROGERS...</div>", unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("INITIALIZE MISSION", use_container_width=True, type="primary"):
            st.session_state.game_started = True
            st.rerun()


# --- 7. THE FEEDBACK CUTSCENE (ANIMATIONS) ---
elif st.session_state.feedback_state is not None:
    st.markdown("<h1 class='marvel-title'>S.H.I.E.L.D. OVERRIDE: RED SKULL PROTOCOL</h1>", unsafe_allow_html=True)
    
    # Calculate health percentages for visual bars
    boss_hp_percent = (st.session_state.boss_health / 10) * 100
    chances_percent = ((3 - st.session_state.wrong_answers) / 3) * 100

    health_html = f"""
    <div style="display: flex; justify-content: space-between; font-family: 'Rajdhani', sans-serif; color: #cbd5e1; font-size: 1.2rem; font-weight: bold; text-transform: uppercase;">
        <span>Red Skull's Health</span>
        <span>Shield Integrity</span>
    </div>
    <div style="display: flex; justify-content: space-between; gap: 40px;">
        <div class="health-container">
            <div class="health-bar-red" style="width: {boss_hp_percent}%;"></div>
        </div>
        <div class="health-container">
            <div class="health-bar-blue" style="width: {chances_percent}%;"></div>
        </div>
    </div>
    """
    st.markdown(health_html, unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    # If she got it RIGHT
    if st.session_state.feedback_state == 'success':
        st.markdown("<p class='mission-success' style='font-size: 3rem; text-shadow: 0 0 20px rgba(16, 185, 129, 0.8);'>💥 BAM! DIRECT HIT! 💥</p>", unsafe_allow_html=True)
        
        gif_col1, gif_col2, gif_col3 = st.columns([1, 2, 1])
        with gif_col2:
            try:
                st.image("cap_strike.gif", use_container_width=True)
            except:
                pass
                
    # If she got it WRONG
    else:
        st.markdown("<p class='mission-success' style='color: #ef4444 !important; font-size: 3rem; text-shadow: 0 0 20px rgba(239, 68, 68, 0.8);'>❌ DODGED! ❌</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='big-question' style='font-size: 2rem; color: #9ca3af !important;'>THE CORRECT ANSWER WAS:<br><span style='color: #ef4444;'>{st.session_state.last_correct_answer}</span></p>", unsafe_allow_html=True)
        
        gif_col1, gif_col2, gif_col3 = st.columns([1, 2, 1])
        with gif_col2:
            try:
                st.image("red_skull_dodge.gif", use_container_width=True)
            except:
                pass

    time.sleep(1.75)
    st.session_state.feedback_state = None
    st.rerun()


# --- 8. GAME OVER & WIN SCREENS ---
elif st.session_state.boss_health <= 0:
    st.balloons()
    
    if not st.session_state.outro_played:
        outro_b64 = get_base64_of_bin_file("cap_outro.mp3")
        if outro_b64:
            ios_outro_fix = f"""
            <audio id="cap-outro-audio" autoplay playsinline>
                <source src="data:audio/mp3;base64,{outro_b64}" type="audio/mp3">
            </audio>
            <script>
                var outroAudio = document.getElementById("cap-outro-audio");
                var outroPlayedJs = false;
                var playPromiseOutro = outroAudio.play();
                
                if (playPromiseOutro !== undefined) {{
                    playPromiseOutro.then(function() {{
                        // Desktop browser allowed autoplay
                        outroPlayedJs = true;
                    }}).catch(function(error) {{
                        // iOS blocked autoplay; wait for tap
                        function forcePlayOutro() {{
                            if (!outroPlayedJs) {{
                                outroPlayedJs = true;
                                outroAudio.play();
                            }}
                        }}
                        window.parent.document.body.addEventListener('touchstart', forcePlayOutro, {{ once: true }});
                        window.parent.document.body.addEventListener('click', forcePlayOutro, {{ once: true }});
                    }});
                }}
            </script>
            """
            st.markdown(ios_outro_fix, unsafe_allow_html=True)
            st.session_state.outro_played = True
            
    st.markdown("<p class='mission-success'>🎉 MISSION ACCOMPLISHED! 🎉</p>", unsafe_allow_html=True)
    st.markdown("<p class='bday-text'>WISHING A VERY<br>HAPPY BIRTHDAY TANYA!</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("PLAY AGAIN", use_container_width=True):
            st.session_state.boss_health = 10
            st.session_state.wrong_answers = 0
            st.session_state.outro_played = False
            st.session_state.available_questions = all_questions.copy()
            st.session_state.current_question = random.choice(st.session_state.available_questions)
            st.rerun()

elif st.session_state.wrong_answers >= 3:
    st.markdown("<p class='big-question' style='color: #ef4444 !important; font-size: 5rem !important;'>💀 MISSION FAILED 💀</p>", unsafe_allow_html=True)
    st.write("<div style='text-align: center; font-family: Rajdhani; font-size: 1.5rem;'><strong style='color: #ef4444;'>Red Skull:</strong> 'You were no match for HYDRA! The presents are mine!'</div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center; font-family: Rajdhani; font-size: 1.5rem;'><strong style='color: #60a5fa;'>Cap:</strong> 'We lost this battle, but the war isn't over. Dust yourself off, we are going back in.'</div>", unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("RETRY MISSION", use_container_width=True):
            st.session_state.boss_health = 10
            st.session_state.wrong_answers = 0
            st.session_state.outro_played = False
            st.session_state.available_questions = all_questions.copy()
            st.session_state.current_question = random.choice(st.session_state.available_questions)
            st.rerun()


# --- 9. MAIN GAME UI ---
else:
    st.markdown("<h1 class='marvel-title'>S.H.I.E.L.D. OVERRIDE: RED SKULL PROTOCOL</h1>", unsafe_allow_html=True)

    # Calculate health percentages for visual bars
    boss_hp_percent = (st.session_state.boss_health / 10) * 100
    chances_percent = ((3 - st.session_state.wrong_answers) / 3) * 100

    health_html = f"""
    <div style="display: flex; justify-content: space-between; font-family: 'Rajdhani', sans-serif; color: #cbd5e1; font-size: 1.2rem; font-weight: bold; text-transform: uppercase;">
        <span>Red Skull's Health</span>
        <span>Shield Integrity</span>
    </div>
    <div style="display: flex; justify-content: space-between; gap: 40px;">
        <div class="health-container">
            <div class="health-bar-red" style="width: {boss_hp_percent}%;"></div>
        </div>
        <div class="health-container">
            <div class="health-bar-blue" style="width: {chances_percent}%;"></div>
        </div>
    </div>
    """
    st.markdown(health_html, unsafe_allow_html=True)
    
    q = st.session_state.current_question
    
    st.markdown(f"<p class='big-question'>{q['question']}</p>", unsafe_allow_html=True)
    
    selected_option = st.radio("Select your answer:", q['options'], index=None, label_visibility="collapsed")
    
    # We wrap the button in columns to force it exactly to the center!
    st.write("")
    btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
    with btn_col2:
        if st.button("THROW SHIELD!", type="primary", use_container_width=True):
            if selected_option == None:
                st.warning("You must select an answer before throwing the shield!")
                
            elif selected_option == q['answer']:
                st.session_state.boss_health -= 1
                st.session_state.feedback_state = 'success'
                next_question()
                st.rerun()
                
            else:
                st.session_state.wrong_answers += 1
                st.session_state.last_correct_answer = q['answer']
                st.session_state.feedback_state = 'error'
                next_question()
                st.rerun()