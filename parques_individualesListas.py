
#Este programa solicitará la información de un grupo de parques y nos dirá cuál es el menor y cuál es el mayor
print("Este programa te solicitará la información de algunos parques")
cantidad = int(input("¿Cuántos parques deseas registrar? "))

#Con listas individuales
lista_nombres = []
lista_direcciones = []
lista_areas = []
for indice in range(cantidad):
    nombre = input("Nombre del parque: ")
    direccion = input("Dirección: ")
    area = float(input("Área (metros cuadrados): "))

    lista_nombres.append(nombre)
    lista_direcciones.append(direccion)
    lista_areas.append(area)

indice_menor = 0
for indice in range(len(lista_nombres)):
    if lista_areas[indice] < lista_areas[indice_menor]:
        indice_menor = indice

print("El parque más pequeño es", lista_nombres[indice_menor], "con un área de", lista_areas[indice_menor], "metros cuadrados")