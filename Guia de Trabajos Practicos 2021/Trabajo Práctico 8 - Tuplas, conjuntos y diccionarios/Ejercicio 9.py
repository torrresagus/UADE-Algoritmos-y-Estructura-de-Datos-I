# Escribir una función que reciba un número entero N y devuelva un diccionario con
# la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar
# la función.

def tabla_multiplicar(N):
    diccionario = {}
    for i in range(1, 13):
        diccionario[i] = N * i
    return diccionario

def imprimir(diccionario):
    for clave, valor in diccionario.items():
        print(clave, ":", valor)

def main():
    N = int(input("Ingrese un número entero: "))
    diccionario = tabla_multiplicar(N)
    imprimir(diccionario)
main()