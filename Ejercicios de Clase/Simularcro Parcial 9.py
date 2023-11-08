# Cargar desde el teclado la cola DADA. 
# Imprimir un mensaje indicando si la cola DADA es capicúa.

from cola import *
from pila import *

def generarCola():
    cola = inicializar_cola()
    valor = int(input("Ingrese un valor: "))
    while valor != -1:
        acolar(cola, valor)
        valor = int(input("Ingrese un valor: "))
    return cola

def calcularColaCapicua(cola):
    pila = copiar_cola(cola)
    while no_es_vacia(cola):
        valorPrimero = desacolar(cola)
        valorUltimo = desapilar(pila)
        if (valorPrimero != valorUltimo):
            return False
    return True

def main():
    cola = generarCola()
    if (calcularColaCapicua(cola)):
        print("La cola es capicua")
    else:
        print("La cola no es capicua")
main()