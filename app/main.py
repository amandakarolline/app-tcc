import streamlit as st
# import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import time
import hmac


def password_entered():
    if st.session_state['usuario'] in st.secrets[
        'passwords'
    ] and hmac.compare_digest(
        st.session_state['senha'],
        st.secrets.passwords[st.session_state['usuario']],
    ):
        st.session_state['senha_correta'] = True
        del st.session_state['senha']
        del st.session_state['usuario']
    else:
        st.session_state['senha_correta'] = False


with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.logo('static/Logo_UFMA_colorido_maior.png', link=None, icon_image='static/Logo_UFMA_colorido.png')

left, right = st.columns(2)

with left:
    st.title("SISU :violet[SIGAA] UFMA")
    st.write("Descubra sua posição antes do processamento de matrícula")

with right:
    with st.container():
        st.markdown('# Faça seu login')

        tab_login, tab_cadastro = st.tabs(["Login", "Cadastre-se"])
        with tab_login:
            with st.form(key='login'):
                usuario_input = st.text_input(label='Usuário', key='usuario')
                senha_input = st.text_input(label='Senha', key='senha', type='password')
                entrar, recuperar = st.columns(2)
                with entrar:
                    st.form_submit_button(label="Entrar", on_click=password_entered())
                with recuperar:
                    st.page_link('pages/recuperacao.py', label='Esqueci a senha')
        with tab_cadastro:
            with st.form(key='cadastro'):
                nome = st.text_input(label='Nome Completo', key='nome')
                matricula = st.text_input(label='Matricula', key='matricula')
                email = st.text_input(label='Email', key='email')
                senha = st.text_input(label='Senha', key='senha_cadastro', type='password')
                confirmar_senha_input = st.text_input(label='Confirmar senha', key='confirmar_senha', type='password')
                st.form_submit_button(label="Cadastrar")
