# Este programa pide las notas de un curso y saca el promedio
# notas entre 0 y 5

num_notas = 0

while num_notas <=0 or num_notas >=7 :
    try:
        num_notas = int(input("¿Cuántas notas son?"))
    except ValueError :
        num_notas = 0


#Ahora pido las notas
lista_nombres = []
lista_notas = []

for i in range(num_notas):
    lista_nombres.append(input("¿Cuál es el tipo de nota?"))

    nota_aux = -1
    # me deben entregar una nota de 0 a 5
    while nota_aux < 0 or nota_aux >5 :
        try:
            nota_aux = float(input("¿Cuál es la nota?"))
        except ValueError:
            nota_aux = -1
    
    lista_notas.append( nota_aux)

#Sumo las notas
suma = 0
for nota_aux in lista_notas:
    suma+= nota_aux

promedio = suma /len(lista_notas)

print("\n")
for i in range(len(lista_notas)):
    print(lista_nombres[i], lista_notas[i])

print("Su promedio es",promedio)





