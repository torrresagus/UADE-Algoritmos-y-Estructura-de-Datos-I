# Desarrollar un programa que permita tener un diccionario Español-Inglés con la clave
# en español y como valor la traducción en inglés. Crear una función para buscar una palabra
# en el diccionario y devolverla al usuario y si no está, devolver un mensaje.
# Debe ingresar una frase y devolver la frase traducida palabra por palabra, si es que la palabra está en el diccionario.
# INPUT: clave, valor del diccionario, palabras a buscar
# OUTPUT: diccionario con las traducciones y un mensaje si está o no
# FUNCIONES: main, carga, buscar, traducir

def carga(diccionario):
    for i in range(1, 4):
        clave = input("Ingrese la palabra en español: ")
        valor = input("Ingrese la palabra en inglés: ")
        diccionario[clave.upper()] = valor.upper()

def buscar(diccionario, palabra):
    palabra = palabra.upper()
    return diccionario.get(palabra, "Palabra no encontrada")

def traducirFrase(diccionario, listaPalabrasFrase):
    for index, palabra in enumerate(listaPalabrasFrase):
        listaPalabrasFrase[index] = buscar(diccionario, palabra)

def main():
    diccionario = {}
    carga(diccionario)
    frase = input("Ingrese una frase: ")
    listaPalabrasFrase = frase.upper().split()
    traducirFrase(diccionario, listaPalabrasFrase)
    fraseTraducida = " ".join(listaPalabrasFrase)
    print(fraseTraducida)

main()