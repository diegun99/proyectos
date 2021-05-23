mi_lista = [2,3,4,5,6,7,8,9]
mi_referencia= mi_lista# apuntando a la misma referencia, solo funciona con objetos
mi_copia = mi_lista[:]
#leer un valor específico

#primer elemento

print(mi_lista[0])


#ultimo elemento
print([-1])

#extraer una parte de la lista
parte = mi_lista[3:]
parte2 = mi_lista[:] #sacar una parte completa y hacerle copia
print(parte)

#invertir lista
mi_lista.reverse()
print(mi_lista)

# ordenar lista
mi_lista.sort()
mi_lista.reverse()
print(mi_lista)
print(mi_copia)

#Quitar elementos de la lista

#quitar una posición específica
del mi_lista[2]
print("lista sin el tercer elemento", mi_lista)

#quitar un elemento por su valor

try:
    mi_lista.remove(7)
except ValueError:
    print("el numero no existe",ValueError)


print(mi_lista)
suma = 0
#sumar los elementos de la lista
for i in range(len(mi_lista)):
    suma+= mi_lista[i]

print(suma)

# alternativa ,recorrer lista con un for each

suma = 0

for valor in mi_lista:
    suma +=  valor
print(suma)



