import streamlit as st

def init_session_state():
    defaults = {
        'score': 0,
        'rounds': 0,
        'show_try_again': False,
        'game_started': False,
        'question_order': [],
        'question_index': 0,

    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_game():
    st.session_state.score = 0
    st.session_state.rounds = 0
    st.session_state.show_try_again = False
    st.session_state.game_started = False
    if 'question_order' in st.session_state:
        del st.session_state.question_order
    if 'question_index' in st.session_state:
        st.session_state.question_index = 0
    if 'current_question' in st.session_state:
        del st.session_state.current_question
    if 'last_question_index' in st.session_state:
        del st.session_state.last_question_index
    if 'last_logged_index' in st.session_state:
        del st.session_state.last_logged_index
    if 'answered_wrong' in st.session_state:
        del st.session_state.answered_wrong



