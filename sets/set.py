meu_set1 = {1, 2, 3, 4}
meu_set2 = set([1, 2, 3])

print(type(meu_set1))
print(type(meu_set2))

# add()
meu_set1.add(5)
print(meu_set1)

# update()
meu_set1.update([1, 2, 3, 4, 5, 6])
print(meu_set1)

# discard()
meu_set1.discard(1)
print(meu_set1)

# União
print(meu_set1 | meu_set2)
print(meu_set1.union(meu_set2))

# Interseção
print(meu_set1 & meu_set2)
print(meu_set1.intersection(meu_set2))

# Diferença
print(meu_set1 - meu_set2)
print(meu_set2.difference(meu_set1))

# Diferença Simétrica
print(meu_set1 ^ meu_set2)
print(meu_set1.symmetric_difference(meu_set2) )