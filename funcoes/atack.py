class AtackPersonagem:
    def __init__(self, atack: int):
        self.atack = atack
    def atualizar_atack(self, nivel, atack):
        novo_atack = 5 + (nivel - 1)
        if atack > 0 and atack < novo_atack:
            atack = novo_atack
        return atack