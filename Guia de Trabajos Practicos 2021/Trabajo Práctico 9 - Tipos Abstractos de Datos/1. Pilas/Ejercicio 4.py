# Escribir una función reemplazar(<pila>, <nuevo>, <viejo>) que reemplace todas
# las apariciones de <viejo> por <nuevo> dentro de la pila suministrada.

import gc

def inicializar_pila():
    pila = []
    return pila

def apilar(pila, dato):
    pila.append(dato)
    return pila

def desapilar(pila):
    return pila.pop()

def tope(pila):
    return pila[-1]

def no_es_vacia(pila):
    return len(pila) != 0

def eliminar_pila(pila):
    del pila
    gc.collect()


def reemplazar(pila, nuevo, viejo):
    pila_aux = inicializar_pila()
    while no_es_vacia(pila):
        dato = desapilar(pila)
        if dato == viejo:
            dato = nuevo
        apilar(pila_aux, dato)
        
    while no_es_vacia(pila_aux):
        dato = desapilar(pila_aux)
        apilar(pila, dato)
        
    eliminar_pila(pila_aux)
    return pila

def cargarPila():
    pila = inicializar_pila()
    
    while True:
        try:
            dato = int(input("Ingrese un numero: "))
            if dato == -1:
                break
            apilar(pila, dato)
        except ValueError:
            print("El dato ingresado no es un numero")

    return pila

def imprimirPila(pila):
    print("Pila: ")
    while no_es_vacia(pila):
        dato = desapilar(pila)
        print(dato)

def main():
    pila = cargarPila()
    imprimirPila(pila)
    numero = int(input("Ingrese el numero a reemplazar: "))
    numeroNuevo = int(input("Ingrese el numero nueco: "))
    reemplazar(pila, numeroNuevo, numero)
    
    eliminar_pila(pila)
    
main()