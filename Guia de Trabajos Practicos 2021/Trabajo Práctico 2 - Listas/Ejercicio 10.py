# Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
# elementos de la primera que sean impares. El proceso deberá realizarse utilizando
# listas por comprensión. Imprimir las dos listas por pantalla. 

import random

def cargarLista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1,100))
    return lista

def main():
    n = int(input("Ingrese la longitud de la lista: "))
    lista = cargarLista(n)
    print(lista)
    lista_impares = [i for i in lista if i % 2 != 0]
    print(lista_impares)
    
main()
