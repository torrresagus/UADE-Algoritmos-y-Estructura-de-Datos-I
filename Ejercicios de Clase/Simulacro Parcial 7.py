# Se tiene una cola en la que se han repartido números con el orden de atención.
# Cada integrante se representa mediante una tupla (<número de orden>, <DNI>).
# Sin embargo hay muchos "colados" en la misma, los que carecen de número ("None").
# Por eso se le ha ordenado al personal de seguridad que retire a todos aquellos que no tienen número.
# Mostrar la cola inicial, los DNI de quienes fueron retirados de la cola y la cola final.


from cola import *

def cargarCola():
    colaPersonas = inicializar_cola()
    dni = input("Ingrese DNI: ")
    while int(dni) > 0:
        numeroOrden = input(f"Ingrese nuemero de orden de {dni}: ")
        acolar(colaPersonas, (numeroOrden, dni))
        dni = input("Ingrese DNI: ")
    return colaPersonas

def colados(cola):
    listaDNI = []
    nuevaCola = inicializar_cola()
    while no_es_vacia(cola):
        orden, dni = desacolar(cola)
        if orden:
            acolar(nuevaCola, (orden, dni))
        else:
            listaDNI.append(dni)
            
    return nuevaCola, listaDNI 
    
def imprimir(cola, lista):

    for dni in lista:
        print(f"El DNI {dni} se coló")

    while no_es_vacia(cola):
        orden, dni = desacolar(cola)        
        print(f"El dni: {dni} tene el orden -> {orden}")

def main():
    colaCargada = cargarCola()
    print(f"Cola Inicial: {colaCargada}")
    colaFinal, listaDNI = colados(colaCargada)
    imprimir(colaFinal, listaDNI)
    
main()

