from collections import deque

minha_fila = deque(["Wellington", "Reginaldo", "Giovane"])
print(minha_fila)

minha_fila.popleft()
print(minha_fila)

minha_fila.append("Maria")
print(minha_fila)