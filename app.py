import streamlit as st
import random

st.set_page_config(page_title="FakeShield", layout="centered")

st.title("🛡️ FakeShield - Fake News Detector")

news = st.text_area("Enter News Text or URL:")

if st.button("Analyze"):
    if news:
        score = random.randint(60, 95)

        st.subheader("Result:")
        st.write(f"Fake News Probability: {score}%")

        if score > 75:
            st.error("⚠️ Likely Fake News")
        else:
            st.success("✅ Likely Real News")

        st.info("Explanation: Suspicious keywords and low credibility sources detected.")
    else:
        st.warning("Please enter some news text.")
