cantidad = int(input("¿Cuántos números quieres ingresar?"))

#crear una lista vacía
lista_numeros = []
print("ingresa los números")

while len(lista_numeros)  < cantidad:
    try:
        numero = int(input())
    except ValueError:
        print("no es un numero valido")
    else:
        lista_numeros.append(numero)
    

print("Los números entregados son ",lista_numeros)

for indice in range(-1,-cantidad-1,-1):
    print(lista_numeros[indice])

