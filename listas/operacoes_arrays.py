from array import array

qualquer = array("B", [1, 1, 1, 2, 2, 3, 4])

print(qualquer)

# for i in qualquer:
#     print(i)

# for i in range(len(qualquer)):
#     print(f"Posição: {i} = {qualquer[i]}")

# Inserindo elementos no array
qualquer.insert(1, 3)
print(qualquer)

# Removendo elementos do array
qualquer.remove(1)
print(qualquer)

# Buscando um elemento em um array
print(qualquer.index(1))

# Atualizando elementos de um array
qualquer[1] = 10
print(qualquer)

