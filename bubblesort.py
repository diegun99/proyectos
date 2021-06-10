'''#Dada una lista, ordenarla
lista = [7, 4, 9, 5, 11, 0, 2, 7, 14, 3, 1, 10]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if (lista[j] < lista[i]):
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux

print(lista)'''


lista2 = ["hdsfdsfoal","sdaadas","afsdfsdmi","didsfego","errs","aswqc"]
for i in range(len(lista2)):
    for j in range(i + 1, len(lista2)):
        if (len(lista2[j] )< len(lista2[i])):
            aux = lista2[j]
            lista2[j] = lista2[i]
            lista2[i] = aux

print(lista2)
