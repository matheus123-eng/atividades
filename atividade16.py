palavra_secreta = "python"
tentativas = []
erros = 0

while True:
    exibida = ''.join([letra if letra in tentativas else '_' for letra in palavra_secreta])
    print(exibida)

    if exibida == palavra_secreta:
        print("Parabéns, você venceu!")
        break

    tentativa = input("Tente uma letra: ").lower()
    if tentativa in tentativas:
        print("Você já tentou essa letra.")
    elif tentativa in palavra_secreta:
        tentativas.append(tentativa)
    else:
        tentativas.append(tentativa)
        erros += 1
        print(f"Erros: {erros}/6")

    if erros >= 6:
        print("Você perdeu! A palavra era:", palavra_secreta)
        break
