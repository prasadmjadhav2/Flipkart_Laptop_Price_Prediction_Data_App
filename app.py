# Home

import streamlit as st
import webbrowser

st.title(':blue[Elon Musk Laptop Price Prediction]')
st.header(':red[Innomatics Research Labs]')
st.caption('Project By PRASAD JADHAV')

linkedin = 'https://linkedin.com/in/prasadmjadhav2'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)

github = 'http://github.com/prasadmjadhav2'

if st.button('GitHub'):
    webbrowser.open_new_tab(github)    