import streamlit as st
import logging
from config import DIFFICULTY_LEVELS
from data_loader import load_sentences
from session_utils import init_session_state
from app_ui import game_setup_screen, game_loop

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

# --- Set up page ---
st.set_page_config(page_title="LinguaGuess", page_icon="🌍")

st.markdown("""
    <style>
    body {
        background-color: #e0f7fa;
    }
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #555;
        margin-bottom: 1rem;
    }
    .difficulty-box {
        background-color: #ffffffcc;
        padding: 2rem;
        border-radius: 1rem;
        width: 100%;
        max-width: 600px;
        margin: 2rem auto;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
    }
    .start-btn {
        text-align: center;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)


# --- Load dataset ---
df = load_sentences()
init_session_state()

# --- Main App Flow ---
if not st.session_state.game_started:
    game_setup_screen(DIFFICULTY_LEVELS)
else:
    difficulty = st.session_state.difficulty
    filtered_df = df[df['difficulty'] == difficulty]

    if filtered_df.empty:
        st.warning(f"No questions found for difficulty '{difficulty}'. Please restart and choose another level.")
        st.stop()

    game_loop(filtered_df)
