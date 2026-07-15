gastos = []

def add(gasto):
    gastos.append(gasto)

def list():
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
            break
        
def quanto_tenho():
    return total()  