meu_dicionario_1 = {"Nome" : "Wellington", "Sobrenome" : "Nora", "Idade" : 24}

print(meu_dicionario_1)

# for key, value in meu_dicionario_1.items():
#     print(f"{key} : {value}")

print(meu_dicionario_1.get("Idade"))
print(meu_dicionario_1["Idade"])

# Len
print(len(meu_dicionario_1))

# Pop
meu_dicionario_1.pop("Sobrenome")
print(meu_dicionario_1)

# Clear
# meu_dicionario_1.clear()
# print(meu_dicionario_1)

# Keys
print(meu_dicionario_1.keys())

# Adicionando elementos
meu_dicionario_1["Profissão"] = 'Programador'
meu_dicionario_1.update({"Cidade" : "São João da Boa Vista"})
print(meu_dicionario_1)
