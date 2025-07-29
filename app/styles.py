import streamlit as st

def apply_global_styles():
    st.markdown(
        """
        <style>
        /* Hide Streamlit header/toolbar */
        header[data-testid="stHeader"],
        .css-1rs6os.edgvbvh3,  /* Menu button */
        .css-1dp5vir.e8zbici2  /* Deploy button */ {
            display: none;
        }

        /* Gradient background */
        div[data-testid="stAppViewContainer"] {
            background: #00416A !important;
            background: -webkit-linear-gradient(to right, #FFE000, #799F0C, #00416A) !important;
            background: linear-gradient(to right, #FFE000, #799F0C, #00416A) !important;
            min-height: 100vh !important;
        }

        /* Global font and text */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Segoe UI', sans-serif;
            color: white;
        }

        body {
            background-color: transparent;
        }

        /* Title Styling */
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .subtitle {
            text-align: center;
            font-size: 1.5rem;
            color: #fff;
            margin-bottom: 1rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }

        /* Buttons */
        .stButton > button {
            background: rgba(255, 255, 255, 0.25) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.4) !important;
            border-radius: 12px !important;
            padding: 0.6rem 1.2rem !important;
            font-size: 16px !important;
            font-weight: bold !important;
            backdrop-filter: blur(10px) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
            white-space: nowrap !important;
            min-width: fit-content !important;
        }

        .stButton > button:hover {
            background: rgba(255, 255, 255, 0.35) !important;
            transform: translateY(-2px) !important;
        }

        /* Flag emoji row */
        .emoji-flags {
            font-size: 2.5rem;
            text-align: center;
            margin: 20px 0;
        }

        /* Score display */
        .score-info {
            text-align: center;
            font-size: 1.2rem;
            color: white;
            margin-top: 10px;
        }

        /* Hint Box */
        .hint-box {
            background: rgba(255,255,255,0.2);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            color: #fff;
            font-style: italic;
            backdrop-filter: blur(5px);
            margin-top: 15px;
        }

        /* Question container */
        .card {
            background: rgba(255, 255, 255, 0.15);
            padding: 2rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            margin: 1rem auto;
            max-width: 700px;
            color: white;
        }

        /* Mascot */
        .mascot {
            position: fixed;
            bottom: 10px;
            right: 20px;
            font-size: 20px;
            background: rgba(0, 0, 0, 0.25);
            padding: 0.6rem 1rem;
            border-radius: 8px;
            backdrop-filter: blur(5px);
            z-index: 1000;
        }

        /* Improve radio spacing */
        .stRadio > div {
            gap: 1rem;
        }

        /* Progress bar color */
        .stProgress > div > div > div {
            background-color: #fff176;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
