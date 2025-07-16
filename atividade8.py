import random

numero_secreto = random.randint(1, 10)
palpite = int(input("Adivinhe o número entre 1 e 10: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou! 🎉")
else:
    print(f"Errou! O número era {numero_secreto}.")

#Fatorial de um Número
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")

