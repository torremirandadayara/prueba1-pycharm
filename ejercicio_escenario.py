mi_lista = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]

resultado = []

for element in mi_lista:
    if element not in resultado:
        resultado.append(element)

print(resultado)
