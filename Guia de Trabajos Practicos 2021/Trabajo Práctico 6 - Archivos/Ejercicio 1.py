# Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
# signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación
# (docstrings).

def cargarArchivo(ruta_del_archivo):
    try:
        with open(ruta_del_archivo, "r") as archivo:
            lista = archivo.readlines()
            archivo.close()
        return lista
    except FileNotFoundError:
        print("El archivo no existe")
        return []
    
def eliminarComentarios(lista):
    lista_nueva = []
    for linea in lista:
        print(linea)
        
        if "#" in linea:
            lista_nueva.append(linea[linea.index("#"):])
        else:
            lista_nueva.append(linea)
    return lista_nueva

def guardarArchivo(lista, ruta_del_archivo):
    try:
        archivo = open(ruta_del_archivo, "w")
        archivo.writelines(lista)
        archivo.close()
    except FileNotFoundError:
        print("El archivo no existe")
            
def main():
    ruta_del_archivo = "Archivos.txt"
    lista = cargarArchivo(ruta_del_archivo)
    print(lista)
    listaSinComentarios = eliminarComentarios(lista)
    guardarArchivo(listaSinComentarios, ruta_del_archivo)
    
main()