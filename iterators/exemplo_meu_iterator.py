class MeuIterator:
    def __init__(self, lista):
        self.lista = lista
        self.max = len(lista)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            elemento = self.lista[self.n]
            self.n += 1
            return elemento
        else:
            raise StopIteration


minha_lista = ("wellington", "nora", "eu mesmo")
lista_numero = (10,10,10 , 20)

for index in MeuIterator(lista_numero):
    print(index)