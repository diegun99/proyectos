def imprimir_nombre_completo(nombres, apellidos):
    print(nombres + " " + apellidos)

def solicitar_nombres():
    nombres = input("¿Cuáles son tus nombres? ")
    apellidos = input("¿Cuáles son tus apellidos? ")
    imprimir_nombre_completo(nombres, apellidos)

    return [nombres, apellidos]

#Principal
lista_nombres = solicitar_nombres()
print(lista_nombres)