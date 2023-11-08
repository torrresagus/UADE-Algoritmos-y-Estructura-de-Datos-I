# Para ir a ver una película hay dos filas de personas.
# Un acomodador es el encargado de dejar entrar a la gente. Sus instrucciones
# son simples: "dejar entrar siempre a la persona que es mayor, si tienen la
# misma edad, a gente de la fila 1 tiene preferencia".
# El siguiente código muestra el comportamiento del acomodador.
# Suponemos que las colas guardan refernecia a Personas:

from cola import *

def cargarCola():
    edad = int(input("Ingrese la edad de la persona: "))
    cola = inicializar_cola()
    while edad > 0:
        nombre = input("Ingrese nombre de la persona: ")
        acolar(edad, nombre)
        
    return cola

def orden(cola1, cola2):
    colaFinal = inicializar_cola()
    
    while no_es_vacia(cola1) or no_es_vacia(cola2):
        if no_es_vacia(cola1) and no_es_vacia(cola2):
            edad1, nombre1 = primero(cola1)
            edad2, nombre2 = primero(cola2)
            
            if edad1 >= edad2:
                acolar(colaFinal, desacolar(cola1))
            else:
                acolar(colaFinal, desacolar(cola2))
        elif no_es_vacia(cola1):
            acolar(colaFinal, desacolar(cola1))
        elif no_es_vacia(cola2):
            acolar(colaFinal, desacolar(cola2))

    return colaFinal                
            

def main():
    cola1 = cargarCola
    cola2 = cargarCola
    orden(cola1,cola2)