def factorial(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def solicitar_entero(texto_solicitud):
    while True:
        try:
            numero = int(input(texto_solicitud + " "))
        except ValueError:
            print("Eso no es un número entero, vuelve a intentarlo")
        else:
            break
    return numero

#Programa principal
numero = solicitar_entero("Escribe un número")
resultado = factorial(numero)

print(str(numero) + "! = " + str(resultado))