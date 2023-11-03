# Verificador de Senha

Com este script, você consegue testar a segurança de uma ou várias senhas através de vários métodos usando Python, de forma simples e rápida.

## Como Funciona?

Através do regex (Python), ele verifica sua senha considerando caixa, tamanho, caracteres especiais, etc.

## Verifica Vulnerabilidade a Brute-force

Fiz também um sistema simples que verifica se sua senha é fácil ou difícil de ser quebrada com ataques de Brute-force.

## Sistema de Porcentagem

Fiz também um sistema bastante básico de porcentagem para calcular a vulnerabilidade da sua senha.

## Verificar uma ou mais senhas

Fiz dois arquivos, um que verifica apenas uma senha (`verificar_senha.py`) e outro que verifica várias senhas em massa (`verificar_varias_senhas.py`). Você define um arquivo com as senhas uma abaixo da outra ou um array (JSON) com as senhas e ao script perguntar, você determina o nome do arquivo.

## Como Baixar (Termux)

Para baixar no Termux, digite:
```bash
termux-setup-storage
cd --
pkg install git -y
pkg install python -y
git clone https://github.com/Wandson-Dev/Verificador-de-Senha
ls
```

Para abrir:
```bash
sempre que quiser abrir o script, digite:
cd --
cd Verificador-de-Senha
ls
python3 verificar_senha.py ou python3 verificar_varias_senhas.py
```
