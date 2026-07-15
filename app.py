import streamlit as st
from controller import controller

st.title("Controle de Gastos")

st.write("Bem-vindo ao sistema!")

if "tela" not in st.session_state:
    st.session_state.tela = "iniciar"