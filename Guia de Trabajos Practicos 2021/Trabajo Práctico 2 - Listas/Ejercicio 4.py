# Eliminar de una lista de palabras las palabras que se encuentren en una segunda
# lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

def cargarLista():
    lista1 = []
    n = int(input("Ingrese la cantidad de palabras que quiere ingresar: "))
    for i in range(n):
        lista1.append(input("Ingrese una palabra: "))
    return lista1

def eliminarPalabras(lista1, lista2):
    listaModificada = []
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            listaModificada.append(lista1[i])
            
    return listaModificada

    
def main():
    listaPalabras = cargarLista()
    listaEliminar = cargarLista()

    print("Lista original:", listaPalabras)
    print("Lista de palabras a eliminar:", listaEliminar)
    print("Lista resultante:", eliminarPalabras(listaPalabras, listaEliminar))

main()
    