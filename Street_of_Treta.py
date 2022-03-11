from random import randint
import sys
import time

class Personagem:
    def __init__(self, nome, vida, pocao, atack):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack

def Inicio():
    print("* * * * * * * * * * *")
    print("*                   *")
    print("*  STREET OF TRETA  *")
    print("*                   *")
    print("* * * * * * * * * * *")
    while True:
        print("\nDeseja ler as instruções?")
        instrucoes = str(input("> "))
        if instrucoes == 'SIM' or instrucoes == 'Sim' or instrucoes == 'sim' or instrucoes == 'S' or instrucoes == 's':
            print("\n• O jogo se resume em Pedra, Papel e Tesoura.\n• Os personagem começam com 50 pontos de vida, 5 pontos de ataque e 2 poções.\n• Ao utilizar uma poção, sua vida aumenta 15 pontos.\n• Ao ganhar 2x consecutivas, o ataque passa a ser 6.\n• Ao ganhar 3x consecutivas, o ataque passa a ser 15.\n• Ao Empatar o ataque volta a seu valor inicial (5).\n• Quando um dos personagens perde, o ataque volta a seu valor inicial (5)\n• Quando o empate ocorre 3x seguidas, os dois personagens perdem 5 pontos\n")
            break
        elif instrucoes == 'NÃO' or instrucoes == 'Não' or instrucoes == 'não' or instrucoes == 'N' or instrucoes == 'n':
            print("")
            break
        else:
            print("Entrada Invalida!")
    time.sleep(0.5)

