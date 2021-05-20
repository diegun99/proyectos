#lista vacia
lista_vacia = []

#lista con elementso

lista_numeros = [1,3,5]

#imprimir listas
print(lista_vacia)
print(lista_numeros)

print(lista_numeros[0])

#solicitaremos una posicion

#probando try catch except

try:
    print(lista_numeros[10])
except IndexError as err:
    print("ha ocurrido un error", err)

    #Solicitar el último elemento de la lista
    print("el último elemento es ", lista_numeros[-1])

