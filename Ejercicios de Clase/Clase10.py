# Escribir un programa, que contenga una función que reciba un archivo
#llamado datos_origen.txt y un número N y guarde en otro archivo llamado
#datos destino.txt las primeras N líneas del archivo datos origen.txt.
# Nota: EI usuario ingresará por teclado la cantidad de líneas a copiar.
#En el caso que se produzca un error al abrir el archivo de datos_origen.txt,
#se deberá guardar en un archivo llamado bitacora.txt un registro con la fecha
#y descripción de la excepción.
#Ej.: 2ê22-11-Ê7 0:46:59.378128; [Errno 2] No such file or directory: 'datos_origen.txt' .
#Se deben utilizar a1 menos dos funciones y las excepciones que crea conveniente.

from datetime import datetime

def leer_archivo(archivo):
    try:
        with open(archivo, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        with open("./bitacora.txt", "a") as file:
            file.write(f"{datetime.now()}; No such file or directory: '{archivo}'\n")
        return None
    
def escribir_archivo(archivo, lineas):
    with open(archivo, "w") as file:
        file.writelines(lineas)
        
def copiar_lineas(origen, destino, n):
    lineas = leer_archivo(origen)
    if lineas:
        escribir_archivo(destino, lineas[:n])
        
def main():
    origen = "origen.txt"
    destino = "datos_destino.txt"
    n = int(input("Ingrese la cantidad de líneas a copiar: "))
    copiar_lineas(origen, destino, n)
    
main()