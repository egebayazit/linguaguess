# 🌍 LinguaGuess: AI-Powered Language Guessing Game

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

> **Experience the power of NLP:** A dynamic, educational game that challenges players to identify languages based on AI-generated text snippets and context-aware hints.

## 🚀 Overview

**LinguaGuess** is not just a trivia game; it is a modular NLP application showcasing the integration of **Transformer models** into a real-time interactive web experience. Unlike traditional games with hardcoded databases, LinguaGuess utilizes Generative AI to dynamically create puzzles, hints, and evaluate player performance on the fly.

## ⚡ Key Features

* **🧠 Dynamic Content Generation:** Leveraging **Transformer models**, the system generates unique text samples and cultural hints in real-time, ensuring no two game sessions are alike.
* **🎯 Adaptive Difficulty Engine:** A custom scoring algorithm adjusts the game difficulty based on the player's streak and response time, providing a tailored user experience.
* **💡 Context-Aware Hints:** instead of static clues, the AI analyzes the target language's linguistic features to generate progressive hints (e.g., script type, grammatical structure) without giving away the answer.
* **🔄 Complex State Management:** Robust session handling between the **Streamlit** frontend and **FastAPI** backend ensures smooth gameplay and persistent score tracking without latency.

## 🏗️ Architecture

The project follows a decoupled architecture:

1.  **Frontend (Streamlit):** Handles user interaction, renders the game UI, and manages session state (preserving scores and streaks across re-runs).
2.  **Backend (FastAPI):** Serves as the logic hub, hosting the NLP inference engine and game logic API endpoints.
3.  **AI Engine:** Utilizes pre-trained Transformer models (via HuggingFace) for text generation and language classification tasks.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Web Framework:** Streamlit (UI), FastAPI (API)
* **AI/NLP:** HuggingFace Transformers, PyTorch
* **Logic:** Pydantic (Data Validation), AsyncIO

## 📸 Usage

1.  The AI generates a text snippet in a random language.
2.  The player guesses the language.
3.  If stuck, the player can request an **AI-generated hint** (costing points).
4.  The system evaluates the answer and updates the dynamic score.

---
*Created by [Ege Bayazit](https://www.linkedin.com/in/egebayazit/)*
