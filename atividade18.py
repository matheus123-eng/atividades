import random

def simular_dado(n):
    frequencias = {i: 0 for i in range(1, 7)}
    for _ in range(n):
        face = random.randint(1, 6)
        frequencias[face] += 1
    return frequencias

vezes = int(input("Quantas vezes deseja lançar o dado? "))
resultado = simular_dado(vezes)
print("Frequências:", resultado)
