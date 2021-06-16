import time

#Este algoritmo implementa el merge sort
def ordenar_lista(lista, indice):
    if len(lista) > 1:
        #Primera parte, división de listas
        medio = len(lista) // 2 # doble // significa división entera
        lista_izquierda = lista[:medio]
        lista_izquierda = ordenar_lista(lista_izquierda, indice)
        lista_derecha = lista[medio:]
        lista_derecha = ordenar_lista(lista_derecha, indice)

        #Segunda parte, unir las listas
        lista_ordenada = []
        cont_izq = 0
        cont_der = 0
        while len(lista_ordenada) < len(lista):
            if cont_izq == len(lista_izquierda):
                #Ya se agregó toda la lista izquierda, se agrega lo que falta de la derecha
                lista_ordenada += lista_derecha[cont_der:]
            elif cont_der == len(lista_derecha):
                #Ya se agregó toda la lista derecha, se agrega lo que falta de la izquierda
                lista_ordenada += lista_izquierda[cont_izq:]
            else:
                if lista_izquierda[cont_izq][indice] < lista_derecha[cont_der][indice]:
                    lista_ordenada.append(lista_izquierda[cont_izq])
                    cont_izq += 1
                else:
                    lista_ordenada.append(lista_derecha[cont_der])
                    cont_der += 1
    else:
        lista_ordenada = lista
       
    return lista_ordenada

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
    lista_municipios = ordenar_lista(lista_municipios, 4)
    fin = time.time()
    print("El tiempo tomado para ordenar la lista fue de " + str(fin - inicio) + " segundos")

    print("Los 10 municipios más poblados de Colombia son:")
    for i in range(-1, -11, -1):
        print(lista_municipios[i][3] + " (" + ("{:,}".format(lista_municipios[i][4])).replace(",", ".") + " habitantes)")