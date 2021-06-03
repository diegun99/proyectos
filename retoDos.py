continuarSesion = "si"
while continuarSesion=="si":

    nit = 0
    nombre = ""
    montoTotal = 0
    listaProveedor = []
    valores =[]
    promedio = 0




    #pedir datos de las 5 cotizaciones
    for i in range(5):# se piden los datos
        continuar = True
        nit = input("Digite el número nit de empresa "+ str(i+1)+": ")
        nombre = input("Digite el nombre de la empresa "+str(i+1)+": ")
        while continuar :# se itera en caso de que el usuario no digite números
            try:
                montoTotal= int(input("Digite el valor total de la cotización "+str(i+1)+": "))
            except ValueError as err:
                print("No se permiten letras")
            else:
                continuar = False
        proveedor = [nit,nombre,montoTotal]# se asigna en arreglo los datos del proveedor
        valores.append(montoTotal)# se asigna en el arreglo los datos de los valores
        
        listaProveedor.append(proveedor)



    print(listaProveedor)
    #nit,nombre y valor de las cotizaciones más altas y mas baja
    #mas alta
    alto= max(valores)
    listaAlto =[]
    #mas bajo
    bajo = min(valores)
    listaBajo = []



    for i in range(len(listaProveedor)):
        aux = listaProveedor[i][2]# auxiliar igual a la posicion del valor
        if aux == alto:
            listaAlto.append(listaProveedor[i])
        if aux == bajo:
            listaBajo.append(listaProveedor[i])
        

    #imprimir el mas bajo

    print("\nCotización más baja")  
    print("NIT: ",listaBajo[0][0]) 
    print("Nombre: ",listaBajo[0][1]) 
    print("Valor: ",listaBajo[0][2]) 

    print("\n")

    print("\nCotización más alta")  
    print("NIT: ",listaAlto[0][0]) 
    print("Nombre: ",listaAlto[0][1]) 
    print("Valor: ",listaAlto[0][2]) 

    print("\n")
    #promedio de las 5 cotizaciones
    acumulador = 0
    for suma in valores:
        acumulador +=suma

    promedio = acumulador/len(valores)

    print("Promedio: ",promedio) 


    continuarSesion= input("Desea realizar una nueva sesión? (si/no): ")

print("sesion finalizada")
# desea realizar una nueva sesión o finalizar


