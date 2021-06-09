#Este programa solicitará la información de un grupo de parques y nos dirá cuál es el menor y cuál es el mayor
print("Este programa te solicitará la información de algunos parques")
cantidad = int(input("¿Cuántos parques deseas registrar? "))

#Con diccionarios
lista_parques = []
for indice in range(cantidad):
    nombre = input("Nombre del parque " + str(indice + 1) + ": ")
    direccion = input("Dirección: ")

    #Nos aseguramos de recibir un área válida
    while True:
        try:
            area = float(input("Área (metros cuadrados): "))
        except ValueError:
            print("El área debe ser un número")
        else:
            break

    parque = {
        "Nombre" : nombre,
        "Dirección" : direccion,
        "Área" : area
    }

    lista_parques.append(parque)

parque_menor = lista_parques[0]
parque_mayor = lista_parques[0]
for parque in lista_parques:
    if parque["Área"] < parque_menor["Área"]:
        parque_menor = parque
    if parque["Área"] > parque_mayor["Área"]:
        parque_mayor = parque

print("El parque más pequeño es", parque_menor["Nombre"], "con un área de", parque_menor["Área"], "metros cuadrados")
print("El parque más grande es", parque_mayor["Nombre"], "con un área de", parque_mayor["Área"], "metros cuadrados")