def SOT():
    while True:
        print("Deseja continuar o jogo anterior?")
        continuar = input(str("> "))
        if continuar == 'SIM' or continuar == 'Sim' or continuar == 'sim' or continuar == 'S' or continuar == 's':
            break
        elif continuar == 'NÃO' or continuar == 'Não' or continuar == 'não' or continuar == 'N' or continuar == 'n':
            Novo()
            Salvar()
            break
        else:
            print("Entrada Invalida!\n")
        
    while True:
        rodada = 0
        empate = 0
        vez_CPU = 0
        vez_jogador = 0
        
        while True:
            print("\nEscolha um personagem:")
            for i in range(len(personagem)):
                print(i+1, "-", personagem[i].nome)
            escolha_personagem1 = int(input('> '))
            if escolha_personagem1 < 1 or escolha_personagem1 > 13 or personagem[escolha_personagem1 - 1].vida <= 0:
                print("Entrada Invalida!\n")
            elif personagem[escolha_personagem1 - 1].vida <= 0:
                print("Esse personagem está morto!\n")
            else:
                print("")
                break
        
        while True:
            print("Escolha outro personagem:")
            for i in range(len(personagem)):
                print(i+1, "-", personagem[i].nome)
            escolha_personagem2 = int(input("> "))
            if escolha_personagem2 < 1 or escolha_personagem2 > 13 or personagem[escolha_personagem2 - 1].vida <= 0 or escolha_personagem1 == escolha_personagem2:
                print("Entrada Invalida!\n")
                if personagem[escolha_personagem2 - 1].vida <= 0:
                    print("Esse personagem está morto!\n")
                elif escolha_personagem1 == escolha_personagem2:
                    print("Esse personagem já foi escolhido!\n")
            else:
                print("")
                break
        
        while True:
            time.sleep(0.5)
            rodada += 1
            print("* * * * * * * *")
            print("*             *")
            print("* {:02}° Rodada  *".format(rodada))
            print("*             *")
            print("* * * * * * * *\n")
            
            while True:
                print("Escolha uma das opções:")
                print("1 - Pedra")
                print("2 - Papel")
                print("3 - Tesoura")
                print("0 - Sair")
                opcao = int(input("> "))
                if opcao < 0 or opcao > 3:
                    print("Entrada Invalida!\n")
                elif opcao == 0:
                    sys.exit()
                else:
                    break
            
            cpu = randint(1, 3)
            if cpu == 1:
                print(personagem[escolha_personagem2 - 1].nome, ": Pedra\n")
            elif cpu == 2:
                print(personagem[escolha_personagem2 - 1].nome, ": Papel\n")
            else:
                print(personagem[escolha_personagem2 - 1].nome, ": Tesoura\n")
            time.sleep(0.5)
            if opcao == 1 and cpu == 3 or opcao == 2 and cpu == 1 or opcao == 3 and cpu == 2:
                #JOGADOR GANHOU
                empate = 0
                print("Vez de", personagem[escolha_personagem1 - 1].nome,"atacar!")
                if vez_CPU == 1:
                    vez_CPU = 0
                elif vez_CPU > 1:
                    vez_CPU = 0
                    print("O ataque de", personagem[escolha_personagem2 - 1].nome,"voltou a ser", personagem[escolha_personagem2 - 1].atack, "pontos.")
                vez_jogador += 1
                if vez_jogador == 1:
                    personagem[escolha_personagem2 - 1].vida  -= personagem[escolha_personagem1 - 1].atack
                elif vez_jogador == 2:
                    personagem[escolha_personagem2 - 1].vida -= personagem[escolha_personagem1 - 1].atack + 1
                    print("\nO ataque de", personagem[escolha_personagem1 - 1].nome,"agora é de", personagem[escolha_personagem1 - 1].atack + 1,"pontos\n")
                elif vez_jogador == 3:
                    personagem[escolha_personagem2 - 1].vida -= personagem[escolha_personagem1 - 1].atack * 3
                    print("\nO ataque de", personagem[escolha_personagem1 - 1].nome,"agora é de", personagem[escolha_personagem1 - 1].atack * 3,"pontos\n")
                elif vez_jogador > 3:
                    personagem[escolha_personagem2 - 1].vida -= personagem[escolha_personagem1 - 1].atack * 3
                print("Vida", personagem[escolha_personagem2 - 1].nome,":", personagem[escolha_personagem2 - 1].vida, "\n")
                
                if personagem[escolha_personagem1 - 1].vida > 0 and personagem[escolha_personagem1 - 1].vida < 25 and personagem[escolha_personagem1 - 1].pocao > 0 and personagem[escolha_personagem2 - 1].vida > 0:
                    print("Vida", personagem[escolha_personagem1 - 1].nome,":", personagem[escolha_personagem1 - 1].vida)
                    print(personagem[escolha_personagem1 - 1].nome, "tem", personagem[escolha_personagem1 - 1].pocao, "poções\n")
                    while True:
                        print("Deseja usar uma?")
                        pocao = str(input("> "))
                        if pocao == 'SIM' or pocao == 'Sim' or pocao == 'sim' or pocao == 'S' or pocao == 's':
                            personagem[escolha_personagem1 - 1].vida += 15
                            personagem[escolha_personagem1 - 1].pocao -= 1
                            print("Vida", personagem[escolha_personagem1 - 1].nome,":", personagem[escolha_personagem1 - 1].vida)
                            print(personagem[escolha_personagem1 - 1].nome, "tem", personagem[escolha_personagem1 - 1].pocao, "poções")
                            break
                        elif pocao == 'NÃO' or pocao == 'Não' or pocao == 'não' or pocao == 'N' or pocao == 'n':
                            break
                        else:
                            print("Entrada Invalida!\n")
            
            elif opcao == cpu:
                empate += 1
                #EMPATE
                print("Empate! Tente novamente.\n")
                if empate == 3:
                    personagem[escolha_personagem1 - 1].vida = personagem[escolha_personagem1 - 1].vida - 5
                    personagem[escolha_personagem2 - 1].vida = personagem[escolha_personagem2 - 1].vida - 5
                    print("Vida", personagem[escolha_personagem1 - 1].nome,":", personagem[escolha_personagem1 - 1].vida)
                    print("Vida", personagem[escolha_personagem2 - 1].nome,":", personagem[escolha_personagem2 - 1].vida)
                if vez_CPU == 1:
                    vez_CPU = 0
                elif vez_CPU > 1:
                    vez_CPU = 0
                    print("O ataque de", personagem[escolha_personagem2 - 1].nome,"voltou a ser 5\n")
                if vez_jogador == 1:
                    vez_jogador = 0
                elif vez_jogador > 1:
                    vez_jogador = 0
                    print("O ataque de", personagem[escolha_personagem1 - 1].nome, "voltou a ser 5\n")
            
            elif cpu == 1 and opcao == 3 or cpu == 2 and opcao == 1 or cpu == 3 and opcao == 2:
                empate+=1
                #JOGADOR PERDEU!
                print("Vez de", personagem[escolha_personagem2 - 1].nome,"atacar!")
                if vez_jogador == 1:
                    vez_jogador = 0
                elif vez_jogador > 1:
                    vez_jogador = 0
                    print("O ataque de", personagem[escolha_personagem1 - 1].nome,"voltou a ser", personagem[escolha_personagem1 - 1].atack, "pontos.")
                vez_CPU += 1
                if vez_CPU  == 1:
                    personagem[escolha_personagem1 - 1].vida -= personagem[escolha_personagem2 - 1].atack
                elif vez_CPU == 2:
                    personagem[escolha_personagem1 - 1].vida -= personagem[escolha_personagem2 - 1].atack + 1
                    print("\nO ataque de", personagem[escolha_personagem2 - 1].nome,"agora é de", personagem[escolha_personagem2 - 1].atack + 1,"pontos\n")
                elif vez_CPU == 3:
                    personagem[escolha_personagem1 - 1].vida -= personagem[escolha_personagem2 - 1].atack * 3
                    print("\nO ataque de", personagem[escolha_personagem2 - 1].nome,"agora é de", personagem[escolha_personagem2 - 1].atack * 3,"pontos\n")
                elif vez_CPU > 3:
                    personagem[escolha_personagem1 - 1].vida -= personagem[escolha_personagem2 - 1].atack * 3
                print("Vida", personagem[escolha_personagem1 - 1].nome,":", personagem[escolha_personagem1 - 1].vida, "\n")

                if personagem[escolha_personagem2 - 1].vida > 0 and personagem[escolha_personagem2 - 1].vida < 25 and personagem[escolha_personagem2 - 1].pocao > 0 and personagem[escolha_personagem1 - 1].vida:
                    pocao = randint(1, 2)
                    if pocao == 1:
                        print(personagem[escolha_personagem2 - 1].nome,"usou 1 poção\n")
                        personagem[escolha_personagem2 - 1].vida += 15
                        personagem[escolha_personagem2 - 1].pocao -= 1
                        print("Vida", personagem[escolha_personagem2 - 1].nome,":", personagem[escolha_personagem2 - 1].vida)
                        print(personagem[escolha_personagem2 - 1].nome,"tem", personagem[escolha_personagem2 - 1].pocao,"poção")
                    elif pocao == 2:
                        print(personagem[escolha_personagem2 - 1].nome,"tem", personagem[escolha_personagem2 - 1].pocao,"poção")
            
            if personagem[escolha_personagem1 - 1].vida <= 0 or personagem[escolha_personagem2 - 1].vida <= 0:
                break
        if personagem[escolha_personagem1 - 1].vida <= 0:
            print(personagem[escolha_personagem1 - 1].nome, "morreu. Você perdeu!")
        elif personagem[escolha_personagem2 - 1].vida <= 0:
            print(personagem[escolha_personagem2 - 1].nome, "morreu. Você ganhou!")

        print("Rodadas Jogadas:", rodada)
        while True:
            print("Deseja salvar o jogo?")
            salvar = input(str("> "))
            
            if salvar == 'NÃO' or salvar == 'Não' or salvar == 'não' or salvar == 'n' or salvar == 'N':
                break
            elif salvar == 'SIM' or salvar == 'Sim' or salvar == 'sim' or salvar == 's' or salvar == 'S':
                Salvar()
                break
            else:
                print("Entrada Invalida!\n")

        while True:
            print("Deseja jogar novamente?")
            novamente = str(input("> "))
            if novamente == "SIM" or novamente == "Sim" or novamente == "sim" or novamente == "S" or novamente == "s":
                print("")
                break
            elif novamente == "NÃO" or novamente == "Não" or novamente == "não" or novamente == "N" or novamente == "n":
                sys.exit()
            else:
                print("Entrada Invalida!\n")
    
