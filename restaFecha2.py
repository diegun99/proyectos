#Este programa usa una librería para maniúlar fechas
import datetime

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

def solicitar_fecha():
    while True:
        año = solicitar_entero("Año", 1900, 9999)
        mes = solicitar_entero("Mes", 1, 12)
        dia = solicitar_entero("Día", 1, 31)

        try:
            fecha_ini = datetime.date(año, mes, dia)
        except ValueError:
            print("No es una fecha válida")
        else:
            break
    
    return fecha_ini

#Programa principal
print("Danos la fecha inicial")
fecha_ini = solicitar_fecha()

print("Danos la fecha final")
fecha_fin = solicitar_fecha()

#Se restan las fechas
diferencia = fecha_fin - fecha_ini

print("El número de días entre las fechas es " + str(diferencia.days))