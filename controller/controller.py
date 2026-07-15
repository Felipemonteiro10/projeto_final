from model import model
from view import view

def iniciar():
    print("Bem-vindo ao sistema de gastos!")
    opcao = -67

    while opcao != 0:
        view.mostrar_menu()
        opcao = int(input("Escolha: "))

        if opcao == 0:
            print("Saindo do sistema...")
            break

        elif opcao == 1:
            gasto = view.ler_gasto()
            model.adicionar(gasto)

        elif opcao == 2:
            view.mostrar_gastos(model.listar())

        elif opcao == 3:
            print("Total:", model.total())

        elif opcao == 4:
            nome = view.rem_nome()
            model.remover(nome)

        elif opcao == 5:
            valor = view.oq_tenho()
            Sobrou=valor-model.total()
            if Sobrou>0:
                print(f"Você ainda tem R$ {Sobrou}")
            else:
                print(f"Você está devendo R$ {Sobrou}")

        else:
            print("Não tem essa opção")
