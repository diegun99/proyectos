def solicitar_entero(texto_solicitud):
    while True:
        try:
            numero = int(input(texto_solicitud + " "))
        except ValueError:
            print("Eso no es un número entero, vuelve a intentarlo")
        else:
            break
    return numero

#Método con parámatros obligatorios y opcionales
def sumar_varios(a, b = 0, c = 0, d = 0, e = 0):
    #Los parámetros se reciben en una tupla
    resultado = a + b + c + d + e
    return resultado

#Método con un número flexible de parámetros
def sumar(*valores):
    #Los parámetros se reciben en una tupla
    resultado = 0
    for x in valores:
        resultado += x
    return resultado

#Programa principal
num1 = solicitar_entero("Dime el primer número")
num2 = solicitar_entero("Dime el segundo número")
num3 = solicitar_entero("Dime el tercer número")

suma = sumar(num1, num2, num3)

print("La suma de los números es:", suma)