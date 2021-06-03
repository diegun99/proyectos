milista = [1,2,3,2,3]

milista.insert(3,4)

#reemplazo el indice 4 por una lista
milista[4] = ["a","b","c"]
print(milista)

#construir una matriz
print("\nAhora voy a trabajar con matrices")

mimatriz = []
mimatriz.append([1,6,11,16])
mimatriz.append([2,7,12,17])
mimatriz.append([3,8,13,18])
mimatriz.append([2,5,12,19])
mimatriz.append([2,2,33,28])

print(mimatriz)

mimatriz2 = [[1, 6, 11, 16], [2, 7, 12, 17], [3, 8, 13, 18], [2, 5, 12, 19], [2, 2, 33, 28]]


print("voy a hallar el valor de la fila 2 columna 3")

print(mimatriz[2][3])

#voya a agregar una columna con todos los valores iguales a 10
for fila in mimatriz:
    fila.append(10)

print(mimatriz)   