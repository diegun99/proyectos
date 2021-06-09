#Voy a declarar un diccionario con los datos de una persona
persona = {
    "Nombres" : "Feisar Enrique",
    "Apellidos" : "Moreno Corzo",
    "Teléfono" : "3182208951",
    "Edad" : 42,
    "Ciudad" : "Bucaramanga"
}
print(persona)

#Ahora voy a recorrer mi diccionario
print("--Imprimo las llaves--")
for x in persona:
    print(x)

print("--Imprimo los valores--")
for x in persona:
    print(persona[x])

print("--Imprimo las llaves de una segunda forma--")
for x in persona.keys():
    print(x)

print("--Imprimo los valores de una segunda forma--")
for x in persona.values():
    print(x)