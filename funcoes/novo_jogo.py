def novo_jogo():
    info = open("infoPersonagens/valores_iniciais.txt", encoding="utf8")
    linha = info.readline()
    info.close()
    coluna = linha.split("|")
    vida = int(coluna[0])
    pocao = int(coluna[1])
    atack = int(coluna[2])
    nivel = int(coluna[3])
    vitoria = int(coluna[4])
    for i in range(len(personagem)):
        personagem[i].vida = vida
        personagem[i].pocao = pocao
        personagem[i].atack = atack
        personagem[i].nivel = nivel
        personagem[i].vitoria = vitoria