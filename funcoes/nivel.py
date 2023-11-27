class NivelPersonagem:
    def __init__(self, nivel: int):
        self.nivel = nivel
    def subir_nivel(self, personagem:Personagem):
        for i in range(len(personagem)):
            if personagem[i].vitoria >= personagem[i].nivel:
                personagem[i].nivel += 1
                print(personagem[i].nome, "subiu para o nivel", personagem[i].nivel, "\n")