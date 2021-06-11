def ordenar_lista(lista, indice):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j][indice] < lista[i][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

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
    ordenar_lista(lista_municipios, 4)

    print("Los 10 municipios más poblados de Colombia son:")
    for i in range(-1, -11, -1):
        print(lista_municipios[i][3] + " (" + ("{:,}".format(lista_municipios[i][4])).replace(",", ".") + " habitantes)")