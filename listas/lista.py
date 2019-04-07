lista_inteiro = [1, 2, 3, 4, 3, 4, 6, 10, 5]
lista_string = ["Olá, mundo!", "Wellington Nora"]
nested_list = [[1,2,3], "Wellington Nora", 1.5]

print(nested_list)

#len()
print(len(lista_inteiro))
print(len(nested_list))

#append()
lista_inteiro.append(6)
print(lista_inteiro)

#insert()
lista_inteiro.insert(0, "Wellington Nora")
print(lista_inteiro)

#remove()
lista_inteiro.remove("Wellington Nora")
print(lista_inteiro)

#index()
print(nested_list.index([1, 2, 3]))

#count()
print(lista_inteiro.count(3))

#sort()
lista_inteiro.sort(reverse=True)
print(lista_inteiro)