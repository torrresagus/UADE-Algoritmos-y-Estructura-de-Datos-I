# Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
# b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
# se ingresa desde el teclado y la función lo recibe como parámetro.
# d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
# auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

import random

def cargarLista():
    lista = []
    cantidadElementos = random.randint(10, 99)
    for i in range(cantidadElementos):
        numero = random.randint(1000, 9999)
        lista.append(numero)
    return lista

def sumatoria(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += lista[i]
    return sumatoria

def eliminarValor(lista, valor):
    while valor in lista:
        lista.remove(valor)
    return lista

def esCapicua(lista):
    for i in range(len(lista) // 2):
        if lista[i] != lista[len(lista) - i - 1]:
            return False
    return True

def main():
    lista = cargarLista()
    print("Lista:", lista)
    
    sumatoriaLista = sumatoria(lista)
    print("Sumatoria:", sumatoriaLista)
    
    valor = int(input("Ingrese el valor a eliminar: "))
    lista = eliminarValor(lista, valor)
    print("Lista:", lista)
    
    if esCapicua(lista):
        print("La lista es capicua")
    else:
        print("La lista no es capicua")
        
main()
