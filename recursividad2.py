def limpiar_espacios_intermedios(texto):
    texto = texto.replace("  ", " ")
    try:
        posicion = texto.index("  ")
    except ValueError:
        return texto
    else:
        texto = limpiar_espacios_intermedios(texto)
        return texto

def ajustar_nombre(nombre):
    texto_ajustado = nombre.strip().lower()

    texto_ajustado = limpiar_espacios_intermedios(texto_ajustado)

    lista_palabras = texto_ajustado.split(" ")
    texto_ajustado = ""
    for palabra in lista_palabras:
        texto_ajustado = texto_ajustado + " " + palabra.capitalize()

    texto_ajustado = texto_ajustado.strip()

    return texto_ajustado

#Principal
texto = "  Feisar          enRiQUE        moreno  CORZO        "
texto_ajustado = ajustar_nombre(texto)
print(texto_ajustado)