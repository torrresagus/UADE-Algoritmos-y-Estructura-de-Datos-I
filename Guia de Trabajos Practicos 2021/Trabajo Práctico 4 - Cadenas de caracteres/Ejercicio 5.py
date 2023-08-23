# Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para
# verificar el comportamiento de la misma. Hacer tres versiones de la función, para
# cada uno de los siguientes casos:
#       a. Utilizando sólo ciclos normales
#       b. Utilizando listas por comprensión
#       c. Utilizando la función filter

# a. Utilizando sólo ciclos normales
def filtrar_palabras_ciclos(frase, N):
    palabras = frase.split()
    palabras_filtradas = []

    for palabra in palabras:
        if len(palabra) >= N:
            palabras_filtradas.append(palabra)

    return ' '.join(palabras_filtradas)

# b. Utilizando listas por comprensión
def filtrar_palabras_comprension(frase, N):
    return ' '.join([palabra for palabra in frase.split() if len(palabra) >= N])

# c. Utilizando la función filter
def filtrar_palabras_filter(frase, N):
    return ' '.join(filter(lambda palabra: len(palabra) >= N, frase.split()))

def main():
    # Probamos las funciones
    frase_ejemplo = "La programación en Python es muy intuitiva"
    N_ejemplo = 5

    resultado_a = filtrar_palabras_ciclos(frase_ejemplo, N_ejemplo)
    resultado_b = filtrar_palabras_comprension(frase_ejemplo, N_ejemplo)
    resultado_c = filtrar_palabras_filter(frase_ejemplo, N_ejemplo)

    return resultado_a, resultado_b, resultado_c

main()
