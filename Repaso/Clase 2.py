#Crear un algoritmo que permita cargar una matriz nxn que devuelva la suma de los valores
#impares la matriz.
#Ejemp10: 2 3 4

import random

def cargarMatriz(n):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(1, 10))
    return matriz

def sumarImpares(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] % 2 != 0:
                suma += matriz[i][j]
    return suma
    
def imprimirMatriz(matriz):
    print("Matriz: ")
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end = " ")
        print()
    
def main():
    n = int(input("Ingrese el tamaño de la matriz (filas y columnas): "))
    matriz = cargarMatriz(n)
    imprimirMatriz(matriz)
    print(f"La suma de los impares de la matriz es: {sumarImpares(matriz)}")

main()