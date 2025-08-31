from Lista import Lista

def main():

    l = Lista()

    while True:
        
        print("\n---------------------")
        print("\nMENU")
        print("\n1)Chegada de uma pessoa para atendimento\n2)Atendimento de uma pessoa\n3)Listar pessoas\n0)Sair")

        op = int(input("\nOpcao: "))

        if op == 1:
            nome = str(input("\nNome: "))
            tipo = str(input("\nNormal=2 | Prioridade=1\n"))
            while tipo != "1" and tipo != "2":
                tipo = str(input("\nNormal=2 | Prioridade=1\n"))


            if tipo == "1":
                l.inserir(nome, True)

            elif tipo == "2":
                l.inserir(nome, False)
            else:
                print("\nDigitaste algo errado! Recomece!")

        elif op == 2:
            l.atender()

        elif op == 3:
            l.listar()


        elif op == 0:
            #l.listar()
            if l.zerada():
                l.estatisticas_finais()
                print("\nEncerrando.")

                break
            else:
                print("\nTermine todos os atendimentos antes de sair!")

        else:
            print("\nDigitaste alguma coisa errada!")


if __name__ == "__main__":
    main()

