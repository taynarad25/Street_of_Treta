from random import randint
import sys
import time

personagem = []
class Personagem:
    def __init__(self, nome, vida, pocao, atack, nivel, ganho):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack
        self.nivel = nivel
        self.ganho = ganho

def Inicio():
    print("* * * * * * * * * * *")
    print("*                   *")
    print("*  STREET OF TRETA  *")
    print("*                   *")
    print("* * * * * * * * * * *")
    while True:
        print("\nDeseja ler as instruções?")
        try:
            instrucoes = str(input("> "))
        except:
            print("Entrada Invalida!")
        if instrucoes == 'SIM' or instrucoes == 'Sim' or instrucoes == 'sim' or instrucoes == 'S' or instrucoes == 's':
            print("\nINSTRUÇÕES INICIAIS\n")
            print("• O jogo se resume em Pedra, Papel e Tesoura.")
            print("• Os personagem começam no nível 1.")
            print("• Ao utilizar uma poção, sua vida aumenta 15 pontos.")
            print("• Você poderá usar uma poção quando sua vida for menor que 25 pontos.")
            print("• Ao ganhar 2x consecutivas, o ataque inicial passa a ser somado a 1.")
            print("• Ao ganhar 3x consecutivas, o ataque inicial passa a ser somado a 10.")
            print("• Ao Empatar o ataque volta ao valor inicial.")
            print("• Ao Empatar 3x os dois personagens perdem 5 pontos de vida.")
            print("• Quando um dos personagens perde, o ataque volta a seu valor inicial")
            print("\nMUDANÇA DE NÍVEL\n")
            print("• Se um personagem de nível 1 sobreviver a 2 batalhas, ele avança para o nível 2")
            print("• Se um personagem de nível 2 sobreviver a 3 batalhas, ele avança para o nível 3")
            print("• Se um personagem de nível 3 sobreviver a 4 batalhas, ele avança para o nível 4")
            print("• Se um personagem de nível 4 sobreviver a 5 batalhas, ele avança para o nível 5")
            print("\nNÍVEIS\n")
            print("• Nível 1\n  > Vida: 50\n  > Poção: 2\n  > Ataque: 5\n")
            print("• Nível 2\n  > Vida: 55\n  > Poção: 2\n  > Ataque: 6\n")
            print("• Nível 3\n  > Vida: 60\n  > Poção: 3\n  > Ataque: 7\n")
            print("• Nível 4\n  > Vida: 65\n  > Poção: 3\n  > Ataque: 8\n")
            print("• Nível 5\n  > Vida: 70\n  > Poção: 4\n  > Ataque: 9\n")
            print("• Assim por diante. A cada nível a vida aumenta 5 pontos e o ataque 1 ponto. E a cada 2 níveis a poção aumenta 1 ponto.")
            break
        elif instrucoes == 'NÃO' or instrucoes == 'Não' or instrucoes == 'não' or instrucoes == 'N' or instrucoes == 'n':
            print("")
            break
        else:
            print("Entrada Invalida!")
    time.sleep(0.5)

def Atualizar_vida():
    for i in range(len(personagem)):
        if personagem[i].vida > 0 and personagem[i].nivel >= 1 and personagem[i].vida < 50 + ((personagem[i].nivel - 1) * 5):
            personagem[i].vida = 50 + ((personagem[i].nivel - 1) * 5)

def Atualizar_atack():
    for i in range(len(personagem)):
        if personagem[i].atack > 0 and personagem[i].nivel >= 1 and personagem[i].atack < 5 + (personagem[i].nivel - 1):
            personagem[i].atack = 5 + (personagem[i].nivel - 1)

def Atualizar_pocao():
    for i in range(len(personagem)):
        if personagem[i].vida > 0 and personagem[i].nivel <= 1 and personagem[i].pocao != 2:
           personagem[i].pocao = 2
        elif personagem[i].vida <= 0:
            continue
        elif personagem[i].vida > 0 and personagem[i].nivel > 1 and personagem[i].pocao < 2 + (personagem[i].nivel - 1) // 2:
            personagem[i].pocao = 2 + (personagem[i].nivel - 1) // 2

