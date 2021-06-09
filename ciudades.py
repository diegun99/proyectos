#Creo mi diccionario de ciudades
ciudades = {
    "68001" : "Bucaramanga",
    "68276" : "Floridablanca",
    "11001" : "Bogotá",
    "05001" : "Medellín",
    "54001" : "Cúcuta",
    "63001" : "Armenia",
    "66001" : "Pereira"
}

repetir = "s"

while repetir == "s" or repetir == "S" or repetir == "SI" or repetir == "si":
    codigo = input("Dime el código de la ciudad: ")

    try:
        ciudad = ciudades[codigo]
        print("La ciudad es", ciudad)
    except KeyError:
        print("No tengo registrado ese código en mi base de datos")

        respuesta = input("¿Quieres agregar el municipio? (s/n) ")
        if respuesta == "s" or respuesta == "S" or respuesta == "SI" or respuesta == "si":
            ciudad = input("Nombre del municipio: ")
            ciudades[codigo] = ciudad

    repetir = input("¿Quieres consultar otro código? (s/n)")