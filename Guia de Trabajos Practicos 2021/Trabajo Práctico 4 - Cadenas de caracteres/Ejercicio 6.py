# Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
# indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
# como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
# 7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
# resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
#       a. Utilizando rebanadas
#       b. Sin utilizar rebanadas

# a. Utilizando rebanadas
def extraer_subcadena_rebanadas(cadena, posicion, cantidad):
    return cadena[posicion:posicion+cantidad]

# b. Sin utilizar rebanadas
def extraer_subcadena(cadena, posicion, cantidad):
    resultado = ''
    for i in range(posicion, posicion+cantidad):
        if i < len(cadena):  # Asegurarse de que no exceda la longitud de la cadena
            resultado += cadena[i]
    return resultado

def main():
    cadena_ejemplo = "El número de teléfono es 4356-7890"
    posicion_ejemplo = 25
    cantidad_ejemplo = 9

    resultado_a = extraer_subcadena_rebanadas(cadena_ejemplo, posicion_ejemplo, cantidad_ejemplo)
    resultado_b = extraer_subcadena(cadena_ejemplo, posicion_ejemplo, cantidad_ejemplo)
    
    return resultado_a, resultado_b

main()
