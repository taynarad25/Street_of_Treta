def salvar_jogo(personagem):
    while True:
        print("Deseja salvar o jogo?")
        try:
            salvar = input(str("> "))
            if salvar == 'NÃO' or salvar == 'Não' or salvar == 'não' or salvar == 'n' or salvar == 'N':
                break
            elif salvar == 'SIM' or salvar == 'Sim' or salvar == 'sim' or salvar == 's' or salvar == 'S':
                arquivo = open("../infoPersonagens/SOT_personagens.txt", "w", encoding="utf8")
                for i in range(len(personagem)):
                    nome = str(personagem[i].nome)
                    vida = str(personagem[i].vida)
                    pocao = str(personagem[i].pocao)
                    atack = str(personagem[i].atack)
                    nivel = str(personagem[i].nivel)
                    vitoria = str(personagem[i].vitoria)
                    concatenado = nome + "|" + vida + "|" + pocao + "|" + atack + "|" + nivel + "|" + vitoria +"\n"
                    arquivo.write(concatenado)
                    arquivo.close()
                break
            else:
                raise TypeError ('Entrada Inválida!')
        except TypeError as e:
            print(e)