# En este ejercicio deberás crear un programa llamado personas.py que lea los
# datos de un archivo de texto llamado personas.txt e informe cuales son las
# personas que ganan más de $ 450000. Se deberán guardar todos los datos de
# la/s persona/s que cumplan con dicha condición, en otro archivo llamado
# resultados.txt usando el mismo formato que el archivo personas.txt.
# El archivo personas.txt tendrá el siguiente contenido en texto plano (créalo previamente):
# 1;Carlos;Pérez;200000
# 2;Manuel;Heredia;168000
# 3;Rosa;Campos;890000
# 4;David;García;900000
# Los campos del archivo serán por orden: id, nombre, apellido y sueldo.
# En el caso que se produzca un error al abrir el archivo de personas.txt, se deberá guardar en un archivo llamado bitacora.txt un registro con la fecha y descripción de la excepción.
# Ej.: 2022-11-07 00:46:59.378128;[Errno 2] No such file or directory: 'tema1ej3origen1.txt'
# Nota: se deben utilizar al menos dos funciones y las excepciones que crea conveniente.
# Librería para la fecha: from datetime import datetime - Función: datetime.now()

from datetime import datetime

def cargarArchivo(directorio_archivo):
    listaEmpleados = []
    try:
        with open(directorio_archivo, "r") as archivo:
            listaEmpleados = archivo.readlines()
            archivo.close()
        return listaEmpleados
    except FileNotFoundError as e:
        bitacora(e)      

def analizarEmpleados(listaEmpleados):
    for empleado in listaEmpleados:
        print(empleado)
        id, nombre, apellido, salario = empleado.split(";")
        if int(salario) > 450000:
            try:
                with open("resultados.txt", "a") as archivo:
                    archivo.write(f"{id};{nombre};{apellido};{salario}")
            except FileNotFoundError as e:
                bitacora(e)
                        
def bitacora(e):
    with open("bitacora.txt", "a") as archivo:
        archivo.write(f"{datetime.now()};{e}\n")
        archivo.close
        
def main():
    archivo = "personas.txt"
    lista = cargarArchivo(archivo)
    analizarEmpleados(lista)

main()