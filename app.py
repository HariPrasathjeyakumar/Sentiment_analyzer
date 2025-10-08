import streamlit as st
from textblob import TextBlob

st.set_page_config(
    page_title="📝 Sentiment Analyzer",
    page_icon="😊",
    layout="centered",
)

st.title("📝 Sentiment Analyzer")
st.markdown("Analyze the sentiment of your text!")

user_input = st.text_area("Enter text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive 😊"
            color = "#00ff99"
        elif polarity < 0:
            sentiment = "Negative 😡"
            color = "#ff4d4d"
        else:
            sentiment = "Neutral 😐"
            color = "#cccccc"

        st.markdown(f"""
        <div style="padding:20px; border-radius:10px; background-color:{color}; color:white">
            <p style="font-size:18px;"><b>Text:</b> {user_input}</p>
            <p style="font-size:22px;"><b>Sentiment:</b> {sentiment}</p>
        </div>
        """, unsafe_allow_html=True)
