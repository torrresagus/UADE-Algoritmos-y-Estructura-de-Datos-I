# Escribir una función que reciba como parámetro una cadena de caracteres en la
# que las palabras se encuentran separadas por uno o más espacios. Devolver otra
# cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada
# una.

def ordenar_palabras(cadena):
    # Dividimos la cadena en palabras
    palabras = cadena.split()
    
    # Ordenamos las palabras alfabéticamente
    palabras_ordenadas = sorted(palabras)
    
    # Unimos las palabras ordenadas en una cadena con un espacio entre cada una
    cadena_ordenada = ' '.join(palabras_ordenadas)
    
    return cadena_ordenada

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    resultado = ordenar_palabras(cadena)
    print(resultado)

main()
