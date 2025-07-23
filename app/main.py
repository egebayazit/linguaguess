import streamlit as st
import random
import pandas as pd

# Load sentence data
@st.cache_data
def load_sentences():
    df = pd.read_csv("data/audio/sentences.csv")
    return df

# Pick one random question
def get_question(df):
    row = df.sample().iloc[0]
    correct_lang = row['language']
    sentence = row['sentence']
    # Pick 3 wrong options
    wrong_langs = df[df['language'] != correct_lang]['language'].sample(3).tolist()
    options = wrong_langs + [correct_lang]
    random.shuffle(options)
    return sentence, correct_lang, options

# --- Streamlit UI ---
st.set_page_config(page_title="LinguaGuess", page_icon="🌍")
st.title("🌍 LinguaGuess")
st.subheader("Can you guess the language from the sentence?")

df = load_sentences()
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.rounds = 0
if 'show_try_again' not in st.session_state:
    st.session_state.show_try_again = False      # hide by default

# Initialize question only once
if 'current_question' not in st.session_state:
    sentence, answer, options = get_question(df)
    st.session_state.current_question = {
        'sentence': sentence,
        'answer': answer,
        'options': options
    }

q = st.session_state.current_question


st.markdown(f"### Sentence:\n> *{q['sentence']}*")


selected = st.radio("Which language is this?", q['options'])


if st.button("Submit"):
    st.session_state.rounds += 1
    if selected == q['answer']:
        st.success("✅ Correct!")
        st.session_state.score += 1
        st.session_state.show_try_again = False  
        # 🔁 Generate and store next question
        sentence, answer, options = get_question(df)
        st.session_state.current_question = {
        'sentence': sentence,
        'answer': answer,
        'options': options
    }
        st.rerun()
    else:
        st.error(f"❌ Nope! The correct answer was **{q['answer']}**.")
        st.session_state.show_try_again = True
        st.info(f"Score: {st.session_state.score} / {st.session_state.rounds}")

if st.session_state.show_try_again:
    if st.button("Try Again"):
        st.session_state.score = 0
        st.session_state.rounds = 0
        st.session_state.show_try_again = False   # hide again for next round

        # generate and store next question
        sentence, answer, options = get_question(df)
        st.session_state.current_question = {
            'sentence': sentence,
            'answer': answer,
            'options': options
        }
        st.rerun()


