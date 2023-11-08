# Intercalar los elementos de una lista entre los elementos de otra. La intercalación
# deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
# una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
# y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

import random

def cargarLista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1,50))
    return lista

# def intercalar(lista1, lista2):
#     for i in range(len(lista1)):
#         lista1.insert((i*2)+1, lista2[i])

#     return lista1

# Otra Forma de hacerlo
def intercalar(lista1, lista2):
    lista_inter = []
    for i in range(len(lista1)):
        lista_inter.append(lista1[i])
        lista_inter.append(lista2[i])
    return lista_inter

def main():
    n = int(input("Ingrese la longitud de la lista: "))
    lista1 = cargarLista(n)
    lista2 = cargarLista(n)
    print(lista1)
    print(lista2)
    print(intercalar(lista1, lista2))
    
main()