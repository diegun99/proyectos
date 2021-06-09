mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)
mi_lista.insert(0, 10)
mi_lista[0] = 0
print(mi_lista)

mi_tupla = (1, 2, 3, 4, 5)
mi_tupla2 = mi_tupla
#mi_tupla.append(6) La tupla no tiene append
#mi_tupla.insert(0, 10) La tupla no tiene insert
#mi_tupla[0] = 0
mi_tupla = (10, 20, 30)
print(mi_tupla)
print(mi_tupla2)

#No púedo modificar la tupla, pero si puedo acceder a su contenido
print("El último elemento de la tupla es", mi_tupla[-1])

#Puedo guardar listas dentro de una tupla
mi_tupla3 = ([1, 3, 2], [5, 6, 7, 8], [10, 12, 9, 11])
print(mi_tupla3)
print("Puedo acceder a los elementos de las listas dentro de una tupla")
print("Lista 2, elemento 1:", mi_tupla3[2][1])

#Dado que las listas son modificables, se pueden modificar los valores de las listas que estén dentro de tuplas
mi_tupla3[0].append(4)
mi_tupla3[2].insert(2, 13)
print(mi_tupla3)
mi_tupla3[1].clear()
print(mi_tupla3)

#Voy a crear una tupla con un solo elemento
mi_tupla4 = (5,)
print("El primer elemento de la tupla 4 es:", mi_tupla4[0])

