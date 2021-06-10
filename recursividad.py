def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = n * factorial(n - 1)
        return resultado

#Programa principal
numero = int(input("Escribe in entero mayor o igual a cero: "))
valor = factorial(numero)
print("El factorial del número es", valor)