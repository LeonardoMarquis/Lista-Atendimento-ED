from Lista import Lista

def main():

    l = Lista()

    while True:
        
        print("\n---------------------")
        print("\nMENU")
        print("\n1)Chegada de uma pessoa para atendimento\n2)Atendimento de uma pessoa\n3)Listar pessoas\n0)Sair")

        op = int(input("\nOpcao: "))
        
        match op:
            case 1:
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

            case 2:
                l.atender()

            case 3:
                l.listar()


            case 0:
                if l.zerada() and l.total_atendidos_normal + l.total_atendidos_prioridade != 0:
                    l.estatisticas_finais()
                    print("\nEncerrando.")

                    break
                elif l.zerada() and l.total_atendidos_normal + l.total_atendidos_prioridade == 0:
                    print("\nNenhuma operação realizada\nEncerrado")
                    break
                else:
                    print("\nTermine todos os atendimentos antes de sair!")

            case _:
                print("\nDigitaste alguma coisa errada!")





if __name__ == "__main__":
    main()

