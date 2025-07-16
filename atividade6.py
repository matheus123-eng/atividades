#Contador de Vogais
frase = input("Digite uma frase: ")
contador = 0

for letra in frase:
    if letra.lower() in "aeiou":
        contador += 1

print("Quantidade de vogais:", contador)