minha_tupla = (1, 2, 3, "Olá, mundo", False)
minha_tupla2 = (1, 2, 3, "Olá, mundo", True)

# Count()
print(minha_tupla.count(-1))

# Index()
print(minha_tupla.index("Olá, mundo"))

# Verifica a existência de um elemento
print("Ola, mundo" in minha_tupla)

# Concatenar tuplas
minha_tupla3 = minha_tupla.__add__(minha_tupla2)
print(minha_tupla.__add__(minha_tupla2))
print(minha_tupla3)