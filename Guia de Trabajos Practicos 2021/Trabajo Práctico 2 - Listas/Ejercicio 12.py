# Resolver el siguiente problema, utilizando funciones:
# Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
# ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
# a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe
# aparecer una sola vez en el informe).
# b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
# ingresos. Mostrar los registros de entrada al club antes y después de
# eliminarlo. Informar cuántos ingresos se eliminaron.

def cargarSocios():
    lista = []
    nro_socio = int(input("Ingrese el número de socio: "))
    while nro_socio != 0:
        lista.append(nro_socio)
        nro_socio = int(input("Ingrese el número de socio: "))
    return lista

def mostrarIngresos(lista):
    lista_socios = []
    for i in lista:
        if i not in lista_socios:
            lista_socios.append(i)
    for i in lista_socios:
        print("El socio", i, "ingresó", lista.count(i), "veces.")
        
def eliminarSocio(lista):
    nro_socio = int(input("Ingrese el número de socio a eliminar: "))
    while nro_socio not in lista:
        print("El número de socio ingresado no existe.")
        nro_socio = int(input("Ingrese el número de socio a eliminar: "))
    print("Lista de ingresos antes de eliminar el socio:", lista)
    cant_ingresos = lista.count(nro_socio)
    for i in range(cant_ingresos):
        lista.remove(nro_socio)
    print("Lista de ingresos después de eliminar el socio:", lista)
    print("Se eliminaron", cant_ingresos, "ingresos.")
    
def main():
    lista = cargarSocios()
    mostrarIngresos(lista)
    eliminarSocio(lista)
    
main()