def Main():
    Inicio()
    Criar_personagens()
    SOT()

def Novo():
    info = open("infoPersonagens/valores_iniciais.txt", encoding="utf8")
    linha = info.readline()
    info.close()
    coluna = linha.split("|")
    vida = int(coluna[0])
    pocao = int(coluna[1])
    atack = int(coluna[2])
    for i in range(len(personagem)):
        personagem[i].vida = vida
        personagem[i].pocao = pocao
        personagem[i].atack = atack
    for i in range(len(personagem)):
        personagem[i].vida = vida
        personagem[i].pocao = pocao
        personagem[i].atack = atack

def Salvar():
    arquivo1 = open("infoPersonagens/SOT_personagens.txt", "w", encoding="utf8")
    for i in range(len(personagem)):
        nome = str(personagem[i].nome)
        vida = str(personagem[i].vida)
        pocao = str(personagem[i].pocao)
        atack = str(personagem[i].atack)
        concatenado1 = nome + "|" + vida + "|" + pocao + "|" + atack + "\n"
        arquivo1.write(concatenado1)
    arquivo1.close()

personagem = []
personagem = []

def Criar_personagens():
    arquivo1 = open("infoPersonagens/SOT_personagens.txt", "r", encoding="utf8")
    linha = arquivo1.readlines()
    for i in range(len(linha)):
        dado1 = []
        coluna = linha[i].split("|")
        nome = coluna[0]
        dado1.append(int(coluna[1]))
        dado1.append(int(coluna[2]))
        dado1.append(int(coluna[3]))
        personagem.append(Personagem(nome, dado1[0], dado1[1], dado1[2]))
    arquivo1.close()

Main()