from model import model
from view import view
import streamlit as st


def iniciar():
    st.write("Bem-vindo ao sistema de gastos!")
    opcao = -67

    while opcao != 0:

        if st.button("Sair"):
            st.session_state.tela = "sair"
            break

        elif st.button("Inserir usuário"):
            st.session_state.tela = "inserir"
        st.rerun()

        if st.button("Todos usuário"):
            st.session_state.tela = "Ver todos"
        st.rerun()

        if st.button("Listar usuários"):
            st.session_state.tela = "listar"
        st.rerun()

        if st.button("Remover usuário"):
            st.session_state.tela = "remover"
        st.rerun()

        if st.button("Quanto tenho?"):
            st.session_state.tela = "quanto tenho"
        st.rerun()
