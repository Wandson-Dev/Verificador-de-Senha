import time
import re

def verificar_forca_senha(senha):
    pontuacao = 0

    comprimento = len(senha)
    pontuacao += min(comprimento, 16) * 2

    caracteres_especiais = set("!@#$%^&*()_+[]{}|;:'\"<>,.?~")
    pontuacao += len([char for char in senha if char in caracteres_especiais]) * 5

    if any(char.islower() for char in senha) and any(char.isupper() for char in senha):
        pontuacao += 20

    if any(char.isdigit() for char in senha):
        pontuacao += 15

    sequencias = re.findall(r'(abc|123|xyz)', senha, re.IGNORECASE)
    pontuacao -= len(sequencias) * 15

    caracteres_repetidos = re.findall(r'(.)\1', senha)
    pontuacao -= len(caracteres_repetidos) * 5

    senhas_comuns = ["password", "123456", "qwerty", "abc123"]
    if senha.lower() in senhas_comuns:
        pontuacao -= 50

    pontuacao = max(0, pontuacao)
    pontuacao = min(100, pontuacao)

    return pontuacao

def avaliar_forca_senha(senha):
    pontuacao = verificar_forca_senha(senha)
    if pontuacao >= 80:
        return f"Sua senha é MUITO FORTE ({pontuacao}% seguro)."
    elif pontuacao >= 60:
        return f"Sua senha é FORTE ({pontuacao}% seguro)."
    elif pontuacao >= 40:
        return f"Sua senha é RAZOÁVEL ({pontuacao}% seguro)."
    else:
        return f"Sua senha é FRACA ({pontuacao}% seguro). Tente uma senha mais segura."

if __name__ == "__main__":
    senha = input("Digite a senha para verificar a força: ")
    time.sleep(1)
    resultado = avaliar_forca_senha(senha)
    time.sleep(1)
    print(resultado)