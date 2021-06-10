#Las cadenas de texto secomportan de forma parecida a las listas
texto = input("Escribe tu primer nombre ").capitalize().replace(",", ".")
print(texto)

print("Tu nombre tiene " + str(len(texto)) + " letras.")
if len(texto) > 0:
    print("La primera letra de tu nombre es la " + texto[0])

lista_letras = []
for x in texto:
    lista_letras.append(x)

print(lista_letras)

print("Tu nombre en mayúsculas es " + texto.upper())
print("Tu nombre en minúsculas es " + texto.lower())