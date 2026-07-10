from random import choice, randint

from db import ATACK_BASE, NIVEL_INICIAL, POCAO_BASE, ROSTER_PADRAO, VIDA_BASE, VITORIA_INICIAL

INCREMENTO_VIDA_POR_NIVEL = 5
INCREMENTO_ATACK_POR_NIVEL = 1

LIMIAR_POCAO = 25
CURA_POCAO = 15

BONUS_COMBO_2 = 1
BONUS_COMBO_3 = 10

VIDA_PERDIDA_EMPATE = 5
EMPATES_PARA_PENALIDADE = 3

NOMES_JOGADAS = {1: "Pedra", 2: "Papel", 3: "Tesoura"}


class Personagem:
    def __init__(self, nome, vida, pocao, atack, nivel, vitoria):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack
        self.nivel = nivel
        self.vitoria = vitoria


def gerar_cpu(excluir_nome=None):
    """Personagem da CPU: nome aleatório e status próprio, independente do
    usuário logado — vitórias/derrotas da CPU nunca são salvas no banco."""
    nomes_possiveis = [n for n in ROSTER_PADRAO if n != excluir_nome] or ROSTER_PADRAO
    nome = choice(nomes_possiveis)
    return Personagem(nome, VIDA_BASE, POCAO_BASE, ATACK_BASE, NIVEL_INICIAL, VITORIA_INICIAL)


def calcular_bonus_ataque(contador):
    if contador <= 1:
        return 0
    if contador == 2:
        return BONUS_COMBO_2
    return BONUS_COMBO_3


def aplicar_ataque(atacante, defensor, contador):
    mensagens = []
    bonus = calcular_bonus_ataque(contador)
    defensor.vida -= atacante.atack + bonus
    if contador in (2, 3):
        mensagens.append(f"O ataque de {atacante.nome} agora é de {atacante.atack + bonus} pontos")
    mensagens.append(f"Vida {defensor.nome}: {defensor.vida}")
    return mensagens


def resetar_combo(personagem, contador):
    mensagens = []
    if contador > 1:
        mensagens.append(f"O ataque de {personagem.nome} voltou a ser {personagem.atack} pontos.")
    return 0, mensagens


def pode_usar_pocao(personagem, oponente):
    return (
        personagem.vida > 0
        and personagem.vida < LIMIAR_POCAO
        and personagem.pocao > 0
        and oponente.vida > 0
    )


def usar_pocao(personagem):
    personagem.vida += CURA_POCAO
    personagem.pocao -= 1


def tentar_usar_pocao_cpu(cpu, oponente):
    mensagens = []
    if pode_usar_pocao(cpu, oponente) and randint(1, 2) == 1:
        usar_pocao(cpu)
        mensagens.append(f"{cpu.nome} usou 1 poção")
        mensagens.append(f"Vida {cpu.nome}: {cpu.vida}")
    return mensagens


def jogar_rodada(jogador, cpu, jogada_jogador, contadores):
    mensagens = []
    jogada_cpu = randint(1, 3)
    mensagens.append(f"{cpu.nome}: {NOMES_JOGADAS[jogada_cpu]}")

    if (jogada_jogador == 1 and jogada_cpu == 3) or (jogada_jogador == 2 and jogada_cpu == 1) or (jogada_jogador == 3 and jogada_cpu == 2):
        resultado = "vitoria"
        mensagens.append(f"Vez de {jogador.nome} atacar!")
        contadores["empate"] = 0
        contadores["vez_cpu"], msgs = resetar_combo(cpu, contadores["vez_cpu"])
        mensagens += msgs
        contadores["vez_jogador"] += 1
        mensagens += aplicar_ataque(jogador, cpu, contadores["vez_jogador"])
        pode_pocao = pode_usar_pocao(jogador, cpu)

    elif jogada_jogador == jogada_cpu:
        resultado = "empate"
        contadores["empate"] += 1
        mensagens.append("Empate! Tente novamente.")
        if contadores["empate"] == EMPATES_PARA_PENALIDADE:
            jogador.vida -= VIDA_PERDIDA_EMPATE
            cpu.vida -= VIDA_PERDIDA_EMPATE
            mensagens.append(f"Vida {jogador.nome}: {jogador.vida}")
            mensagens.append(f"Vida {cpu.nome}: {cpu.vida}")
            contadores["empate"] = 0
        contadores["vez_cpu"], msgs = resetar_combo(cpu, contadores["vez_cpu"])
        mensagens += msgs
        contadores["vez_jogador"], msgs = resetar_combo(jogador, contadores["vez_jogador"])
        mensagens += msgs
        pode_pocao = False

    else:
        resultado = "derrota"
        mensagens.append(f"Vez de {cpu.nome} atacar!")
        contadores["empate"] = 0
        contadores["vez_jogador"], msgs = resetar_combo(jogador, contadores["vez_jogador"])
        mensagens += msgs
        contadores["vez_cpu"] += 1
        mensagens += aplicar_ataque(cpu, jogador, contadores["vez_cpu"])
        mensagens += tentar_usar_pocao_cpu(cpu, jogador)
        pode_pocao = False

    morreu = jogador.vida <= 0 or cpu.vida <= 0
    return {
        "mensagens": mensagens,
        "resultado": resultado,
        "pode_pocao": pode_pocao,
        "morreu": morreu,
    }


def atualizar_vida(personagens):
    for p in personagens:
        vida = VIDA_BASE + (p.nivel - 1) * INCREMENTO_VIDA_POR_NIVEL
        if p.vida > 0 and p.vida < vida:
            p.vida = vida


def atualizar_atack(personagens):
    for p in personagens:
        atack = ATACK_BASE + (p.nivel - 1) * INCREMENTO_ATACK_POR_NIVEL
        if p.atack > 0 and p.atack < atack:
            p.atack = atack


def atualizar_pocao(personagens):
    for p in personagens:
        pocao = POCAO_BASE + (p.nivel - 1) // 2
        if p.vida > 0 and p.nivel == 1 and p.pocao != POCAO_BASE:
            p.pocao = POCAO_BASE
        elif p.vida > 0 and p.nivel > 1 and p.pocao < pocao:
            p.pocao = pocao


def subir_nivel(personagens):
    mensagens = []
    for p in personagens:
        if p.vitoria >= p.nivel:
            p.nivel += 1
            mensagens.append(f"{p.nome} subiu para o nível {p.nivel}")
    atualizar_pocao(personagens)
    atualizar_atack(personagens)
    atualizar_vida(personagens)
    return mensagens
