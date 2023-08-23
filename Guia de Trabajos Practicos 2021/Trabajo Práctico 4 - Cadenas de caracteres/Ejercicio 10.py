# Desarrollar una función para reemplazar todas las apariciones de una palabra por
# otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
# cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
# palabras completas, y no fragmentos de palabras. Escribir también un programa
# para verificar el comportamiento de la función. 

def reemplazar_palabra(cadena, palabra_original, palabra_nueva):
    # Dividimos la cadena en palabras
    palabras = cadena.split()
    
    # Contador de reemplazos
    reemplazos = 0
    
    # Recorremos las palabras y reemplazamos si es necesario
    for i, palabra in enumerate(palabras):
        if palabra == palabra_original:
            palabras[i] = palabra_nueva
            reemplazos += 1
    
    # Unimos las palabras en una cadena con un espacio entre cada una
    cadena_modificada = ' '.join(palabras)
    
    return cadena_modificada, reemplazos

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    palabra_original = input("Ingrese la palabra a reemplazar: ")
    palabra_nueva = input("Ingrese la palabra nueva: ")
    
    resultado, reemplazos = reemplazar_palabra(cadena, palabra_original, palabra_nueva)
    print(resultado, reemplazos)
    
main()
