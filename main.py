print("Iniciando o sistema...")

import random
from Python.CRUD.functions import *
usuarios = {}

while True:
    resposta = int(input('''
                         Opções do sistema:
                         1. Cadastrar
                         2. Buscar
                         3. Atualizar
                         4. Deletar
                         5. Sair
                         R: '''))
    
    if resposta == 1:
        cadastrar(usuarios)

    elif resposta == 2:
        print(buscar())

    elif resposta == 3:
        atualizar()

    elif resposta == 4:
        deletar(usuarios)

    elif resposta == 5:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")