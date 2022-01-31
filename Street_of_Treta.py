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
    print("*  STRET OF TRETA   *")
    print("*                   *")
    print("* * * * * * * * * * *")
    while True:
        print("\nDeseja ler as instruções?")
        instrucoes = str(input("> "))
        if instrucoes == 'SIM' or instrucoes == 'Sim' or instrucoes == 'sim' or instrucoes == 'S' or instrucoes == 's':
            print("\nO Jogador começa com 50 pontos de vida e 5 de ataque. O jogo se resume em Pedra, Papel e Tesoura.")
            print("Assim que você ganha no Pedra, Papel e Tesoura, você ataca, quando você ganha 2x seguidas, seu")
            print("ataque soma +1, se ganhar 3x seguidas, seu ataque inicial multiplica por 3. O mesmo acontece com a")
            print("CPU, se ele ganhar 2x, ataque +1, se 3x ataque *3. Quando empata, seu ataque zera, volta ao estado")
            print("inicial. Quando você toma dano, você pode escolher se quer tomar a Poção. Você tem direito a 2 poções,")
            print("cada uma restaura 15 pontos de vida.\n")
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
        vez_CPU = 0
        vez_jogador = 0
        
        while True:
            print("Escolha um Heroi:")
            for i in range(len(heroi)):
                print(i+1, "-", heroi[i].nome)
            escolha_heroi = int(input('> '))
            if escolha_heroi < 1 or escolha_heroi > 10:
                print("Entrada Invalida!\n")
            else:
                print("")
                break
        
        while True:
            print("Escolha um Vilão:")
            for i in range(len(vilao)):
                print(i+1, "-", vilao[i].nome)
            escolha_vilao = int(input("> "))
            if escolha_vilao < 1 or escolha_vilao > 4:
                print("Entrada Invalida!\n")
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
                print(vilao[escolha_vilao - 1].nome, ": Pedra\n")
            elif cpu == 2:
                print(vilao[escolha_vilao - 1].nome, ": Papel\n")
            else:
                print(vilao[escolha_vilao - 1].nome, ": Tesoura\n")
            time.sleep(0.5)
            if opcao == 1 and cpu == 3 or opcao == 2 and cpu == 1 or opcao == 3 and cpu == 2:
                #JOGADOR GANHOU
                print("Vez de", heroi[escolha_heroi - 1].nome,"atacar!")
                if vez_CPU == 1:
                    vez_CPU = 0
                elif vez_CPU > 1:
                    vez_CPU = 0
                    print("O ataque de", vilao[escolha_vilao - 1].nome,"voltou a ser", vilao[escolha_vilao - 1].atack, "pontos.")
                vez_jogador += 1
                if vez_jogador == 1:
                    vilao[escolha_vilao - 1].vida  -= heroi[escolha_heroi - 1].atack
                elif vez_jogador == 2:
                    vilao[escolha_vilao - 1].vida -= heroi[escolha_heroi - 1].atack + 1
                    print("\nO ataque de", heroi[escolha_heroi - 1].nome,"agora é de", heroi[escolha_heroi - 1].atack + 1,"pontos\n")
                elif vez_jogador == 3:
                    vilao[escolha_vilao - 1].vida -= heroi[escolha_heroi - 1].atack * 3
                    print("\nO ataque de", heroi[escolha_heroi - 1].nome,"agora é de", heroi[escolha_heroi - 1].atack * 3,"pontos\n")
                elif vez_jogador > 3:
                    vilao[escolha_vilao - 1].vida -= heroi[escolha_heroi - 1].atack * 3
                print("Vida", vilao[escolha_vilao - 1].nome,":", vilao[escolha_vilao - 1].vida, "\n")
                
                if heroi[escolha_heroi - 1].vida > 0 and heroi[escolha_heroi - 1].vida < 25 and heroi[escolha_heroi - 1].pocao > 0 and vilao[escolha_vilao - 1].vida > 0:
                    print("Vida", heroi[escolha_heroi - 1].nome,":", heroi[escolha_heroi - 1].vida)
                    print(heroi[escolha_heroi - 1].nome, "tem", heroi[escolha_heroi - 1].pocao, "poções\n")
                    while True:
                        print("Deseja usar uma?")
                        pocao = str(input("> "))
                        if pocao == 'SIM' or pocao == 'Sim' or pocao == 'sim' or pocao == 'S' or pocao == 's':
                            heroi[escolha_heroi - 1].vida += 15
                            heroi[escolha_heroi - 1].pocao -= 1
                            print("Vida", heroi[escolha_heroi - 1].nome,":", heroi[escolha_heroi - 1].vida)
                            print(heroi[escolha_heroi - 1].nome, "tem", heroi[escolha_heroi - 1].pocao, "poções")
                            break
                        elif pocao == 'NÃO' or pocao == 'Não' or pocao == 'não' or pocao == 'N' or pocao == 'n':
                            break
                        else:
                            print("Entrada Invalida!\n")
            
            elif opcao == cpu:
                #EMPATE
                print("Empate! Tente novamente.\n")
                if vez_CPU == 1:
                    vez_CPU = 0
                elif vez_CPU > 1:
                    vez_CPU = 0
                    print("O ataque de", vilao[escolha_vilao - 1].nome,"voltou a ser 5\n")
                if vez_jogador == 1:
                    vez_jogador = 0
                elif vez_jogador > 1:
                    vez_jogador = 0
                    print("O ataque de", heroi[escolha_heroi - 1].nome, "voltou a ser 5\n")
            
            elif cpu == 1 and opcao == 3 or cpu == 2 and opcao == 1 or cpu == 3 and opcao == 2:
                #JOGADOR PERDEU!
                print("Vez de", vilao[escolha_vilao - 1].nome,"atacar!")
                if vez_jogador == 1:
                    vez_jogador = 0
                elif vez_jogador > 1:
                    vez_jogador = 0
                    print("O ataque de", heroi[escolha_heroi - 1].nome,"voltou a ser", heroi[escolha_heroi - 1].atack, "pontos.")
                vez_CPU += 1
                if vez_CPU  == 1:
                    heroi[escolha_heroi - 1].vida -= vilao[escolha_vilao - 1].atack
                elif vez_CPU == 2:
                    heroi[escolha_heroi - 1].vida -= vilao[escolha_vilao - 1].atack + 1
                    print("\nO ataque de", vilao[escolha_vilao - 1].nome,"agora é de", vilao[escolha_vilao - 1].atack + 1,"pontos\n")
                elif vez_CPU == 3:
                    heroi[escolha_heroi - 1].vida -= vilao[escolha_vilao - 1].atack * 3
                    print("\nO ataque de", vilao[escolha_vilao - 1].nome,"agora é de", vilao[escolha_vilao - 1].atack * 3,"pontos\n")
                elif vez_CPU > 3:
                    heroi[escolha_heroi - 1].vida -= vilao[escolha_vilao - 1].atack * 3
                print("Vida", heroi[escolha_heroi - 1].nome,":", heroi[escolha_heroi - 1].vida, "\n")

                if vilao[escolha_vilao - 1].vida > 0 and vilao[escolha_vilao - 1].vida < 25 and vilao[escolha_vilao - 1].pocao > 0 and heroi[escolha_heroi - 1].vida:
                    pocao = randint(1, 2)
                    if pocao == 1:
                        print(vilao[escolha_vilao - 1].nome,"usou 1 poção\n")
                        vilao[escolha_vilao - 1].vida += 15
                        vilao[escolha_vilao - 1].pocao -= 1
                        print("Vida", vilao[escolha_vilao - 1].nome,":", vilao[escolha_vilao - 1].vida)
                        print(vilao[escolha_vilao - 1].nome,"tem", vilao[escolha_vilao - 1].pocao,"poção")
                    elif pocao == 2:
                        print(vilao[escolha_vilao - 1].nome,"tem", vilao[escolha_vilao - 1].pocao,"poção")
            
            if heroi[escolha_heroi - 1].vida <= 0 or vilao[escolha_vilao - 1].vida <= 0:
                break
        if heroi[escolha_heroi - 1].vida <= 0:
            print(heroi[escolha_heroi - 1].nome, "morreu. Você perdeu!")
        elif vilao[escolha_vilao - 1].vida <= 0:
            print(vilao[escolha_vilao - 1].nome, "morreu. Você ganhou!")

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
    for i in range(len(heroi)):
        heroi[i].vida = vida
        heroi[i].pocao = pocao
        heroi[i].atack = atack
    for i in range(len(vilao)):
        vilao[i].vida = vida
        vilao[i].pocao = pocao
        vilao[i].atack = atack

