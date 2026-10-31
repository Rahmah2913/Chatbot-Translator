
import streamlit as st
from translate import Translator
from gtts import gTTS
import io

st.set_page_config(page_title="Translator Chatbot")

LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Hindi": "hi",
    "Turkish": "tr",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko"
}

st.title("🌍 Translator with Voice")

target = st.selectbox("Translate into:", list(LANGUAGES.keys()), index=1)

text = st.text_area("Enter your text:")

if st.button("Translate and Generate Voice"):
    if not text.strip():
        st.warning("Please enter text!")

    else:
        try:
            translator = Translator(
                to_lang=LANGUAGES[target]
            )

            result = translator.translate(text)
            if not result:
                st.error("The translation service returned no text.")
                st.stop()

            st.subheader("Translated Text")
            st.write(result)

            # Generate voice in the target language
            audio = gTTS(
                text=result,
                lang=LANGUAGES[target]
            )

            audio_bytes = io.BytesIO()
            audio.write_to_fp(audio_bytes)
            audio_bytes.seek(0)

            st.subheader("🔊 Translated Voice")
            st.audio(audio_bytes, format="audio/mp3")

        except Exception as e:
            st.error("Translation or voice generation failed.")
            st.caption(str(e))