# Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresar datos desde teclado.
# b. Ordenar en forma ascendente cada una de las filas de la matriz.
# c. Intercambiar dos filas, cuyos números se reciben como parámetro.
# d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
# f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
# parámetro.
# g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
# h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
# i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
# una lista con los números de las mismas.
# NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
# sea el valor ingresado.

def cargarMatriz(n):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(int(input("Ingrese un número: ")))
    return matriz

def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()
        
def ordenarFilas(matriz):
    for i in range(len(matriz)):
        matriz[i].sort()
    return matriz

def intercambiarFilas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

def intercambiarColumnas(matriz, columna1, columna2):
    for i in range(len(matriz)):
        matriz[i][columna1], matriz[i][columna2] = matriz[i][columna2], matriz[i][columna1]
    return matriz

def trasponerMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

def promedioFila(matriz, fila):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[fila][i]
    return suma / len(matriz)

def porcentajeImparColumna(matriz, columna):
    cant_impares = 0
    for i in range(len(matriz)):
        if matriz[i][columna] % 2 != 0:
            cant_impares += 1
    return cant_impares / len(matriz) * 100

def esSimetricaDiagonalPrincipal(matriz):
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def esSimetricaDiagonalSecundaria(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz) - i - 1):
            if matriz[i][j] != matriz[len(matriz) - j - 1][len(matriz) - i - 1]:
                return False
    return True

def columnasPalindromos(matriz):
    lista = []
    for i in range(len(matriz)):
        columna = ""
        for j in range(len(matriz)):
            columna += str(matriz[j][i])
        if columna == columna[::-1]:
            lista.append(i)
    return lista

def main():
    n = int(input("Ingrese el tamaño de la matriz: "))
    matriz = cargarMatriz(n)
    print("Matriz cargada:")
    mostrarMatriz(matriz)
    print("Matriz ordenada:")
    mostrarMatriz(ordenarFilas(matriz))
    fila1 = int(input("Ingrese el número de la primer fila a intercambiar: "))
    fila2 = int(input("Ingrese el número de la segunda fila a intercambiar: "))
    print("Matriz con filas intercambiadas:")
    mostrarMatriz(intercambiarFilas(matriz, fila1, fila2))
    columna1 = int(input("Ingrese el número de la primer columna a intercambiar: "))
    columna2 = int(input("Ingrese el número de la segunda columna a intercambiar: "))
    print("Matriz con columnas intercambiadas:")
    mostrarMatriz(intercambiarColumnas(matriz, columna1, columna2))
    print("Matriz traspuesta:")
    mostrarMatriz(trasponerMatriz(matriz))
    fila = int(input("Ingrese el número de la fila a calcular el promedio: "))
    print("El promedio de la fila", fila, "es:", promedioFila(matriz, fila))
    columna = int(input("Ingrese el número de la columna a calcular el porcentaje de impares: "))
    print("El porcentaje de impares de la columna", columna, "es:", porcentajeImparColumna(matriz, columna))
    if esSimetricaDiagonalPrincipal(matriz):
        print("La matriz es simétrica con respecto a su diagonal principal.")
    else:
        print("La matriz no es simétrica con respecto a su diagonal principal.")
    if esSimetricaDiagonalSecundaria(matriz):
        print("La matriz es simétrica con respecto a su diagonal secundaria.")
    else:
        print("La matriz no es simétrica con respecto a su diagonal secundaria.")
    print("Las columnas palíndromos son:", columnasPalindromos(matriz))
    
main()