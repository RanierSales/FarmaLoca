import os
import time
remedios = []

def cadastroDeRemedios(nomeDoRemedio, tipoDeRemedio, statusDoRemedio):
    os.system("cls")
    remedio = []
    remedio.append(nomeDoRemedio)
    remedio.append(tipoDeRemedio)
    remedio.append(statusDoRemedio)
    remedios.append(remedio)
    time.sleep(1)
    print("""
        =================================
        Remedio cadastrado com sucesso!!!
        =================================""")
        


def alterarStatus(nomeDoRemedio, statusParaAlterar):
    os.system("cls")
    retorno = 0
    for i in range(len(remedios)):
        if remedios[i][0] == nomeDoRemedio: 
            remedios[i][2] = statusParaAlterar
            print(f"{nomeDoRemedio} alterado status para {statusParaAlterar}")
            time.sleep(1)
        else: 
            retorno += 1
        if retorno == len(remedios):
            print("Remedio não encontrado no sistema!")
            time.sleep(1)


def exibirRemedios():
    for i in range(len(remedios)):
        print(f"""
        Remedio: {remedios[i][0]}
        Tipo de Remedio: {remedios[i][1]}
        Status do Remedio: {remedios[i][2]}""")
        time.sleep(0.5)



def exibirOpcoes():
    print("""
█▀▀ ▄▀█ █▀█ █▀▄▀█ ▄▀█ █░░ █▀█ █▀▀ ▄▀█
█▀░ █▀█ █▀▄ █░▀░█ █▀█ █▄▄ █▄█ █▄▄ █▀█ \n""")
    print("1. Cadastrar remédios")
    print("2. Listar remédios")
    print("3. Alterar estado do remedio")
    print("4. Sair")
    option = int(input("Digite uma opção: "))
    return option 


escolha = exibirOpcoes()
while escolha != 4:
    if escolha == 1:
        nome = input("Digite o nome do Remédio: ")
        tipo = input("Digite o tipo do Remédio: ")
        status = input("Dgitie o status desse Remédio: ")
        cadastroDeRemedios(nome, tipo, status)
    elif escolha == 2: 
        print("""
        ==============================
        Lista de Remedios cadastrados:
        ==============================
        """)
        exibirRemedios()
    elif escolha == 3: 
        nomeR = input("Digite o nome do Remédio para troca: ")
        statusParAlt = input("Digite o novo status do Remédio: ")
        alterarStatus(nomeR, statusParAlt)
    elif escolha != 4: 
        print("Opção invalida!!!!")
    
    escolha = exibirOpcoes()

print("Obrigado pela preferencia, volte sempre!!!")
