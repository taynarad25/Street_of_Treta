from random import randint

class Personagem:
    def __init__(self, nome, vida, pocao, atack):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack

def Inicio():
    print("******************")
    print("* STRET OF TRETA *")
    print("******************")
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

def SOT():
    while True:
        print("Escolha um Heroi:")
        for i in range(10):
            print(i+1, "-", heroi[i].nome)
        escolha_heroi = int(input('> '))
        if escolha_heroi < 1 or escolha_heroi > 10:
            print("Entrada Invalida!\n")
        else:
            print("")
            break
    while True:
        print("Escolha um Vilão:")
        for i in range(4):
            print(i+1, "-", vilao[i].nome)
        escolha_vilao = int(input("> "))
        if escolha_vilao < 1 or escolha_vilao > 4:
            print("Entrada Invalida!\n")
        else:
            print("")
            break

def Main():
    Inicio()
    SOT()

heroi = []
heroi.append(Personagem("Bill", 50 , 2, 5))
heroi.append(Personagem("C2", 50 , 2, 5))
heroi.append(Personagem("Jumpsbare", 50 , 2, 5))
heroi.append(Personagem("Lucyfilho", 50 , 2, 5))
heroi.append(Personagem("Átomo", 50 , 2, 5))
heroi.append(Personagem("Alien", 50 , 2, 5))
heroi.append(Personagem("BLUEman", 50, 2, 5))
heroi.append(Personagem("Xerife Maluvido", 50 , 2, 5))
heroi.append(Personagem("Árvore", 50 , 2, 5))
heroi.append(Personagem("Dracoman", 50 , 2, 5))

vilao = []
vilao.append(Personagem("Gigante", 50 , 2, 5))
vilao.append(Personagem("Martin Prudente", 50 , 2, 5))
vilao.append(Personagem("Demonio Rubro", 50 , 2, 5))
vilao.append(Personagem("Morte", 50 , 2, 5))

Main()