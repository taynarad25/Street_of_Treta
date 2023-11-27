from funcoes.nivel import subir_nivel
from funcoes.atack import atualizar_atack
from funcoes.pocao import atualizar_pocao

class Personagem:
    def __init__(self, nome, vida, pocao, atack, nivel, vitoria):
        self.nome = nome
        self.vida = VidaPersonagem(vida)
        self.pocao = PocaoPersonagem(pocao)
        self.atack = AtackPersonagem(atack)
        self.nivel = NivelPersonagem(nivel)
        self.vitoria = vitoria
    def criar_personagens(self):
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
        return personagem
