#Voy a declarar un diccionario con los datos de una persona
persona = {
    "Nombres" : "Feisar Enrique",
    "Apellidos" : "Moreno Corzo",
    "Teléfono" : "3182208951",
    "Edad" : 42,
    "Ciudad" : "Bucaramanga",
    15: True
}
print(persona)

#Yo puedo acceder a los elementos de un diccionario por su nombre
print("El nombre de la persona es", persona["Nombres"])

#Vamos a agregarle una nueva variable con valor al diccionario
nombre_llave = input("¿Cuál es el nombre de la nueva llave? ")
valor = input("¿Cuál es su valor? ")

persona[nombre_llave] = valor
print("La persona ha cambiado")
print(persona)

print(persona[15])