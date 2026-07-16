gastos = []

def add(gasto):
    gastos.append(gasto)

def listar():
    return gastos

def total():
    soma = 0
    for gasto in gastos:
        soma += gasto["valor"]
    return soma

def remover(nome):
    for gasto in gastos:
        if gasto["nome"] == nome:
            gastos.remove(gasto)
            return True
    return False

def quanto_tenho(valor):
    return valor - total()  