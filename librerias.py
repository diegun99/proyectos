#Importar una librería
import math

def solicitar_entero(texto_solicitud):
    while True:
        try:
            numero = int(input(texto_solicitud + " "))
        except ValueError:
            print("Eso no es un número entero, vuelve a intentarlo")
        else:
            if numero >= 1 and numero <= 3:
                break
            else:
                print("No es una opción válida")
    return numero

def solicitar_positivo(texto_solicitud):
    while True:
        try:
            numero = float(input(texto_solicitud + " "))
        except ValueError:
            print("Eso no es un número positivo, vuelve a intentarlo")
        else:
            if numero > 0:
                break
            else:
                print("No es una opción válida")
    return numero

def resolver_cuadrado():
    lado = solicitar_positivo("Digita el lado del cuadrado")
    area = math.pow(lado, 2)
    return area

def resolver_triangulo():
    base = solicitar_positivo("Digita la base del triángulo")
    altura = solicitar_positivo("Digita la altura del triángulo")
    area = base * altura / 2
    return area

def resolver_circulo():
    radio = solicitar_positivo("Digita el radio del circulo")
    area = math.pi * math.pow(radio, 2)
    return area

#Este programa halla el área de varias figuras geométricas
print("Escoge una figura geométrica")
print("1. Cuadrado\n2. Triángulo\n3. Círculo")
opcion = solicitar_entero("Tu opción")

if opcion == 1: #Cuadrado
    area = resolver_cuadrado()
elif opcion == 2:
    area = resolver_triangulo()
else:
    area = resolver_circulo()

print("El área de la figura es", area)