# abrir y leer el archivo
try:
    archivo = open("archivos\Pacientes COVID-19 Quindío Mayo.csv")
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


#Definición de métodos
def numeroDeCasosTotal(arreglo): 
    return len(arreglo)

def numeroTotalCasosIndiceDescripcion( arreglo,indice, descripcion):
    contador = 0
    for i in range (len(arreglo)):
        if arreglo[i][indice]==descripcion:
            contador += 1
    
    return contador

def numeroTotalCasosIndiceDescripcionPorQuinquenio( arreglo,indice, descripcion):# clasifica segun la descripción y por quinquenios
    contador = 0
    resultado = []
    for i in range (len(arreglo)):
        if arreglo[i][indice]==descripcion:
            aux = arreglo[i]
            resultado.append(aux)
            contador += 1
    
    quinFallecido= quinquenio(resultado)

    
    return quinFallecido

def quinquenio(arreglo):
    inicial =0
    final = 4
    arregloQuinque = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for j in range(len(arregloQuinque)-1):# recorre cada indice y luego evalua todos los datos
        for i in range(len(arreglo)):# evalua cada registro y lo guarda en  el quinque adecuado
            if arreglo[i][4] >=inicial and arreglo [i][4]<=final:
                arregloQuinque[j]+=1
        inicial+=5
        final+=5


    for l in range(len(arreglo)):## for  para contar los mayores 80 y almacenarlos en la ultima posición
        if arreglo[l][4] >=80:
         arregloQuinque[16]+=1


    return arregloQuinque

#Leer archivo para crear diccionario por municipio
def obtenerporMunicipio():
    #Se abre el archivo
    archivo = open("archivos\Pacientes COVID-19 Quindío Mayo.csv")

    #Primero se lee el contenido del archivo
    dicc_municipios = {}
    contador = 0
    for linea in archivo:
        if contador > 0:
            linea = linea.replace("\n", "")
            lista_datos = linea.split(";")
            try:
                dicc_municipios[lista_datos[2]] += 1 
            except KeyError:
                dicc_municipios[lista_datos[2]]  = 1 
        contador+=1

    archivo.close()

    return dicc_municipios

def obtenerfallecidosPorMunicipio():
    #Leer archivo para crear diccionaio fallecidos por municipio
    #Se abre el archivo
    archivo = open("archivos\Pacientes COVID-19 Quindío Mayo.csv")

    #Primero se lee el contenido del archivo
    dicc_municipiosFallecidos = {}
    contador = 0
    for linea in archivo:
        if contador > 0:
            linea = linea.replace("\n", "")
            lista_datos = linea.split(";")
            if lista_datos[7] == "Fallecido":
                try:
                    dicc_municipiosFallecidos[lista_datos[2]] += 1 
                except KeyError:
                    dicc_municipiosFallecidos[lista_datos[2]]  = 1 
        contador+=1

    archivo.close()

    return dicc_municipiosFallecidos


def obtenerPromedioEdadFallecidos( arreglo,indice, descripcion):
    contador = 0
    sumaEdad = 0
    for i in range (len(arreglo)):
        if arreglo[i][indice]==descripcion:
            sumaEdad+=arreglo[i][4]
            contador +=1
    
    return sumaEdad/contador



#principal
#1 número total casos
casosTotal = numeroDeCasosTotal(lista_municipios)

#2 números activos
activos = numeroTotalCasosIndiceDescripcion(lista_municipios,7,"Activo")

#3 números fallecidos
fallecidos = numeroTotalCasosIndiceDescripcion(lista_municipios,7,"Fallecido")

#4 números femenino
femenino = numeroTotalCasosIndiceDescripcion(lista_municipios,5,"F")

#4 números masculino
masculino = numeroTotalCasosIndiceDescripcion(lista_municipios,5,"M")

# 5 numero total por quinquenio
quinquenios = quinquenio(lista_municipios)

#6 numero total fallecidos quinquenio
quinFallecidos = numeroTotalCasosIndiceDescripcionPorQuinquenio(lista_municipios,7,"Fallecido")

#7 numero casos por poblacion
municipios = obtenerporMunicipio()

#8 numero casos fallecidos por poblacion
municipiosF = obtenerfallecidosPorMunicipio()

#9 Promedio edad Fallecidos 
edadPromedioF = obtenerPromedioEdadFallecidos(lista_municipios,7,"Fallecido")

#10  Porcentaje de casos que corresponden a la ciudad de Armenia (código 63001).

numCasosArmenia= ( municipios["ARMENIA"]/casosTotal)*100




print(casosTotal)
print(activos)
print(fallecidos)
print(femenino)
print(masculino)
print(quinquenios)
print(quinFallecidos)
print(municipios)
print(municipiosF)
print(edadPromedioF)
print(numCasosArmenia)


continuarSesion="si"
opcion = 0

while continuarSesion=="si":
   

    print("1)Número total de casos.")
    print("2)Número total de casos activos.")
    print("3)Número total de fallecidos.")
    print("4)Número total de casos por sexo.")
    print("5)Número total de casos por quinquenio.")
    print("6)Número total de fallecidos por quinquenio.")
    print("7)Número de casos de cada municipio.")
    print("8)Número de fallecidos de cada municipio.")
    print("9)Promedio de edad de los fallecidos.")
    print("10)Porcentaje de casos que corresponden a la ciudad de Armenia (código 63001).")

    while True:
        try:
            opcion = int(input("digite la opción a consultar: "))
        except ValueError:
            print("No puedes escribir letras")

        else:
            break


    if opcion == 1:
        print("1)Número total de casos: ",casosTotal )
    elif opcion == 2:
        print("2)Número total de casos activos: ",activos)
    elif opcion == 3:
        print("3)Número total de fallecidos: ",fallecidos)
    elif opcion == 4:
        print("4)Número total de casos por sexo: \n")
        print("Masculino: ",masculino)
        print("Femenino: ",femenino)
    elif opcion == 5:
        print("5)Número total de casos por quinquenio: \n")
        ini=0
        final=4
        for i in range(len(quinquenios)-1):
            print("De ",ini," a ",final," años: ",quinquenios[i])
            ini+=5
            final+=5
        print("De 80 años o más: ",quinquenios[16])
    elif opcion == 6:
        print("6)Número total de fallecidos por quinquenio: \n")
        ini=0
        final=4
        for i in range(len(quinFallecidos)-1):
            print("De ",0," a ",final," años: ",quinFallecidos[i])
            ini+=5
            final+=5
        print("De 80 años o más: ",quinFallecidos[16])
    elif opcion == 7:
        print("7)Número de casos de cada municipio: ")
        for llave in municipios:
            valor = municipios[llave]
            print(llave," : ",valor,". ")
    elif opcion == 8:
        print("8)Número de fallecidos de cada municipio.")
        for llave in municipiosF:
            valor = municipiosF[llave]
            print(llave," : ",valor,". ")
    elif opcion == 9:
        print("9)Promedio de edad de los fallecidos: ", edadPromedioF)
    elif opcion == 10:
        print("10)Porcentaje de casos que corresponden a la ciudad de Armenia (código 63001): ",numCasosArmenia,"%")





    continuarSesion= input("desea realizar otra Consulta? (si/no): ")

