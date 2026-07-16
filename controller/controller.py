from model import model
from view import view
import streamlit as st


def iniciar():
    if "tela" not in st.session_state:
        st.session_state.tela = "menu"

    if st.session_state.tela == "menu": 
        opcao = view.most_menu()

        if st.button("Acessar"):
            st.session_state.tela = opcao
            st.rerun()
    elif st.session_state.tela == "Adicionar gasto":
        gasto = view.ler_gasto()

        if st.button("Confirmar"):
            model.add(gasto)
            st.success("Adicionado com sucesso!")
        
        if st.button("Voltar"):
            st.session_state.tela = "menu"
            st.rerun()

    elif st.session_state.tela == "Listar gastos":
        gastos = model.listar()
        view.most_gastos(gastos)

        if st.button("Voltar"):
            st.session_state.tela = "menu"
            st.rerun()

    elif st.session_state.tela == "Ver total":
        total = model.total()
        st.write(f"Total de gastos: R$ {total}")

        if st.button("Voltar"):
            st.session_state.tela = "menu"
            st.rerun()

    if st.session_state.tela == "Remover gasto":
        nome = view.rem_nome()

        if st.button("Remover"):
            if model.remover(nome):
                st.success("Removido com sucesso!")
            else:
                st.error("Gasto não encontrado.")

        if st.button("Voltar"):
            st.session_state.tela = "menu"
            st.rerun()

    if st.session_state.tela == "Quanto tenho?":
        valor = view.oq_tenho()

        if st.button("Calcular"):
            saldo = model.quanto_tenho(valor)
            st.write(f"Você tem R$ {saldo} na carteira.")

        if st.button("Voltar"):
            st.session_state.tela = "menu"
            st.rerun()