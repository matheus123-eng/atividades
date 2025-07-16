with open("numeros.txt", "r") as arquivo:
    numeros = [float(linha.strip()) for linha in arquivo if linha.strip().isdigit() or '.' in linha]

media = sum(numeros) / len(numeros)
print(f"Média dos números: {media}")
