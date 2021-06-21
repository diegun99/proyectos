"""El Laboratorio Clínico del Sur ha tenido últimamente varias quejas por parte de algunos de sus usuarios.
 Las quejas hacen referencia a la demora los procesos de asignación de citas de toma de muestras y de entrega de resultados. 
 Cuando un usuario llama, se le debe asignar una cita para los próximos 2 días como máximo, y los resultados de las pruebas se deben entregar máximo 3 días después de la toma de la muestra.
  Por ejemplo, si un usuario llamó a pedir cita el 25 de abril de 2021, su cita debió quedar agendada máximo para el 27 de abril del mismo año;
   si una cita de toma de muestras fue realizada el 14 de abril de 2021, el resultado de la misma debió ser entregado máximo el 17 de abril.

Durante el mes pasado se recibieron más quejas de lo habitual, por lo que el laboratorio clínico quiere revisar todas las atenciones y entregas de resultados de ese mes.
 Es por esto que requiere que su desarrollador de software (tú) cree un programa en Python en el que se soliciten las fechas de solicitud,
  cita y entrega de muestras (3 fechas) de cada uno de los pacientes, junto con su nombre completo, número de documento y teléfono de contacto;
   en cada caso debe calcular los días pasados entre la llamada y la cita, y entre la cita y la entrega de resultados,
    si estos días superan alguno de los límites establecidos, se deben agregar los datos de dicho paciente a un listado aparte para su posterior impresión en pantalla.
     También se deben imprimir al final las cantidades de pacientes que superaron los tiempos establecidos como límite.

La aplicación debe pedir los datos de un paciente, después preguntar si se desean agregar los datos de otro paciente y seguir solicitando datos hasta que se le solicite no hacerlo.

El reporte de resultados solamente se debe imprimir después de solicitar los datos de todos los pacientes y debe seguir el formato del siguiente ejemplo:

PACIENTES CON TIEMPOS DE ESPERA SUPERIORES A LO ESTABLECIDO


1) Ana María González Roa – 1 días entre llamada y cita, 4 días entre cita y resultados – Teléfono: 3153153131


2) Juan Manuel Pérez Gómez – 5 días entre llamada y cita, 2 días entre cita y resultados – Teléfono: 3103103131''

2) Diana García García – 7 días entre llamada y cita, 6 días entre cita y resultados – Teléfono: 3003003030
 

Total de pacientes con tiempos superiores: 3"""

 

#fecha solicitud
#fecha  cita
#fecha  entrega muestras

# nombre completo
#numer de documento
# telefono de contacto

#listado aparte  si superan los limites establecidos
# mostrar cantidad de pacientes que superan los tiempso establecidos








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


solicitar_fecha()