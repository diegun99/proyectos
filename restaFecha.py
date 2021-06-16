#Este programa pide dos fechas y las resta

def solicitar_entero(texto, inicial, final):
    while True:
        try:
            numero = int(input(texto + ": "))
        except ValueError:
            print("Debes escribir un número entre " + str(inicial) + " y " + str(final))
        else:
            if numero < inicial or numero > final:
                print("Debes escribir un número entre " + str(inicial) + " y " + str(final))
            else:
                break
    return numero

def verificar_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        resultado = True
    else:
        resultado = False
    return resultado

def obtener_dias_mes(año, mes):
    #Se evalúa el número máximo de días del mes 
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        max_dias = 30
    elif mes == 2:
        if verificar_bisiesto(año):
            max_dias = 29
        else:
            max_dias = 28
    else:
        max_dias = 31
    
    return max_dias

def solicitar_fecha():
    año = solicitar_entero("Año", 1900, 9999)
    mes = solicitar_entero("Mes", 1, 12)

    #Se evalúael número máximo de días del mes 
    max_dias = obtener_dias_mes(año, mes) 

    dia = solicitar_entero("Día", 1, max_dias)

    #Se retorna la fecha en una lista
    return [año, mes, dia]

#Este método devuelve la diferencia en días de dos fechas si la fecha inicial es menor o igual.
#Si la fecha final es menor, se devuelve -1
def restar_fechas(fecha_fin, fecha_ini):
    resultado = 0

    #Se valida si las fechas corresponden al mismo año
    if fecha_ini[0] == fecha_fin[0]:
        #Es el mismo año

        #Se valida si las fecha corresponden al mismo mes
        if fecha_ini[1] == fecha_fin[1]:
            #Es el mismo mes
            if fecha_ini[2] <= fecha_fin[2]:
                #El día inicial es menor o igual
                resultado = fecha_fin[2] - fecha_ini[2]
            else:
                #El día inicial es mayor, error
                resultado = -1
        else:
            #Mismo año, mes diferente
            if fecha_ini[1] < fecha_fin[1]:
                #Para el mes inicial se calculan los días faltantes hasta el final
                dias_mes_ini = obtener_dias_mes(fecha_ini[0], fecha_ini[1])
                resultado = dias_mes_ini - fecha_ini[2]

                #Se suman los días de los meses intermedios
                for mes_int in range(fecha_ini[1] + 1, fecha_fin[1]):
                    dias_mes = obtener_dias_mes(fecha_ini[0], mes_int)
                    resultado += dias_mes
                
                #se suman los días del mes final
                resultado += fecha_fin[2]
            else:
                #Mes inicial mayor, error
                resultado = -1
    else:
        #Año diferente

        if fecha_ini[0] < fecha_fin[0]:
            #El año inicial es menor

            #Se obtiene el máximo de días del mes inicial
            dias_mes_ini = obtener_dias_mes(fecha_ini[0], fecha_ini[1])

            #Se calcula lo que falta del año inicial hasta el final
            #Faltante del mes inicial
            resultado = dias_mes_ini - fecha_ini[2]
            
            #Meses faltantes hasta el final del año inicial
            if fecha_ini[1] < 12: #Se valida que el mes no sea diciembre
                for mes_fal in range(fecha_ini[1] + 1, 13):
                    dias_mes = obtener_dias_mes(fecha_ini[0], mes_fal)
                    resultado += dias_mes
            
            #Se suman los años intermedios
            for año_int in range(fecha_ini[0] + 1, fecha_fin[0]):
                if verificar_bisiesto(año_int):
                    resultado += 366
                else:
                    resultado += 365
            
            #Se suman los meses anteriores de la fecha final
            if fecha_fin[1] > 1:
                for mes_ant in range(1, fecha_fin[1]):
                    dias_mes = obtener_dias_mes(fecha_fin[0], mes_ant)
                    resultado += dias_mes
            
            #Se suman los días del mes final
            resultado += fecha_fin[2]
        else:
            #El año inicial es mayor, error
            return -1
    
    return resultado

#Programa principal
print("Danos la fecha inicial")
fecha_ini = solicitar_fecha()

print("Danos la fecha final")
fecha_fin = solicitar_fecha()

#Restar las fechas
diferencia = restar_fechas(fecha_fin, fecha_ini)

if diferencia >= 0:
    print("El número de días entre las fechas es " + str(diferencia))
else:
    print("La fecha inicial el mayor a la fecha final, no se efectúa la resta")