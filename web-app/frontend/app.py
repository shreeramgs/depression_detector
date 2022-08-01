import streamlit as st
import requests
from PIL import Image

image = Image.open('wordcloud.png')
session = requests.Session()


def fetch(session, url, data):
    try:
        result = session.get(url, json={'text': data})
        json = result.json()
        return bool(json['is_suicide'])
    except Exception:
        return False


st.title("Suicidal Posts Detection using NLP")
st.subheader("Help is availabe! Call 988")
input_text = st.text_area("Enter the text to analyze")

if st.button('Check'):
    data = fetch(session, f"http://127.0.0.1:8000/predict", input_text)
    if data:
        suicide_text = '<p style="color:Red; font-size: 20px;">This post has suicidal intention</p>'
        st.markdown(suicide_text, unsafe_allow_html=True)
    else:
        suicide_text = '<p style="color:Green; font-size: 20px;">This post has no suicidal intention</p>'
        st.markdown(suicide_text, unsafe_allow_html=True)

st.image(image, caption="Wordcloud of frequently used words")
