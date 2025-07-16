#Calcule a Soma de uma Lista
entrada = input("Digite os números separados por espaço: ")
lista = [int(num) for num in entrada.split()]
print(f"A soma da lista é: {sum(lista)}")
