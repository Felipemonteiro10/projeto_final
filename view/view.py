import streamlit as st

def most_menu():
    st.title("Menu principal")
    st.header("Escolha uma opção")

    st.write("1 - Adicionar gasto")
    st.write("2 - Listar gastos")
    st.write("3 - Ver total")
    st.write("4 - Remover gasto")
    st.write("5 - Quanto tenho?")
    st.write("0 - Sair")

def oq_tenho():
    st.write("Quanto você tem na carteira?")
    return float(st.number_input("Digite o valor: "))

def ler_gasto():

    nome = st.text_input("Nome: ")
    valor = st.number_input("Valor: ")
    categoria = st.text_input("Categoria: ")

    return {
        "nome": nome,
        "valor": valor,
        "categoria": categoria
    }

def most_gastos(lista):
    for gasto in lista:
        st.write(gasto)

def rem_nome():
    nome = st.text_input("Digite o nome do gasto a ser removido: ")
    return nome