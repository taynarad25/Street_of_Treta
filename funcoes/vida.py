class VidaPersonagem:
    def __init__(self, vida):
        self.vida = vida
    def atualizar_vida(self, personagem):
        vida = 50 + ((personagem.nivel - 1) * 5)
        if personagem.vida > 0 and personagem.vida < vida:
            personagem.vida = vida
        return personagem