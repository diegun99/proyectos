#Este programa solicita las notas de un estudiante y las agrega a un archivo

#Se abre el archivo
arch_notas = open("archivos/notas_estudiante.txt", "r")

#Primero se lee el contenido del archivo
dicc_notas = {}
for linea in arch_notas:
    linea = linea.replace("\n", "")
    lista_datos = linea.split(";")
    try:
        lista_datos[1] = float(lista_datos[1])
    except ValueError:
        print("Linea de títulos")
    else:
        dicc_notas[lista_datos[0].lower()] = lista_datos

print("Lectura inicial", dicc_notas)
arch_notas.close()


print("Este programa solicita las notas de un estudiante y las guarda en un archivo.")
cantidad = int(input("¿Cuántas notas vas a agregar? "))

for i in range(cantidad):
    materia = input("Materia " + str(i + 1) + ": ")
    nota = float(input("Nota: "))
    dicc_notas[materia.lower()] = [materia, nota]

print("Modificado", dicc_notas)

#Ahora abrimos el archivo para escritura
arch_notas = open("Archivos/notas_estudiante.txt", "w")
for llave in dicc_notas:
    lista_datos = dicc_notas[llave]
    arch_notas.write(lista_datos[0] + ";" + str(lista_datos[1]) + "\n")

arch_notas.close()