import time
def escolha_personagem(escolha, personagem, index, tempo):
    while True:
        time.sleep(tempo)
        print("\nEscolha o {}° personagem:".format(index+1))
        for i in range(len(personagem)):
            print(i+1, "-", personagem[i].nome)
            time.sleep(tempo/2)
        try:
            escolha[index] = int(input('> '))
            if type(escolha[index]) == type('a'):
                raise ValueError()
            try:
                if escolha[index] < 1 or escolha[index] > 14:
                    print(EntradaInvalida)
                elif personagem[escolha[index] - 1].vida <= 0:
                    raise TypeError('\nNão é possível escolher '+ personagem[escolha[index] - 1].nome)
                else:
                    return escolha
            except TypeError as e:
                print(e)
        except ValueError:
            print("\nEntrada Inválida!")