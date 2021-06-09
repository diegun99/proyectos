#Ejemplos de llamado a funciones de Python
'''dato = input("¿Qué dato quieres entregar? ")
numero = int("5")
texto = str(5)'''

#Mi primera función
def saludo():
    print("Hola")
    print("¿Cómo estás?")

#Ahora voy a crear un método con un parámetro de entrada
def saludo_con_nombre(nombre):
    print("Hola", nombre)

#Programa principal
print("Esta función saluda")
saludo()
texto = input("¿Cómo te llamas? ")
saludo_con_nombre(texto)
