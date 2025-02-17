import streamlit as st
import requests

st.title("Okta Text Summarizer")

# User input
text = st.text_area("Enter your text here: ")

if st.button("Summarize"):
    if text:
        response = requests.post("https://text-summarizer-ozgj.onrender.com", json={"text":text})
        summary = response.json().get("summary", "Error")
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("PLease enter some text: ")