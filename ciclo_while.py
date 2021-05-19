print("este programa seguira solicitando un número hasta que ingrese un cero")
numero = float(input("digite un numerito : "))
suma = 0 #acumulador
contador = 0#contador
while numero !=0 :
    suma +=numero
    contador += 1
    print(" la suma de los números es: ", suma)
    promedio = suma / contador
    print(" el promedio es: ",promedio)

    if suma >100:
        print("pasaste de 100")
        break;


    numero = float(input("digite un numerito : "))

print(" la suma de los números es: ", suma)
if contador > 0 : 
   
    print(" el promedio es: ",promedio)
else:
    print(" no puede  obtener un promedio  dado que no ingresaste ningun numero diferente de cero")

