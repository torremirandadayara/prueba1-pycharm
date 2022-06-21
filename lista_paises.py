paises = []
for x in range(5):
    nombre = input("Ingrese el nombre de país: ")
    paises.append(nombre)
for k in range(4):
    for x in range(4):
        if paises[x] > paises[x + 1]:
            aux = paises[x]
            paises[x] = paises[x + 1]
            paises[x + 1] = aux
print("Lista de países: ")
print(paises)
