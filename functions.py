import random

def cadastrar(dicionario):
    usuario = str(input("Usuário: "))
    senha = int(input("Senha: "))
    nome = str(input("Nome: ")).upper()
    nascimento = input("Nascimento: ").upper()
    cidade = input("Cidade: ").upper()
    uf = input("UF: ").upper()

    dicionario[random.randint(0, 999)] = {
            "usuario": usuario,
            "senha": senha,
            "nome": nome,
            "nascimento": nascimento,
            "cidade": cidade,
            "uf": uf
        }
    
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f"{chave}: {valor}\n")   

    iD = list(dicionario)[0]
    print(f"O ID {iD} com o nome de '{dicionario[iD]["usuario"]}' cadastrado com sucesso!")

def buscar():
    busca = input("Digite o ID cadastrado: ")

    with open("bd.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith(f"{busca}:"):
                return linha 

    return "Usuário não encontrado."

def atualizar():
    id_usuario = input("Digite o ID cadastrado: ")
    atualizado = False

    with open("bd.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("bd.txt", "w") as arquivo:
        for linha in linhas:
            if linha.startswith(f"{id_usuario}:"):
                print("Usuário encontrado! Insira os novos dados:")
                usuario = input("Usuário: ")
                senha = input("Senha: ")
                nome = input("Nome: ")
                nascimento = input("Nascimento: ")
                cidade = input("Cidade: ")
                uf = input("UF: ")

                nova_linha = f"{id_usuario}: {{'usuario': '{usuario}', 'senha': {senha}, 'nome': '{nome}', 'nascimento': '{nascimento}', 'cidade': '{cidade}', 'uf': '{uf}'}}\n"
                
                arquivo.write(nova_linha)
                atualizado = True
            else:
                arquivo.write(linha)

    if atualizado:
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def deletar():
    delete = input("Digite o ID de cadastro: ")
    
    with open("bd.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open("bd.txt", "w") as arquivo:
        for linha in linhas:
            if not linha.startswith(f"{delete}:"):
                arquivo.write(linha)
            else:
                print(f"Usuário {delete} removido com sucesso!")

