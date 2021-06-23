#Este programa solicita las notas de un estudiante y las agrega a un archivo JSON
import json

#Se abre el archivo
arch_notas = open("archivos/notas_estudiante.json", "r")

#Primero se lee el contenido del archivo
dicc_notas = json.load(arch_notas)

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
arch_notas = open('Archivos/notas_estudiante.json', 'w')
json.dump(dicc_notas, arch_notas)
arch_notas.close()