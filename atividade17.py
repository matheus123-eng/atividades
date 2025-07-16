import random
import string

def gerar_senha(nivel):
    if nivel == "fraca":
        caracteres = string.ascii_lowercase
    elif nivel == "media":
        caracteres = string.ascii_letters + string.digits
    elif nivel == "forte":
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Nível inválido."

    return ''.join(random.choice(caracteres) for _ in range(12))

nivel = input("Escolha o nível da senha (fraca, media, forte): ")
print("Senha gerada:", gerar_senha(nivel))
