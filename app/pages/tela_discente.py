import streamlit as st
from app.controller.controller import lista_turmas, classificacao

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.logo('static/Logo_UFMA_colorido_maior.png', link=None, icon_image='static/Logo_UFMA_colorido.png')