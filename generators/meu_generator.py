def retorna_elemento(lista):
    n = 0
    while n < len(lista):
        yield  lista[n]
        n += 1

lista_nomes = ("Wellington", "Nora", "Junior")
lista_numeros = (10, 20, 30, 40, 50, 60)

for index in retorna_elemento(lista_nomes):
    print(index)

for index in retorna_elemento(lista_numeros):
    print(index)