def Escolha_personagem(escolha):
    while True:
        print("\nEscolha um personagem:")
        for i in range(len(personagem)):
            print(i+1, "-", personagem[i].nome)
        try:
            escolha[0] = int(input('> '))
        except:
            print("Entrada Invalida!")

        if escolha[0] < 1 or escolha[0] > 14:
            print("Entrada Invalida!\n")
        elif personagem[escolha[0] - 1].vida <= 0:
            print("\nNão é possível escolher",personagem[escolha[0] - 1].nome)
        else:
            print("")
            break

    while True:
        print("\nEscolha um personagem:")
        for i in range(len(personagem)):
            print(i+1, "-", personagem[i].nome)
        try:
            escolha[1] = int(input('> '))
        except:
            print("Entrada Invalida!")

        if escolha[1] < 1 or escolha[1] > 14:
            print("Entrada Invalida!\n")
        elif personagem[escolha[1] - 1].vida <= 0 or escolha[1] == escolha[0]:
            print("\nNão é possível escolher",personagem[escolha[1] - 1].nome)
        else:
            print("")
            return escolha


def SOT():
    while True:
        print("Deseja continuar o jogo anterior?")
        try:
            continuar = input(str("> "))
        except:
            print("Entrada Invalida!")
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
        escolha = [0, 0]

        Escolha_personagem(escolha)

        while True:
            time.sleep(0.5)
            rodada += 1
            print("* * * * * * * *")
            print("*             *")
            print("* {:02}° Rodada  *".format(rodada))
            print("*             *")
            print("* * * * * * * *\n")

            while True:
                print("\nEscolha uma das opções:")
                print("1 - Pedra")
                print("2 - Papel")
                print("3 - Tesoura")
                print("0 - Sair")
                try:
                    opcao = int(input("> "))
                except:
                    print("Entrada Invalida!")
                    continue

                if opcao < 0 or opcao > 3:
                    print("Entrada Invalida!\n")
                elif opcao == 0:
                    sys.exit()
                else:
                    break

            cpu = randint(1, 3)
            if cpu == 1:
                print(personagem[escolha[1] - 1].nome, ": Pedra\n")
            elif cpu == 2:
                print(personagem[escolha[1] - 1].nome, ": Papel\n")
            else:
                print(personagem[escolha[1] - 1].nome, ": Tesoura\n")
            time.sleep(0.5)
            if opcao == 1 and cpu == 3 or opcao == 2 and cpu == 1 or opcao == 3 and cpu == 2:
                #JOGADOR GANHOU
                print("Vez de", personagem[escolha[0] - 1].nome,"atacar!")
                empate = 0
                if vez_CPU == 1:
                    vez_CPU = 0
                elif vez_CPU > 1:
                    vez_CPU = 0
                    print("O ataque de", personagem[escolha[1] - 1].nome,"voltou a ser", personagem[escolha[1] - 1].atack, "pontos.")
                vez_jogador += 1
                if vez_jogador == 1:
                    personagem[escolha[1] - 1].vida  -= personagem[escolha[0] - 1].atack
                elif vez_jogador == 2:
                    personagem[escolha[1] - 1].vida -= personagem[escolha[0] - 1].atack + 1
                    print("\nO ataque de", personagem[escolha[0] - 1].nome,"agora é de", personagem[escolha[0] - 1].atack + 1,"pontos\n")
                elif vez_jogador == 3:
                    personagem[escolha[1] - 1].vida -= personagem[escolha[0] - 1].atack + 10
                    print("\nO ataque de", personagem[escolha[0] - 1].nome,"agora é de", personagem[escolha[0] - 1].atack + 10,"pontos\n")
                elif vez_jogador > 3:
                    personagem[escolha[1] - 1].vida -= personagem[escolha[0] - 1].atack + 10
                print("Vida", personagem[escolha[1] - 1].nome,":", personagem[escolha[1] - 1].vida, "\n")

                if personagem[escolha[0] - 1].vida > 0 and personagem[escolha[0] - 1].vida < 25 and personagem[escolha[0] - 1].pocao > 0 and personagem[escolha[1] - 1].vida > 0:
                    print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida)
                    print(personagem[escolha[0] - 1].nome, "tem", personagem[escolha[0] - 1].pocao, "poções\n")
                    while True:
                        print("Deseja usar uma?")
                        try:
                            pocao = str(input("> "))
                        except:
                            print("Entrada Invalida!")
                        if pocao == 'SIM' or pocao == 'Sim' or pocao == 'sim' or pocao == 'S' or pocao == 's':
                            personagem[escolha[0] - 1].vida += 15
                            personagem[escolha[0] - 1].pocao -= 1
                            print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida)
                            print(personagem[escolha[0] - 1].nome, "tem", personagem[escolha[0] - 1].pocao, "poções")
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
                    personagem[escolha[0] - 1].vida = personagem[escolha[0] - 1].vida - 5
                    personagem[escolha[1] - 1].vida = personagem[escolha[1] - 1].vida - 5
                    print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida)
                    print("Vida", personagem[escolha[1] - 1].nome,":", personagem[escolha[1] - 1].vida)
                    empate = 0
                if vez_CPU == 1:
                    vez_CPU = 0
                elif vez_CPU > 1:
                    vez_CPU = 0
                    print("O ataque de", personagem[escolha[1] - 1].nome,"voltou a ser", personagem[escolha[0] - 1].atack, "pontos.")
                if vez_jogador == 1:
                    vez_jogador = 0
                elif vez_jogador > 1:
                    vez_jogador = 0
                    print("O ataque de", personagem[escolha[0] - 1].nome,"voltou a ser", personagem[escolha[0] - 1].atack, "pontos.")

            elif cpu == 1 and opcao == 3 or cpu == 2 and opcao == 1 or cpu == 3 and opcao == 2:
                #JOGADOR PERDEU!
                print("Vez de", personagem[escolha[1] - 1].nome,"atacar!")
                empate = 0
                if vez_jogador == 1:
                    vez_jogador = 0
                elif vez_jogador > 1:
                    vez_jogador = 0
                    print("O ataque de", personagem[escolha[0] - 1].nome,"voltou a ser", personagem[escolha[0] - 1].atack, "pontos.")
                vez_CPU += 1
                if vez_CPU  == 1:
                    personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack
                elif vez_CPU == 2:
                    personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack + 1
                    print("\nO ataque de", personagem[escolha[1] - 1].nome,"agora é de", personagem[escolha[1] - 1].atack + 1,"pontos\n")
                elif vez_CPU == 3:
                    personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack + 10
                    print("\nO ataque de", personagem[escolha[1] - 1].nome,"agora é de", personagem[escolha[1] - 1].atack + 10,"pontos\n")
                elif vez_CPU > 3:
                    personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack + 10
                print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida, "\n")

                if personagem[escolha[1] - 1].vida > 0 and personagem[escolha[1] - 1].vida < 25 and personagem[escolha[1] - 1].pocao > 0 and personagem[escolha[0] - 1].vida > 0:
                    pocao = randint(1, 2)
                    if pocao == 1:
                        print(personagem[escolha[1] - 1].nome,"usou 1 poção\n")
                        personagem[escolha[1] - 1].vida += 15
                        personagem[escolha[1] - 1].pocao -= 1
                        print("Vida", personagem[escolha[1] - 1].nome,":", personagem[escolha[1] - 1].vida)
                        print(personagem[escolha[1] - 1].nome,"tem", personagem[escolha[1] - 1].pocao,"poção")
                    elif pocao == 2:
                        print(personagem[escolha[1] - 1].nome,"tem", personagem[escolha[1] - 1].pocao,"poção")

            if personagem[escolha[0] - 1].vida <= 0 or personagem[escolha[1] - 1].vida <= 0:
                break
        if personagem[escolha[0] - 1].vida <= 0:
            print(personagem[escolha[0] - 1].nome, "morreu. Você perdeu!")
            personagem[escolha[1] - 1].ganho += 1
            personagem[escolha[0] - 1].ganho = 0
        elif personagem[escolha[1] - 1].vida <= 0:
            print(personagem[escolha[1] - 1].nome, "morreu. Você ganhou!")
            personagem[escolha[0] - 1].ganho += 1
            personagem[escolha[1] - 1].ganho = 0

        print("Rodadas Jogadas:", rodada)

        Subir_nivel()

        while True:
            print("Deseja salvar o jogo?")
            try:
                salvar = input(str("> "))
            except:
                print("Entrada Invalida!")
            if salvar == 'NÃO' or salvar == 'Não' or salvar == 'não' or salvar == 'n' or salvar == 'N':
                break
            elif salvar == 'SIM' or salvar == 'Sim' or salvar == 'sim' or salvar == 's' or salvar == 'S':
                Salvar()
                break
            else:
                print("Entrada Invalida!\n")

        while True:
            print("Deseja jogar novamente?")
            try:
                novamente = str(input("> "))
            except:
                print("Entrada Invalida!")
            if novamente == "SIM" or novamente == "Sim" or novamente == "sim" or novamente == "S" or novamente == "s":
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
    nivel = int(coluna[3])
    ganho = int(coluna[4])
    for i in range(len(personagem)):
        personagem[i].vida = vida
        personagem[i].pocao = pocao
        personagem[i].atack = atack
        personagem[i].nivel = nivel
        personagem[i].ganho = ganho

