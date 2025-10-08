import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="📝 Sentiment Analyzer",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("📝 Sentiment Analyzer")
st.markdown("Analyze the sentiment of your text!")

# Use CPU-friendly pipeline (onnxruntime backend)
with st.spinner("Loading model..."):
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1  # CPU only
    )

user_input = st.text_area("Enter text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner("Analyzing..."):
            result = sentiment_pipeline(user_input)[0]
            label = result["label"]
            score = result["score"]

            color = "#00ff99" if label == "POSITIVE" else "#ff4d4d"
            emoji = "😊" if label == "POSITIVE" else "😡"

            st.markdown(f"""
            <div style="padding:20px; border-radius:10px; background-color:{color}; color:white">
                <p style="font-size:18px;"><b>Text:</b> {user_input}</p>
                <p style="font-size:22px;"><b>Sentiment:</b> {label} {emoji} ({score*100:.2f}%)</p>
            </div>
            """, unsafe_allow_html=True)
