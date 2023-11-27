from salvar_jogo import salvar_jogo
from novo_jogo import novo_jogo

def continuar_jogo():
    while True:
        print("Deseja continuar o jogo anterior?")
        try:
            continuar = input(str("> "))
            if continuar == 'SIM' or continuar == 'Sim' or continuar == 'sim' or continuar == 'S' or continuar == 's':
                break
            elif continuar == 'NÃO' or continuar == 'Não' or continuar == 'não' or continuar == 'N' or continuar == 'n':
                novo()
                salvar()
                break
            else:
                raise TypeError ('Entrada Inválida!')
        except TypeError as e:
            print(e)