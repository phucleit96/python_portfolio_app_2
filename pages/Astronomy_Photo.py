import requests
import streamlit as st
import os

ASTRO_KEY = os.getenv("ASTRO_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={ASTRO_KEY}"
response = requests.get(url)
content = response.json()

st.title("ASTRONOMY PICTURE OF THE DAY!!!")
st.markdown(f"<h1 style='text-align: center;'>{content['title']}</h1>", unsafe_allow_html=True)
st.image(image=content['url'])
st.write(content['explanation'])
st.markdown(f"<p style='text-align: right;'><i>{content['copyright']}</i></p>", unsafe_allow_html=True)