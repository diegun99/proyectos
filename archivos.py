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

    #Ya se leyó el archivo y se agregó su contenido a una lista
    #Ahora vamos a hallar el de menor población y el de mayor población
    municipio_menor = lista_municipios[0]
    municipio_mayor = lista_municipios[0]
    poblacion_total = 0
    for municipio in lista_municipios:
        poblacion_total += municipio[4]
        if municipio[4] < municipio_menor[4]:
            municipio_menor = municipio
        if municipio[4] > municipio_mayor[4]:
            municipio_mayor = municipio

    #Se imprimen el menor y el mayor
    print("El municipio de menor población es " + municipio_menor[3] + ", en el departamento de " + municipio_menor[1] + " con una población de " + ("{:,}".format(municipio_menor[4])).replace(",", ".") + " habitantes")
    print("El municipio de mayor población es " + municipio_mayor[3] + ", en el departamento de " + municipio_mayor[1] + " con una población de " + ("{:,}".format(municipio_mayor[4])).replace(",", ".") + " habitantes")
    print("La población de Colombia es de " + ("{:,}".format(poblacion_total)).replace(",", ".") + " habitantes")