import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Ashton Southall", page_icon="wave")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Load Assets ----
lottie_animation = load_lottieurl("https://lottie.host/7d664a52-b3ee-4702-8080-98d3eff10e9a/nJR5u4spAU.json")

## ---- Headers ----
with st.container():
    st.subheader("Hi, I'm Ashton :wave:")
    st.title("A Network Administrator From Australia")
    st.write("I am a passionate and driven professional in the tech industy. I am currently working at AirBridge Networks, where I am constantly learning and applying new skills to help businesses and organizations stay connected in a fast moving world")
    st.write("[Connect With Me](https://www.linkedin.com/in/ashtonsouthall/)")

