nombres = ["Ana", "Sonia", "Helena"]
nombres2 = ["Miguel", "Carlos", "Juan"]
nombresFinales = [nombres, nombres2]
print("Imprimiendo valor [0] [1]", nombresFinales[0][1])
print("Lista completa: ", nombresFinales)

for i in range(len(nombresFinales)):
    print("\n")
    if i == 0:
        print("###### NOMBRES FEMENINOS ######")
    elif i == 1:
        print("###### NOMBRES MASCULINOS ######")
    for j in range(len(nombresFinales[i])):
        print(nombresFinales[i][j], end=", ")
