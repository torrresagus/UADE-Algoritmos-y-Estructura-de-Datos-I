# Escribir un programa, que contenga una función que reciba un archivo
# llamado datos_origen.txt y un número N y guarde en otro archivo llamado
# datos_destino.txt las primeras N líneas del archivo datos_origen.txt.
# Nota: El usuario ingresará por teclado la cantidad de líneas a copiar.
# En el caso que se produzca un error al abrir el archivo de datos_origen.txt,
# se deberá guardar en un archivo llamado bitacora.txt un registro con la fecha
# y descripción de la excepción.
# Ej.: 2022-11-07 00:46:59.378128;[Errno 2] No such file or directory: 'datos_origen.txt'.
# Se deben utilizar al menos dos funciones y las excepciones que crea conveniente.

from datetime import datetime


class outforlines(Exception):
    pass

def escribirNuevoArchivo(archivo, cantLineas):
    lineas = archivo.readlines()
    if len(lineas) < cantLineas:
        raise outforlines("Fuera de rango")
    
    for i in range(cantLineas):
        with open("datos_destino.txt", "a") as nuevoArchivo:
            nuevoArchivo.write(lineas[i])
    archivo.close()
    
def main():
    nombreArchivo = "datos_origen.txt"
    cantLineas = int(input("Ingrese la cantidad de lineas a copiar: "))
    
    try:
        with open(nombreArchivo, "r") as archivo:
            escribirNuevoArchivo(archivo, cantLineas)    
    except FileNotFoundError as e:
        with open("bitacora.txt", "a") as bitacora:
            bitacora.write(f"{datetime.now()};{e}\n")        
    except outforlines as e:
        with open("bitacora.txt", "a") as bitacora:
            bitacora.write(f"{datetime.now()};{e}\n")
main()