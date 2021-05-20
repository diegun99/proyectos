print("clínica dental Sonrisas Blancas S.A. ")
print("digite los siguientes datos : ")

nombre = input("Digite su Nombre: ")
apellido = input("Digite su Apellido: ")
direccion = input("Digite su dirección de residencia: ")
telefono= input("Digite su teléfono de contacto: ")
sexo = input("Digite su genero (masculino/femenino): ")

print("Digite su fecha de nacimiento")
dian = int(input("Digite el día de nacimiento: "))
mesn = int(input("Digite el mes de nacimiento: "))
añon = int(input("Digite el año de nacimiento: "))

print("Digite la fecha de realización del procedimiento")
diap = int(input("Digite el día de  realización del procedimiento: "))
mesp = int(input("Digite el mes de  realización del procedimiento: "))
añop = int(input("Digite el año de  realización del procedimiento: "))


edad = 0
ciclo_vital = ""
seguimiento_edad=""

# calcular edad
if mesp>mesn and diap<=dian :
	edad = añop-añon
else:
	if mesp>=mesn and diap>=dian :
		edad = añop-añon
	else:
		if mesp<mesn and diap<dian :
			edad = añop-añon-1
		else:
			edad = añop-añon-1

#calcular ciclo vital

if edad >= 0 and edad <= 5:
    ciclo_vital= "Primera infancia"
else:
    if edad >= 6 and edad <= 11:
        ciclo_vital= "Infancia"
    else:
        if edad >= 12 and edad <= 18:
            ciclo_vital= "Adolescencia"
        else:
            if edad >= 19 and edad <= 26:
                ciclo_vital= "Juventud"
            else:
                if edad >= 27 and edad <= 59:
                    ciclo_vital= "Adultez"
                else:
                    if edad >= 60 :
                        ciclo_vital= "Persona mayor"
                    else:
                        "no valido"



#Seguimiento vejez
# si es multiplo y edad es menor de 55
if edad % 5 == 0 and edad <=55:
    seguimiento_edad= "Es"
else:
    seguimiento_edad = "No es"


print("Ficha Paciente")

print("Nombre: ",nombre,apellido)
print("Dirección: ",direccion)
print("Teléfono: ", telefono)
print("Sexo: ",sexo)
print("Edad: ",edad ," años")
print("Ciclo vital: ",ciclo_vital)
print(seguimiento_edad,"necesario seguimiento detallado por edad")









