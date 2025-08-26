class Node:
    def __init__(self, nome):
        self.nome = nome
        self.prox = None

class Lista:
    def __init__(self):
        self.inicio = None
    
    def inserir(self, nome):
        novo = Node(nome)
        novo.prox = self.inicio
        self.inicio = novo

    def mostrar(self):
        aux = self.inicio
        seqNomes=""
        while aux != None:
            seqNomes += aux.nome + " - "
            aux = aux.prox
        return seqNomes

    def size(self):
        aux = self.inicio
        qde = 0
        while aux != None:
            qde += 1
            aux = aux.prox
        return qde


    def inverter(self):
        aux = self.inicio

        while aux != None:

