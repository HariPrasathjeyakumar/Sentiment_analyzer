# app.py
import streamlit as st
from transformers import pipeline
import torch

# -----------------------------
# 1️⃣ Page configuration
# -----------------------------
st.set_page_config(
    page_title="📝 Sentiment Analyzer",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------
# 2️⃣ Load pretrained sentiment model with spinner
# -----------------------------
import time

with st.spinner("Loading sentiment model... This may take a few minutes!"):
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1  # CPU only (Streamlit Cloud has no GPU by default)
    )


# -----------------------------
# 3️⃣ App title & description
# -----------------------------
st.title("📝 Sentiment Analyzer")
st.markdown("""
This app analyzes the **sentiment of your text** using a pretrained DistilBERT model.  
Type any sentence, tweet, or review, and see if it's **Positive** or **Negative**!
""")

# -----------------------------
# 4️⃣ Input text area
# -----------------------------
user_input = st.text_area(
    "Type your text below:",
    placeholder="Enter your text here...",
    height=120
)

# -----------------------------
# 5️⃣ Analyze button
# -----------------------------
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text!")
    else:
        # Run prediction
        result = sentiment_pipeline(user_input)[0]
        label = result['label']
        score = result['score']

        # Map to friendly emoji and color
        if label == "POSITIVE":
            emoji = "😊"
            color = "#00ff99"  # green
            text_label = "Positive"
        else:
            emoji = "😡"
            color = "#ff4d4d"  # red
            text_label = "Negative"

        # Display in a visually appealing card
        st.markdown(f"""
        <div style="padding:20px; border-radius:10px; background-color:{color}; color:white">
            <h3>📝 Text:</h3>
            <p>{user_input}</p>
            <h3>📊 Sentiment:</h3>
            <p style="font-size:22px; font-weight:bold">{text_label} {emoji} (Confidence: {score*100:.2f}%)</p>
        </div>
        """, unsafe_allow_html=True)

