import time

def por_poblacion(municipio):
    return municipio[4]

try:
    archivo = open("Archivos/Población Colombia 2021.txt")
except FileNotFoundError:
    print("El archivo no existe")
else:
    #Leer el archivo completo y copiarlo en una lista
    #lista_lineas = archivo.readlines()
    #print(lista_lineas)

    lista_municipios = []
    for linea in archivo:
        linea = linea.replace("\n", "")
        lista_datos = linea.split(";")
        try:
            lista_datos[4] = int(lista_datos[4])
        except ValueError:
            print("Linea de títulos")
        else:
            lista_municipios.append(lista_datos)

    #Ordenar la lista por población
    inicio = time.time()
    lista_municipios.sort(key=por_poblacion)
    fin = time.time()
    print("El tiempo tomado para ordenar la lista fue de " + str(fin - inicio) + " segundos")

    print("Los 10 municipios más poblados de Colombia son:")
    for i in range(-1, -11, -1):
        print(lista_municipios[i][3] + " (" + ("{:,}".format(lista_municipios[i][4])).replace(",", ".") + " habitantes)")