#este programa solicita los datos de varios estudiantes y posteriormente los imprime en pantalla
cantidad = int(input("¿Cuántos estudiantes a a registrar? "))
listaEstudiantes = []
for i in range(cantidad):
    nombres = input("Nombres del estudiante número "+ str(i+1)+": ")
    apellidos = input("Apellido del estudiante número "+ str(i+1)+": ")
    documento = input("Documento del estudiante "+ str(i+1)+": ")
    edad = int(input("Edad del estudiante"+ str(i+1)+": "))

    persona = [nombres, apellidos,documento,edad]

    listaEstudiantes.append(persona)

## imprimir datos

print("\n\nListado de estudiantes : ")
for estudiante in listaEstudiantes :
    print("Nombre,",estudiante[0],"Apellido: ",apellidos[i])
