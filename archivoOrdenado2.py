try:
    archivo = open("Archivos/Población Colombia 2021.txt")
except FileNotFoundError:
    print("El archivo no existe")
else:
    #Leer el archivo completo y copiarlo en una lista
    #lista_lineas = archivo.readlines()
    #print(lista_lineas)

    lista_municipios = []
    lista_poblacion = []
    lista_cod_mun = []
    for linea in archivo:
        linea = linea.replace("\n", "")
        lista_datos = linea.split(";")
        try:
            lista_datos[4] = int(lista_datos[4])
        except ValueError:
            print("Linea de títulos")
        else:
            lista_municipios.append(lista_datos)
            lista_poblacion.append([lista_datos[4], lista_datos])
            lista_cod_mun.append([lista_datos[2], lista_datos])

    #Ordenar la lista de población
    lista_poblacion.sort()

    print("Los 10 municipios más poblados de Colombia son:")
    for i in range(-1, -11, -1):
        print(lista_poblacion[i][1][3] + " (" + ("{:,}".format(lista_poblacion[i][0])).replace(",", ".") + " habitantes)")