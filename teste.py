class Personagem:
    def __init__(self, nome, vida, pocao, atack):
        self.nome = nome
        self.vida = vida
        self.pocao = pocao
        self.atack = atack


heroi = []
arquivo = open("SOT.txt", "r")
linha = arquivo.readlines()
dados = []
for i in range((len(linha))):
    colunas = linha[i].split('-')
    nome = colunas[0]
    dados.append(int(colunas[1]))
    dados.append(int(colunas[2]))
    dados.append(int(colunas[3]))
    heroi.append(Personagem(nome, dados[0], dados[1], dados[2]))
arquivo.close()
for i in range(len(linha)):
    print(heroi[i].nome, heroi[i].vida, heroi[i].pocao, heroi[i].atack)