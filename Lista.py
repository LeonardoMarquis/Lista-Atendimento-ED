class Node:     # o chamado nó da lista encadeada, vai representar a pessoa
    def __init__(self, nome, prioridade = False):   # para receber o nome, e o outro como booleano, true ou false
        self.nome = nome
        self.prioridade = prioridade
        self.prox = None

    def __str__(self):
        return f"{self.nome} ({'Prioridade' if self.prioridade else 'Normal'})"



class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

        self.quant_prioridade = 0
        self.quant_atendido_prioridade = 0
        
        self.quant_normal = 0

        self.total_atendidos_prioridade = 0
        self.total_atendidos_normal = 0

        # E para controlar o n de normais atendidos desde a última prioridade
        # Começa em 2 para forcar logo o primeiro atendimento ser de prioridade se existir
        self.normais_desde_ultima_prioridade = 2

    
    def inserir(self, nome, prioridade = False):
        novo = Node(nome, prioridade)

        if prioridade:
            self.quant_prioridade += 1
        else:                           # - Coloco um contador de pessoas normais
            self.quant_normal += 1


        if not self.inicio:
            self.inicio = novo 
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo 
                            # prioridade tem um valor booleano de true ou false
        print(f"\nAdicionado à fila. {nome} ;({'Prioridade' if prioridade else 'Normal'})")   # controlar o valor a ser printado logo aqui, na hora,


    def atender(self):
        if not self.inicio:
            print("\nFila vazia!")
            return

        # Variaveis para percorrer a lista
        atual = self.inicio 
        passado = None
        

        # Acha a pessoa a ser atendida de acordo com a regra de prioridade, 1 com, 2 sem
        # se faltar normal atende prioridade se faltar prioridade, segue normal
        vai_de_prioridade = (self.normais_desde_ultima_prioridade >= 2 and self.quant_prioridade > 0)


        if vai_de_prioridade:
            # procurar a primeira prioridade
            while atual and not atual.prioridade:
                passado = atual
                atual = atual.prox

            if not atual:
                # não achou prioridade ve se tem normal
                atual = self.inicio
                passado = None
                while atual and atual.prioridade:
                    passado = atual
                    atual = atual.prox
                if not atual:
                    print("\nFila vazia!")
                    return
                
                
        else:
            # preefeerencia em nromal
            while atual and atual.prioridade:
                passado = atual
                atual = atual.prox

            if not atual:
                # não achou normal ve se ter prioridade
                atual = self.inicio
                passado = None
                while atual and not atual.prioridade:
                    passado = atual
                    atual = atual.prox
                if not atual:
                    print("\nFila vazia!")
                    return


        # Atualiza contadores conforme o tipo atendido
        if atual.prioridade:
            self.quant_prioridade -= 1
            self.total_atendidos_prioridade += 1


            # zera o ciclo de normais após uma prioridade
            self.normais_desde_ultima_prioridade = 0

           
            self.quant_atendido_prioridade = 1
        else:
            self.quant_normal -= 1
            self.total_atendidos_normal += 1
            # incrementa quantos normais desde a última prioridade, e no max dois normais ai vai prioridade denvoo

            self.normais_desde_ultima_prioridade = min(self.normais_desde_ultima_prioridade + 1, 2)
            

            self.quant_atendido_prioridade = 0



        # aqui e a parte de remocoes da lista

        # remove o nó 'atual' da lista
        if passado:                     # se tem um no anterior, liga ele ao próximo do 'atual'
            passado.prox = atual.prox

        else: # se não há nó anterior, o 'atual' é o inicio da lista
            self.inicio = atual.prox
        
        # o nó a ser removido é o ultimo, atualiza o 'fim' da lista
        if atual == self.fim:
            self.fim = passado

        print(f"{atual} ; Atendido")

        

    def listar(self):
        if not self.inicio:
            print("\nFila Vazia!")
            return

        atual = self.inicio
        print("\nFila: ")

        while atual:
            print(f"; {atual}")
            atual = atual.prox


    def zerada(self):
        return self.inicio is None
    



    def estatisticas_finais(self):  
        total = self.total_atendidos_normal + self.total_atendidos_prioridade
        percent_atend_normal = (self.total_atendidos_normal/total) * 100
        percent_atend_prioridade = (self.total_atendidos_prioridade/total) * 100
        print("\n-----===-------====---=======--=-")
        print("\n-Estatísticas dos Atendimentos-")
        print(f"Pessoas com prioridade atendidas: {self.total_atendidos_prioridade} | {percent_atend_prioridade:.2f}% do Total")
        print(f"Pessoas normais atendidas: {self.total_atendidos_normal} | {percent_atend_normal:.2f}% do Total")
        print("\n-------====-----===------------=====")
