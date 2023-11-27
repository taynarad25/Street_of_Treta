def jogar_novamente():
    while True:
        print("Deseja jogar novamente?")
        try:
            novamente = str(input("> "))
            if novamente == "SIM" or novamente == "Sim" or novamente == "sim" or novamente == "S" or novamente == "s":
                break
            elif novamente == "NÃO" or novamente == "Não" or novamente == "não" or novamente == "N" or novamente == "n":
                sys.exit()
            else:
                raise TypeError ('Entrada Inválida!')
        except TypeError as e:
            print(e)