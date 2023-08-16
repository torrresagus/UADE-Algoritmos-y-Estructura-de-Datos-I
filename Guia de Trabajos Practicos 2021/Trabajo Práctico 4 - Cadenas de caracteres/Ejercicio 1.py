# Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
# utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
# verificar su funcionamiento.

def capicua(cadena):
    i = 0
    j = len(cadena) - 1
    while i < j and cadena[i] == cadena[j]:
        i += 1
        j -= 1
    return i >= j

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    if capicua(cadena):
        print("La cadena es capicúa")
    else:
        print("La cadena no es capicúa")
        
main()