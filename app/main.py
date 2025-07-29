import streamlit as st
import logging
from config import DIFFICULTY_LEVELS
from data_loader import load_sentences
from session_utils import init_session_state
from app_ui import game_setup_screen, game_loop
from styles import apply_global_styles

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

# --- Set up page ---
st.set_page_config(page_title="LinguaGuess", page_icon="🌍")

# Apply global styles
apply_global_styles()

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