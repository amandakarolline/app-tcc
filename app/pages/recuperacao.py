import streamlit as st

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.logo('static/Logo_UFMA_colorido_maior.png', link=None, icon_image='static/Logo_UFMA_colorido.png')

left, right = st.columns(2)

with left:
    st.title("SISU :violet[SIGAA] UFMA")
    st.write("Descubra sua posição antes do processamento de matrícula")

with right:
    with st.container():
        st.markdown('# Recuperar Senha')

    with st.form(key='recuperacao'):
        usuario_recuperar = st.text_input(label='Usuário', key='usuario_recuperacao')
        email_recuperar = st.text_input(label='Email Cadastrado', key='email_recuperacao')

        st.form_submit_button(label="Recuperar Senha")