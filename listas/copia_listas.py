import copy

# deep copy
nested_list = [[1,2,3], "Wellington Nora", 1.5]
copia_lista = copy.deepcopy(nested_list)

nested_list[0][1] = 4
print(nested_list)
print(copia_lista)

#Shallow list
outra_lista = copy.copy(nested_list)
nested_list[0][1] = 10
print(nested_list)
print(outra_lista)