import time
def escolha_opcoes(personagem, tempo):
    while True:
        time.sleep(tempo)
        print("\nEscolha uma das opções:")
        time.sleep(tempo/2)
        print("1 - Pedra")
        time.sleep(tempo/2)
        print("2 - Papel")
        time.sleep(tempo/2)
        print("3 - Tesoura")
        time.sleep(tempo/2)
        print("0 - Sair")
        time.sleep(tempo/2)
        try:
            opcao = int(input("> "))
            if opcao < 0 or opcao > 3:
                raise ValueError()
            elif opcao == 0:
                sys.exit()
            else:
                break
        except ValueError:
            print("\nEntrada Inválida!")

    cpu = randint(1, 3)
    if cpu == 1:
        print(personagem[escolha[1] - 1].nome, ": Pedra\n")
    elif cpu == 2:
        print(personagem[escolha[1] - 1].nome, ": Papel\n")
    else:
        print(personagem[escolha[1] - 1].nome, ": Tesoura\n")