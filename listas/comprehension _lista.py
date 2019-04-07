lista = [1, 2, 3, 4, 5]
lista_quadrado = []
for i in lista:
    lista_quadrado.append(i * i)
print(lista_quadrado)

# Exemplo de lista comprehension
lista_quadrado_elegannte = [i * i for i in lista]
print(lista_quadrado_elegannte)