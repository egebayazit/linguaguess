import random
import pandas as pd
from typing import List

def generate_question(filtered_df: pd.DataFrame, correct_lang: str) -> List[str]:
    # Get distinct wrong languages
    wrong_langs = filtered_df[filtered_df['language'] != correct_lang]['language'].drop_duplicates()
    sampled = wrong_langs.sample(n=min(3, len(wrong_langs))).tolist()

    # Add correct answer and shuffle
    options = sampled + [correct_lang]
    random.shuffle(options)

    return options
