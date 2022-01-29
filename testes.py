class Personagem:
    def __init__(self, nome, vida, pocao, atack):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack
heroi = []
heroi.append(Personagem("Bill", 50 , 2, 5))
heroi.append(Personagem("C2", 50 , 2, 5))
heroi.append(Personagem("Jumpsbare", 50 , 2, 5))
heroi.append(Personagem("Lucyfilho", 50 , 2, 5))

print("Escolha um Heroi:")
for i in range(4):
    print(i+1, "-", heroi[i].nome)
