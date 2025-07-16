clientes = {}

while True:
    print("\n1 - Adicionar\n2 - Visualizar\n3 - Remover\n4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        clientes[nome] = email

    elif opcao == "2":
        for nome, email in clientes.items():
            print(f"{nome}: {email}")

    elif opcao == "3":
        nome = input("Nome a remover: ")
        clientes.pop(nome, None)

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")
