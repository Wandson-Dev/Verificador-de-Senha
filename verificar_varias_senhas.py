import time
import re
import json


from verificar_senha import avaliar_forca_senha

def verificar_senhas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

            try:
                senhas = json.loads(conteudo)
            except json.JSONDecodeError:
                senhas = conteudo.strip().split('\n')

            for senha in senhas:
                print("\n")
                print(f"Analisando a senha: {senha}")
                time.sleep(0.1)
                resultado = avaliar_forca_senha(senha)
                print(resultado)
                time.sleep(0.1)

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo com as senhas: ")
    print("Fazendo a Verificação:")
    time.sleep(2.0)
    verificar_senhas_arquivo(nome_arquivo)