def Salvar():
    arquivo1 = open("infoPersonagens/SOT_heroi.txt", "w", encoding="utf8")
    for i in range(len(heroi)):
        nome = str(heroi[i].nome)
        vida = str(heroi[i].vida)
        pocao = str(heroi[i].pocao)
        atack = str(heroi[i].atack)
        concatenado1 = nome + "|" + vida + "|" + pocao + "|" + atack + "\n"
        arquivo1.write(concatenado1)
    arquivo1.close()
    arquivo2 = open("infoPersonagens/SOT_vilao.txt", "w", encoding="utf8")
    for i in range(len(vilao)):
        nome = str(vilao[i].nome)
        vida = str(vilao[i].vida)
        pocao = str(vilao[i].pocao)
        atack = str(vilao[i].atack)
        concatenado2 = nome + "|" + vida + "|" + pocao + "|" + atack + "\n"
        arquivo2.write(concatenado2)
    arquivo2.close()    

heroi = []
vilao = []
def Criar_personagens():
    arquivo1 = open("infoPersonagens/SOT_heroi.txt", "r", encoding="utf8")
    linha = arquivo1.readlines()
    for i in range(len(linha)):
        dado1 = []
        coluna = linha[i].split("|")
        nome = coluna[0]
        dado1.append(int(coluna[1]))
        dado1.append(int(coluna[2]))
        dado1.append(int(coluna[3]))
        heroi.append(Personagem(nome, dado1[0], dado1[1], dado1[2]))
    arquivo1.close()

    arquivo2 = open("infoPersonagens/SOT_vilao.txt", "r", encoding="utf8")
    linha = arquivo2.readlines()
    for i in range(len(linha)):
        dado2 = []
        coluna = linha[i].split("|")
        nome = coluna[0]
        dado2.append(int(coluna[1]))
        dado2.append(int(coluna[2]))
        dado2.append(int(coluna[3]))
        vilao.append(Personagem(nome, dado2[0], dado2[1], dado2[2]))
    arquivo2.close()

Main()