def mostrar_menu():
    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Ver total")
    print("4 - Remover gasto")
    print("5 - Quanto tenho?")
    print("0 - Sair")

def oq_tenho():
    print("Quanto você tem na carteira?")
    return float(input("Digite o valor: "))

def ler_gasto():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")

    return {
        "nome": nome,
        "valor": valor,
        "categoria": categoria
    }

def mostrar_gastos(lista):
    for gasto in lista:
        print(gasto)

def rem_nome():
    nome = input("Digite o nome do gasto a ser removido: ")
    return nome