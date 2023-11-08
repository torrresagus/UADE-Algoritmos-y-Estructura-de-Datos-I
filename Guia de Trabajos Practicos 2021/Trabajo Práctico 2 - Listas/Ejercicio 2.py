# Escribir funciones para:
# a. Generar una lista de 50 números aleatorios del 1 al 100.
# b. Recibir una lista como parámetro y devolver True si la misma contiene algún
# elemento repetido. La función no debe modificar la lista.
# c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
# únicos de la lista original, sin importar el orden.
# Combinar estas tres funciones en un mismo programa.

import random

def cargarLista():
    lista1 = []
    for i in range(50):
        lista1.append(random.randint(1,100))
    return lista1

def repetidos(lista1):
    for i in range(len(lista1)):
        for j in range(len(lista1)):
            if lista1[i] == lista1[j]:
                return True
    return False

def elementosUnicos(lista1):
    nueva_lista = []
    for i in range(len(lista1)):
        if lista1[i] not in nueva_lista:
            nueva_lista.append(lista1[i])
    return nueva_lista
    
def main():
    lista1 = cargarLista()
    print("Lista:", lista1)
    
    if repetidos(lista1):
        print("La lista tiene elementos repetidos")
        listaUnica = elementosUnicos(lista1)
        print("Lista unica:", listaUnica)
    else:
        print("La lista no tiene elementos repetidos")
        listaUnica = lista1
        print("Lista unica:", listaUnica)        
    
main()