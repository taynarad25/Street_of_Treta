def serie_jogo(rodada, personagem, tempo):
    empate = 0
    vez_cpu = 0
    vez_jogador = 0
    while True:
        time.sleep(tempo)
        rodada += 1
        print("* * * * * * * *")
        print("*             *")
        print("* {:02}° Rodada  *".format(rodada))
        print("*             *")
        print("* * * * * * * *\n")

        escolha_opcoes(personagem, tempo):
            
        if opcao == 1 and cpu == 3 or opcao == 2 and cpu == 1 or opcao == 3 and cpu == 2:
            #JOGADOR GANHOU!
            print("Vez de", personagem[escolha[0] - 1].nome,"atacar!")
            empate = 0
            if vez_cpu == 1:
                vez_cpu = 0
            elif vez_cpu > 1:
                vez_cpu = 0
                print("O ataque de", personagem[escolha[1] - 1].nome,"voltou a ser", personagem[escolha[1] - 1].atack, "pontos.")
            vez_jogador += 1
            if vez_jogador == 1:
                personagem[escolha[1] - 1].vida  -= personagem[escolha[0] - 1].atack
            elif vez_jogador == 2:
                personagem[escolha[1] - 1].vida -= personagem[escolha[0] - 1].atack + 1
                print("\nO ataque de", personagem[escolha[0] - 1].nome,"agora é de", personagem[escolha[0] - 1].atack + 1,"pontos\n")
            elif vez_jogador == 3:
                personagem[escolha[1] - 1].vida -= personagem[escolha[0] - 1].atack + 10
                print("\nO ataque de", personagem[escolha[0] - 1].nome,"agora é de", personagem[escolha[0] - 1].atack + 10,"pontos\n")
            elif vez_jogador > 3:
                personagem[escolha[1] - 1].vida -= personagem[escolha[0] - 1].atack + 10
            print("Vida", personagem[escolha[1] - 1].nome,":", personagem[escolha[1] - 1].vida, "\n")

            if personagem[escolha[0] - 1].vida > 0 and personagem[escolha[0] - 1].vida < 25 and personagem[escolha[0] - 1].pocao > 0 and personagem[escolha[1] - 1].vida > 0:
                print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida)
                print(personagem[escolha[0] - 1].nome, "tem", personagem[escolha[0] - 1].pocao, "poções\n")
                while True:
                    print("Deseja usar uma?")
                    pocao = str(input("> "))
                    if pocao == 'SIM' or pocao == 'Sim' or pocao == 'sim' or pocao == 'S' or pocao == 's':
                        personagem[escolha[0] - 1].vida += 15
                        personagem[escolha[0] - 1].pocao -= 1
                        print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida)
                        print(personagem[escolha[0] - 1].nome, "tem", personagem[escolha[0] - 1].pocao, "poções")
                        break
                    elif pocao == 'NÃO' or pocao == 'Não' or pocao == 'não' or pocao == 'N' or pocao == 'n':
                        break
                    else:
                        print(EntradaInvalida)

        elif opcao == cpu:
            empate += 1
            #EMPATE
            print("Empate! Tente novamente.\n")
            if empate == 3:
                personagem[escolha[0] - 1].vida = personagem[escolha[0] - 1].vida - 5
                personagem[escolha[1] - 1].vida = personagem[escolha[1] - 1].vida - 5
                print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida)
                print("Vida", personagem[escolha[1] - 1].nome,":", personagem[escolha[1] - 1].vida)
                empate = 0
            if vez_cpu == 1:
                vez_cpu = 0
            elif vez_cpu > 1:
                vez_cpu = 0
                print("O ataque de", personagem[escolha[1] - 1].nome,"voltou a ser", personagem[escolha[0] - 1].atack, "pontos.")
            if vez_jogador == 1:
                vez_jogador = 0
            elif vez_jogador > 1:
                vez_jogador = 0
                print("O ataque de", personagem[escolha[0] - 1].nome,"voltou a ser", personagem[escolha[0] - 1].atack, "pontos.")

        elif cpu == 1 and opcao == 3 or cpu == 2 and opcao == 1 or cpu == 3 and opcao == 2:
            #JOGADOR PERDEU!
            print("Vez de", personagem[escolha[1] - 1].nome,"atacar!")
            empate = 0
            if vez_jogador == 1:
                vez_jogador = 0
            elif vez_jogador > 1:
                vez_jogador = 0
                print("O ataque de", personagem[escolha[0] - 1].nome,"voltou a ser", personagem[escolha[0] - 1].atack, "pontos.")
            vez_cpu += 1
            if vez_cpu  == 1:
                personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack
            elif vez_cpu == 2:
                personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack + 1
                print("\nO ataque de", personagem[escolha[1] - 1].nome,"agora é de", personagem[escolha[1] - 1].atack + 1,"pontos\n")
            elif vez_cpu == 3:
                personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack + 10
                print("\nO ataque de", personagem[escolha[1] - 1].nome,"agora é de", personagem[escolha[1] - 1].atack + 10,"pontos\n")
            elif vez_cpu > 3:
                personagem[escolha[0] - 1].vida -= personagem[escolha[1] - 1].atack + 10
            print("Vida", personagem[escolha[0] - 1].nome,":", personagem[escolha[0] - 1].vida, "\n")

            if personagem[escolha[1] - 1].vida > 0 and personagem[escolha[1] - 1].vida < 25 and personagem[escolha[1] - 1].pocao > 0 and personagem[escolha[0] - 1].vida > 0:
                pocao = randint(1, 2)
                if pocao == 1:
                    print(personagem[escolha[1] - 1].nome,"usou 1 poção\n")
                    personagem[escolha[1] - 1].vida += 15
                    personagem[escolha[1] - 1].pocao -= 1
                    print("Vida", personagem[escolha[1] - 1].nome,":", personagem[escolha[1] - 1].vida)
                    print(personagem[escolha[1] - 1].nome,"tem", personagem[escolha[1] - 1].pocao,"poção")
                elif pocao == 2:
                    print(personagem[escolha[1] - 1].nome,"tem", personagem[escolha[1] - 1].pocao,"poção")

        if personagem[escolha[0] - 1].vida <= 0 or personagem[escolha[1] - 1].vida <= 0:
            break
    serie = [rodada, personagem]
    return serie