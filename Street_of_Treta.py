from random import randint

class Personagem:
    def __init__(self, nome, vida, pocao, atack):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack

# OBS.: Tentar implementar de uma forma diferente.
def CriarPersonagens():
    # Herois
    bill = Personagem("Bill", 50 , 2, 5)
    c2 = Personagem("C2", 50 , 2, 5)
    jumpsbare = Personagem("Jumpsbare", 50 , 2, 5)
    lucyfilho = Personagem("Lucyfilho", 50 , 2, 5)
    atomo = Personagem("Átomo", 50 , 2, 5)
    alien = Personagem("Alien", 50 , 2, 5)
    blueman = Personagem("BLUEman", 50, 2, 5)
    xerife_maluvido = Personagem("Xerife Maluvido", 50 , 2, 5)
    arvore = Personagem("Árvore", 50 , 2, 5)
    dracoman = Personagem("Dracoman", 50 , 2, 5)
    
    # Vilões
    gigante = Personagem("Gigante", 50 , 2, 5)
    martin_prudente = Personagem("Martin Prudente", 50 , 2, 5)
    demonio_rubro = Personagem("Demonio Rubro", 50 , 2, 5)
    morte = Personagem("Morte", 50 , 2, 5)

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

def Main():
    Inicio()
