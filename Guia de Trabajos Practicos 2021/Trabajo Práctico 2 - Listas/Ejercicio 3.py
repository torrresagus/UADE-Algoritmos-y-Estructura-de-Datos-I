# Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
# donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 

def cargarLista():
    lista1 = []
    n = int(input("Ingrese un numero: "))
    for i in range(1,n+1):
        lista1.append(i**2)
    return lista1

def main():
    lista1 = cargarLista()
    print("Lista:", lista1)
    print("Ultimos 10 valores:", lista1[-10:])
    
main()
