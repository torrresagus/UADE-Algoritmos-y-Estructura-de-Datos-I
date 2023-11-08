# El método index permite buscar un elemento dentro de una lista, devolviendo la
# posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
# produce una excepción de tipo ValueError. Desarrollar un programa que cargue
# una lista con números enteros ingresados a través del teclado (terminando con -1)
# y permita que el usuario ingrese el valor de algunos elementos para visualizar la
# posición que ocupan, utilizando el método index. Si el número no pertenece a la
# lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
# proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

def cargarLista():
    lista = []
    numero = int(input("Ingrese un numero: "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingrese un numero: "))
    return lista

def buscarElemento(lista):
    for i in range(3):
        try:
            lista.index(int(input("Ingrese un numero a encontrar: ")))
        except ValueError:
            print("El elemento no pertenece a la lista")
        else:
            return True
def main():
    try:
        lista1= cargarLista()
        if buscarElemento(lista1):
            print("El elemento pertenece a la lista")
            
    except ValueError:
        print("El elemento no puede ser un caracter")

main()