def Salvar():
    arquivo = open("infoPersonagens/SOT_personagens.txt", "w", encoding="utf8")
    for i in range(len(personagem)):
        nome = str(personagem[i].nome)
        vida = str(personagem[i].vida)
        pocao = str(personagem[i].pocao)
        atack = str(personagem[i].atack)
        nivel = str(personagem[i].nivel)
        ganho = str(personagem[i].ganho)
        concatenado = nome + "|" + vida + "|" + pocao + "|" + atack + "|" + nivel + "|" + ganho +"\n"
        arquivo.write(concatenado)
    arquivo.close()

def Renovar_personagens():
    arquivo = open("infoPersonagens/SOT_personagens.txt", "r", encoding="utf8")
    linha = arquivo.readlines()
    for i in range(len(personagem)):
        coluna = linha[i].split("|")
        personagem[i].nome = coluna[0]
        personagem[i].vida = int(coluna[1])
        personagem[i].pocao = int(coluna[2])
        personagem[i].atack = int(coluna[3])
        personagem[i].nivel = int(coluna[4])
        personagem[i].ganho = int(coluna[5])
    arquivo.close()

def Criar_personagens():
    arquivo = open("infoPersonagens/SOT_personagens.txt", "r", encoding="utf8")
    linha = arquivo.readlines()
    for i in range(len(linha)):
        dado = []
        coluna = linha[i].split("|")
        nome = coluna[0]
        dado.append(int(coluna[1]))
        dado.append(int(coluna[2]))
        dado.append(int(coluna[3]))
        dado.append(int(coluna[4]))
        dado.append(int(coluna[5]))
        personagem.append(Personagem(nome, dado[0], dado[1], dado[2], dado[3], dado[4]))
    arquivo.close()

def Subir_nivel():
    for i in range(len(personagem)):
        if personagem[i].ganho >= personagem[i].nivel:
            personagem[i].nivel += 1
            print(personagem[i].nome, "subiu para o nivel", personagem[i].nivel, "\n")
    Atualizar_pocao()
    Atualizar_atack()
    Atualizar_vida()

Main()