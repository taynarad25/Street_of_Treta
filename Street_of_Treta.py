from random import randint
import sys
import time

# Estado global: lista de personagens, carregada do arquivo de save em Criar_personagens()
personagem = []

VIDA_BASE = 50
ATACK_BASE = 5
POCAO_BASE = 2
INCREMENTO_VIDA_POR_NIVEL = 5
INCREMENTO_ATACK_POR_NIVEL = 1

LIMIAR_POCAO = 25
CURA_POCAO = 15

BONUS_COMBO_2 = 1
BONUS_COMBO_3 = 10

VIDA_PERDIDA_EMPATE = 5
EMPATES_PARA_PENALIDADE = 3

ARQUIVO_PERSONAGENS = "infoPersonagens/SOT_personagens.txt"
ARQUIVO_VALORES_INICIAIS = "infoPersonagens/valores_iniciais.txt"

NOMES_JOGADAS = {1: "Pedra", 2: "Papel", 3: "Tesoura"}


class Personagem:
    def __init__(self, nome, vida, pocao, atack, nivel, vitoria):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack
        self.nivel = nivel
        self.vitoria = vitoria


def confirmar(pergunta):
    respostas_sim = {"sim", "s"}
    respostas_nao = {"não", "nao", "n"}
    while True:
        print(pergunta)
        try:
            resposta = input("> ").strip().lower()
        except EOFError:
            print("Entrada Invalida!")
            continue
        if resposta in respostas_sim:
            return True
        if resposta in respostas_nao:
            return False
        print("Entrada Invalida!\n")


def Inicio():
    print("* * * * * * * * * * *")
    print("*                   *")
    print("*  STREET OF TRETA  *")
    print("*                   *")
    print("* * * * * * * * * * *")
    if confirmar("\nDeseja ler as instruções?"):
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
    else:
        print("")
    time.sleep(0.5)


def Atualizar_vida():
    for p in personagem:
        vida = VIDA_BASE + (p.nivel - 1) * INCREMENTO_VIDA_POR_NIVEL
        if p.vida > 0 and p.vida < vida:
            p.vida = vida


def Atualizar_atack():
    for p in personagem:
        atack = ATACK_BASE + (p.nivel - 1) * INCREMENTO_ATACK_POR_NIVEL
        if p.atack > 0 and p.atack < atack:
            p.atack = atack


def Atualizar_pocao():
    for p in personagem:
        pocao = POCAO_BASE + (p.nivel - 1) // 2
        if p.vida > 0 and p.nivel == 1 and p.pocao != POCAO_BASE:
            p.pocao = POCAO_BASE
        elif p.vida > 0 and p.nivel > 1 and p.pocao < pocao:
            p.pocao = pocao


def Escolha_personagem(escolha):
    def escolher(indices_bloqueados):
        while True:
            print("\nEscolha um personagem:")
            for i in range(len(personagem)):
                print(i + 1, "-", personagem[i].nome)
            try:
                valor = int(input("> "))
            except ValueError:
                print("Entrada Invalida!\n")
                continue
            if valor < 1 or valor > len(personagem):
                print("Entrada Invalida!\n")
            elif personagem[valor - 1].vida <= 0 or valor in indices_bloqueados:
                print("\nNão é possível escolher", personagem[valor - 1].nome)
            else:
                print("")
                return valor

    escolha[0] = escolher([])
    escolha[1] = escolher([escolha[0]])
    return escolha


