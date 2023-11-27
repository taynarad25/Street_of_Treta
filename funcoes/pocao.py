class PocaoPersonagem:
    def __init__(self, pocao):
        self.pocao = pocao
    def atualizar_pocao(self, personagem):
        pocao = 2 + (personagem.nivel - 1) // 2
        if personagem.vida > 0 and personagem.nivel == 1 and personagem.pocao != 2:
            personagem.pocao = 2
        elif personagem.vida > 0 and personagem.nivel > 1 and personagem.pocao < pocao:
            personagem.pocao = pocao
        return personagem