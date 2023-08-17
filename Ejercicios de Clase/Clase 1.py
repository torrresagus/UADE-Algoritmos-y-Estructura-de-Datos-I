#Crear un algoritmo que permita crear una lista a partir de otra pero que esta ultima tenga
#la suma del anterior y el actual. Utilizar a1 menos 4 funciones, los datos ingresados en la lista
#puede ser por teclado o random. Ejemplo: [3, 6, 8] -> RESULTADO: [3, 9, 17]

def cargarLista():
    longitud = int(input("Ingrese la longitud de la lista: "))
    lista = []
    
    for i in range(longitud):
        lista.append(int(input("Ingrese un numero: ")))
    return lista

def mostrarLista(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

def listaSumada(lista):
    acumulador = 0
    listaNueva = []
    for i in range(len(lista)):
        acumulador += lista[i]
        listaNueva.append(acumulador)
    return listaNueva

def main():
    listaCargada = cargarLista()
    listaNueva = listaSumada(listaCargada)
    
    mostrarLista(listaCargada)
    mostrarLista(listaNueva)
    
main()