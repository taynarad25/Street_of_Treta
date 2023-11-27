from funcoes.continuar_jogo import continuar_jogo
from funcoes.jogar_novamente import jogar_novamente
from funcoes.escolha_personagem import escolha_personagem
from funcoes.serie_jogo import serie_jogo
from funcoes.instrucoes import instrucoes
from funcoes.subir_nivel import subir_nivel
from random import randint
import sys
import time

EntradaInvalida = 'Entrada Inválida!'

personagem = []

escolha = [0,0]

tempo = 0.25

class Personagem:
    def __init__(self, nome, vida, pocao, atack, nivel, vitoria):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack
        self.nivel = nivel
        self.vitoria = vitoria

def jogo():
    while True:
        rodada = 0
        
        for i in range(len(escolha)):
            escolha_personagem(escolha, personagem, i, tempo)
        
        rodada = serie_jogo(rodada, personagem, tempo)
        
        if personagem[escolha[0] - 1].vida <= 0:
            print(personagem[escolha[0] - 1].nome, "morreu. Você perdeu!")
            personagem[escolha[1] - 1].vitoria += 1
            personagem[escolha[0] - 1].vitoria = 0
        elif personagem[escolha[1] - 1].vida <= 0:
            print(personagem[escolha[1] - 1].nome, "morreu. Você ganhou!")
            personagem[escolha[0] - 1].vitoria += 1
            personagem[escolha[1] - 1].vitoria = 0

        print("Rodadas Jogadas:", rodada)
        subir_nivel(personagem)
        jogar_novamente()

def main():
    print("* * * * * * * * * * *")
    print("*                   *")
    print("*  STREET OF TRETA  *")
    print("*                   *")
    print("* * * * * * * * * * *")
    instrucoes(tempo)
    criar_personagens()
    continuar_jogo()
    jogo()

main()