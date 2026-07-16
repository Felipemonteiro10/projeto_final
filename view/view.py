import streamlit as st

def most_menu():
    st.title("Controle de Gastos")
    st.text("Produzido por: Isis Vitória e Felipe M.")

    st.header("Menu principal")

    opcao = st.selectbox("Escolha uma opção:", 
    ["Adicionar gasto",
    "Listar gastos",
    "Ver total",
    "Remover gasto", 
    "Quanto tenho?"])
    return opcao

def oq_tenho():
    st.write("Quanto você tem na carteira?")
    return st.number_input("Digite o valor: ")

def ler_gasto():

    nome = st.text_input("Nome: ")
    valor = st.number_input("Valor: ")
    categoria = st.text_input("Categoria: ")

    return {
        "nome": nome,
        "valor": valor,
        "categoria": categoria
    }

def rem_nome():
    nome = st.text_input("Digite o nome do gasto a ser removido: ")
    return nome

def most_gastos(lista):
    st.table(lista)