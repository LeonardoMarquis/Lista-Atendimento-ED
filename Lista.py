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
        
        # Encontra a pessoa a ser atendida de acordo com a regra de prioridade
        # a regra e: 2 prioridades, depois 1 normal

        if self.quant_atendido_prioridade < 2 and self.quant_prioridade > 0:

            # Prioridade para atendimento no maximo 2 prioridades seguidas

            while atual and not atual.prioridade:
                passado = atual
                atual = atual.prox
            

            
            # Se nao tm mais prioridades na lista, retorna e avisa

            if not atual:
                # Reinicia a busca do primeiro normal na fila

                atual = self.inicio
                passado = None
                while atual and atual.prioridade:
                    passado = atual
                    atual = atual.prox

                if atual:           # se tem normal encontrou ele aqui
                    self.quant_normal -= 1
                    self.quant_atendido_prioridade = 0          # Reseta o contador para a proxima vez que tiverr prioridad


                else:                           
                    return
                

            else:               # Encontrou uma pessoa de prioridade
                self.quant_prioridade -= 1
                self.quant_atendido_prioridade += 1
        

        else:                   # Caso contrario, atende uma pessoa normal
            

            # acha o primeiro cliente normal da fila
            while atual and atual.prioridade:
                passado = atual
                atual = atual.prox
            
            if not atual:                       # Não ha pessoas normais na fila. Procura por prioridade para atender.
                print("\nSem clientes normais para atender")

                # Reinicia a busca do primeiro prioridade na fila
                atual = self.inicio
                passado = None
                while atual and not atual.prioridade:
                    passado = atual
                    atual = atual.prox

                if atual:                   # Encontrou um prioridade
                    self.quant_prioridade -= 1
                    self.quant_atendido_prioridade += 1


                else:
                    print("\nFila vazia!")
                    return

            else: # Encontrou uma pessoa normal para atender
                self.quant_normal -= 1
                self.quant_atendido_prioridade = 0 # Reseta o contador de prioridade, porque atendeu 1u normal




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