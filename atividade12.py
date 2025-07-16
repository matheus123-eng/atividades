entrada = input("Digite números separados por espaço: ")
lista = [int(x) for x in entrada.split()]
unicos = list(set(lista))
print(f"Lista sem duplicatas: {unicos}")
