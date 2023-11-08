# Escribir una función que reciba una lista de números enteros como parámetro y la
# normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también
# un programa que permita verificar el comportamiento de la función. Por ejemplo,
# normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

import random

def cargarLista():
    lista = []
    n = int(input("Ingrese la longitud de la lsita: "))
    for i in range(n):
        lista.append(random.randint(1,50))
    
    return lista

def normalizar(lista):
    nuevaLista = []
    suma = sum(lista)
    
    for i in range(len(lista)):
        nuevaLista.append(lista[i]/suma)
        
    return nuevaLista

def main():
    lista1 = cargarLista()
    lista2 = normalizar(lista1)
    
    print(lista1)
    print(lista2)
    
main()