def escolher_jogada():
    while True:
        print("\nEscolha uma das opções:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        print("0 - Sair")
        try:
            opcao = int(input("> "))
        except ValueError:
            print("Entrada Invalida!\n")
            continue
        if opcao < 0 or opcao > 3:
            print("Entrada Invalida!\n")
        elif opcao == 0:
            sys.exit()
        else:
            return opcao


def calcular_bonus_ataque(contador):
    if contador <= 1:
        return 0
    if contador == 2:
        return BONUS_COMBO_2
    return BONUS_COMBO_3


def aplicar_ataque(atacante_idx, defensor_idx, contador):
    atacante = personagem[atacante_idx]
    defensor = personagem[defensor_idx]
    bonus = calcular_bonus_ataque(contador)
    defensor.vida -= atacante.atack + bonus
    if contador in (2, 3):
        print("\nO ataque de", atacante.nome, "agora é de", atacante.atack + bonus, "pontos\n")
    print("Vida", defensor.nome, ":", defensor.vida, "\n")


def resetar_combo(contador, idx):
    if contador > 1:
        print("O ataque de", personagem[idx].nome, "voltou a ser", personagem[idx].atack, "pontos.")
    return 0


def tentar_usar_pocao_jogador(idx_jogador, idx_oponente):
    jogador = personagem[idx_jogador]
    oponente = personagem[idx_oponente]
    if jogador.vida > 0 and jogador.vida < LIMIAR_POCAO and jogador.pocao > 0 and oponente.vida > 0:
        print("Vida", jogador.nome, ":", jogador.vida)
        print(jogador.nome, "tem", jogador.pocao, "poções\n")
        if confirmar("Deseja usar uma?"):
            jogador.vida += CURA_POCAO
            jogador.pocao -= 1
            print("Vida", jogador.nome, ":", jogador.vida)
            print(jogador.nome, "tem", jogador.pocao, "poções")


def tentar_usar_pocao_cpu(idx_cpu, idx_oponente):
    cpu = personagem[idx_cpu]
    oponente = personagem[idx_oponente]
    if cpu.vida > 0 and cpu.vida < LIMIAR_POCAO and cpu.pocao > 0 and oponente.vida > 0:
        if randint(1, 2) == 1:
            print(cpu.nome, "usou 1 poção\n")
            cpu.vida += CURA_POCAO
            cpu.pocao -= 1
            print("Vida", cpu.nome, ":", cpu.vida)
        print(cpu.nome, "tem", cpu.pocao, "poção")


def jogar_rodada(escolha, contadores):
    idx_jogador = escolha[0] - 1
    idx_cpu = escolha[1] - 1

    opcao = escolher_jogada()
    cpu = randint(1, 3)
    print(personagem[idx_cpu].nome, ":", NOMES_JOGADAS[cpu], "\n")
    time.sleep(0.5)

    if (opcao == 1 and cpu == 3) or (opcao == 2 and cpu == 1) or (opcao == 3 and cpu == 2):
        # Jogador ganhou
        print("Vez de", personagem[idx_jogador].nome, "atacar!")
        contadores["empate"] = 0
        contadores["vez_cpu"] = resetar_combo(contadores["vez_cpu"], idx_cpu)
        contadores["vez_jogador"] += 1
        aplicar_ataque(idx_jogador, idx_cpu, contadores["vez_jogador"])
        tentar_usar_pocao_jogador(idx_jogador, idx_cpu)

    elif opcao == cpu:
        # Empate
        contadores["empate"] += 1
        print("Empate! Tente novamente.\n")
        if contadores["empate"] == EMPATES_PARA_PENALIDADE:
            personagem[idx_jogador].vida -= VIDA_PERDIDA_EMPATE
            personagem[idx_cpu].vida -= VIDA_PERDIDA_EMPATE
            print("Vida", personagem[idx_jogador].nome, ":", personagem[idx_jogador].vida)
            print("Vida", personagem[idx_cpu].nome, ":", personagem[idx_cpu].vida)
            contadores["empate"] = 0
        contadores["vez_cpu"] = resetar_combo(contadores["vez_cpu"], idx_cpu)
        contadores["vez_jogador"] = resetar_combo(contadores["vez_jogador"], idx_jogador)

    else:
        # CPU ganhou
        print("Vez de", personagem[idx_cpu].nome, "atacar!")
        contadores["empate"] = 0
        contadores["vez_jogador"] = resetar_combo(contadores["vez_jogador"], idx_jogador)
        contadores["vez_cpu"] += 1
        aplicar_ataque(idx_cpu, idx_jogador, contadores["vez_cpu"])
        tentar_usar_pocao_cpu(idx_cpu, idx_jogador)


def SOT():
    if not confirmar("Deseja continuar o jogo anterior?"):
        Novo()
        Salvar()

    # Cada iteração deste laço é uma partida completa entre dois personagens
    while True:
        rodada = 0
        contadores = {"empate": 0, "vez_cpu": 0, "vez_jogador": 0}
        escolha = [0, 0]
        Escolha_personagem(escolha)
        idx_jogador = escolha[0] - 1
        idx_cpu = escolha[1] - 1

        while True:
            time.sleep(0.5)
            rodada += 1
            print("* * * * * * * *")
            print("*             *")
            print("* {:02}° Rodada  *".format(rodada))
            print("*             *")
            print("* * * * * * * *\n")

            jogar_rodada(escolha, contadores)

            if personagem[idx_jogador].vida <= 0 or personagem[idx_cpu].vida <= 0:
                break

        if personagem[idx_jogador].vida <= 0:
            print(personagem[idx_jogador].nome, "morreu. Você perdeu!")
            personagem[idx_cpu].vitoria += 1
            personagem[idx_jogador].vitoria = 0
        elif personagem[idx_cpu].vida <= 0:
            print(personagem[idx_cpu].nome, "morreu. Você ganhou!")
            personagem[idx_jogador].vitoria += 1
            personagem[idx_cpu].vitoria = 0

        print("Rodadas Jogadas:", rodada)

        Subir_nivel()

        if confirmar("Deseja salvar o jogo?"):
            Salvar()

        if not confirmar("Deseja jogar novamente?"):
            sys.exit()


def Main():
    Inicio()
    Criar_personagens()
    SOT()


def Novo():
    with open(ARQUIVO_VALORES_INICIAIS, encoding="utf8") as arquivo:
        linha = arquivo.readline()
    vida, pocao, atack, nivel, vitoria = (int(v) for v in linha.split("|")[:5])
    for p in personagem:
        p.vida = vida
        p.pocao = pocao
        p.atack = atack
        p.nivel = nivel
        p.vitoria = vitoria


def Salvar():
    # Sobrescreve o arquivo de save com o estado atual de todos os personagens
    with open(ARQUIVO_PERSONAGENS, "w", encoding="utf8") as arquivo:
        for p in personagem:
            arquivo.write(f"{p.nome}|{p.vida}|{p.pocao}|{p.atack}|{p.nivel}|{p.vitoria}\n")


def Criar_personagens():
    with open(ARQUIVO_PERSONAGENS, "r", encoding="utf8") as arquivo:
        linhas = arquivo.readlines()
    for linha in linhas:
        coluna = linha.split("|")
        nome = coluna[0]
        vida, pocao, atack, nivel, vitoria = (int(v) for v in coluna[1:6])
        personagem.append(Personagem(nome, vida, pocao, atack, nivel, vitoria))


def Subir_nivel():
    for p in personagem:
        if p.vitoria >= p.nivel:
            p.nivel += 1
            print(p.nome, "subiu para o nivel", p.nivel, "\n")
    Atualizar_pocao()
    Atualizar_atack()
    Atualizar_vida()


if __name__ == "__main__":
    Main()
