# Escribir una función para eliminar una subcadena de una cadena de caracteres, a
# partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
# Escribir una función para cada uno de los siguientes casos:
#       a. Utilizando rebanadas
#       b. Sin utilizar rebanadas

# a. Utilizando rebanadas
def eliminar_subcadena_rebanadas(cadena, posicion, cantidad):
    return cadena[:posicion] + cadena[posicion+cantidad:]

# b. Sin utilizar rebanadas
def eliminar_subcadena(cadena, posicion, cantidad):
    resultado = ''
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            resultado += cadena[i]
    return resultado

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion_ejemplo = 25
    cantidad_ejemplo = 9

    resultado_a = eliminar_subcadena_rebanadas(cadena, posicion_ejemplo, cantidad_ejemplo)
    resultado_b = eliminar_subcadena(cadena, posicion_ejemplo, cantidad_ejemplo)
    
    print(resultado_a, resultado_b)

main()
