lista_inteiros = [1, 2, 3, 4, 5]

meu_iter = iter(lista_inteiros)

# print(next(meu_iter))
# print(next(meu_iter))

# Implementação real do for
while True:
    try:
        elemento = next(meu_iter)
        print(elemento)
    except StopIteration:
        break