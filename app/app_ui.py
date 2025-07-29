import streamlit as st
from session_utils import reset_game
from core.question_generator import generate_question
import logging
import pandas as pd
from styles import apply_global_styles

def game_setup_screen(difficulties: list[str]) -> None:
    apply_global_styles()
    
    # Add some top spacing
    st.markdown("<div style='height: 80px'></div>", unsafe_allow_html=True)
    
    # Main title with enhanced styling
    st.markdown("<div class='main-title'>🌍 LinguaGuess</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>🧠 Choose Your Difficulty</div>", unsafe_allow_html=True)
    
    # Add a description/tagline
    st.markdown("""
        <div style='text-align: center; color: white; font-size: 18px; 
                    margin: 20px 0 40px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);'>
            Test your language knowledge with sentences from around the world!
        </div>
    """, unsafe_allow_html=True)
    
    # Replace the flags section with:
    st.markdown("""
    <div style='text-align: center; margin: 30px 0;'>
        <span style='font-size: 40px; margin: 0 15px;'>🏴</span>
        <span style='font-size: 40px; margin: 0 15px;'>🏳️</span>
        <span style='font-size: 40px; margin: 0 15px;'>🌍</span>
        <span style='font-size: 40px; margin: 0 15px;'>🗺️</span>
        <span style='font-size: 40px; margin: 0 15px;'>🌐</span>
    </div>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        difficulty = st.selectbox("Difficulty", difficulties, index=0)

    # Center the button using columns
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("🚀 Start Game"):
            st.session_state.difficulty = difficulty
            st.session_state.game_started = True
            st.session_state.score = 0
            st.session_state.rounds = 0
            st.session_state.hint_uses = 0
            st.session_state.hints_shown = set()
            for key in ["current_question", "selected_answer", "failed_last_question", "show_hint_now"]:
                st.session_state.pop(key, None)
            logging.info(f"Game started with difficulty: {difficulty}")
            st.rerun()




def game_loop(filtered_df: pd.DataFrame) -> None:
    apply_global_styles()
    if not st.session_state.question_order:
        st.session_state.question_order = filtered_df.sample(frac=1).index.tolist()
        st.session_state.question_index = 0
        logging.info("Shuffled question order initialized.")

    if st.session_state.question_index >= len(st.session_state.question_order):
        st.success("🎉 You've completed all questions!")
        st.info(f"Final Score: {st.session_state.score} / {st.session_state.rounds}")
        if st.button("Restart Game"):
            logging.info("Game completed. User restarted.")
            reset_game()
            st.rerun()
        return

    row_idx = st.session_state.question_order[st.session_state.question_index]
    row = filtered_df.loc[row_idx]
    sentence, answer = row['sentence'], row['language']
    hint = row['hint'] if 'hint' in row and pd.notna(row['hint']) else 'No hint available'
    options = generate_question(filtered_df, correct_lang=answer)

    if (
        'current_question' not in st.session_state or
        st.session_state.question_index != st.session_state.get('last_question_index')
    ):
        st.session_state.current_question = {
            'sentence': sentence,
            'answer': answer,
            'options': options,
            'hint': hint
        }
    st.session_state.last_question_index = st.session_state.question_index
    current_question = st.session_state.current_question

    # ⛔ Handle incorrect answer
    if st.session_state.get("failed_last_question", False):
        st.error(f"❌ Nope! The correct answer was **{current_question['answer']}**.")
        st.info(f"Score: {st.session_state.score} / {st.session_state.rounds}")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔁 Try Again"):
                logging.info("User clicked Try Again after incorrect answer")
                st.session_state.score = 0
                st.session_state.rounds = 0
                st.session_state.hint_uses = 0
                st.session_state.hints_shown = set()
                st.session_state.question_index += 1
                for key in ["current_question", "selected_answer", "failed_last_question", "show_hint_now"]:
                    st.session_state.pop(key, None)
                st.rerun()

        with col2:
            if st.button("🎯 Change Difficulty"):
                logging.info("User returned to difficulty selection screen")
                reset_game()
                st.session_state.game_started = False
                st.rerun()
        return

    # 📌 Display question
    st.markdown(f"### Sentence:\n> *{current_question['sentence']}*")

    # 💡 Hint button logic
    hints_left = 3 - st.session_state.hint_uses
    question_key = st.session_state.question_index
    already_shown = question_key in st.session_state.hints_shown

    if st.button(f"💡 Show Hint {hints_left}", key=f"hint_button_{question_key}", disabled=hints_left == 0 or already_shown):
        st.session_state.show_hint_now = True
        st.rerun()

    if st.session_state.get("show_hint_now"):
        st.session_state.hint_uses += 1
        st.session_state.hints_shown.add(question_key)
        st.session_state.show_hint_now = False
        st.rerun()

    if already_shown:
        st.info(current_question['hint'])

    # 🎯 Answer options
    st.session_state.selected_answer = st.radio(
        "Which language is this?",
        current_question['options'],
        key=f"q_{question_key}"
    )

    if st.button("Submit"):
        selected = st.session_state.get("selected_answer")
        if selected is None:
            st.warning("Please select an option before submitting.")
            return

        st.session_state.rounds += 1
        correct = current_question['answer']

        if selected == correct:
            st.session_state.score += 1
            logging.info(f"User selected: {selected} → Correct (Score increased)")
            st.success("✅ Correct!")
            st.session_state.question_index += 1
            for key in ["current_question", "selected_answer", "show_hint_now"]:
                st.session_state.pop(key, None)
            logging.info(f"Score: {st.session_state.score} / {st.session_state.rounds}")
            st.rerun()
        else:
            st.session_state.failed_last_question = True
            logging.info(f"User selected: {selected} → Incorrect (Correct was: {correct})")
            logging.info(f"Score: {st.session_state.score} / {st.session_state.rounds}")
            st.rerun()
