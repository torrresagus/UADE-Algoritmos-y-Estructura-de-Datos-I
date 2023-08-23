# Desarrollar una función que devuelva una subcadena con los últimos N caracteres
# de una cadena dada. La cadena y el valor de N se pasan como parámetros.

def ultimos_n_caracteres(cadena, N):
    return cadena[-N:]

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    n = int(input("Ingrese un número: "))
    resultado = ultimos_n_caracteres(cadena, n)
    print(resultado)

main()
