
import streamlit as st
from translate import Translator
import requests

st.set_page_config(page_title="Translator Chatbot")

# Available languages
LANGUAGES = {
    "English": "en",
        "Urdu": "ur",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Chinese": "zh-cn",
        "Arabic": "ar",
        "Hindi": "hi",
        "Turkish": "tr",
        "Russian": "ru",
        "Japanese": "ja",
        "Korean": "ko"
}

# Store translation history
if "history" not in st.session_state:
    st.session_state.history = []

# App title
st.title("🌍 Translator Chatbot")
st.write("Enter text and select a language.")

# Select target language
language = st.selectbox(
    "Translate into:",
    list(LANGUAGES.keys())
)

# Input text
text = st.text_area("Enter your text:")

# Translate button
if st.button("Translate"):

    if not text.strip():
        st.warning("Please enter some text.")

    else:
        try:
            translator = Translator(
                to_lang=LANGUAGES[language]
            )

            result = translator.translate(text)

            st.success("Translation completed!")
            st.write("Translated Text:")
            st.write(result)

            st.session_state.history.append({
                "original": text,
                "translated": result,
                "language": language
            })

        except Exception as error:
            st.error("Translation failed. Please try again.")
            st.caption(str(error))