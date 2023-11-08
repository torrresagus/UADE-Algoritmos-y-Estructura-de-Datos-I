# Ejercicio 3 (Puntaje: 30%)
# Codifica un programa que nos permita guardar los nombres de los 
# alumnos de una clase y la nota final que han obtenido. 
# El programa pedirá el número de alumnos que vamos a introducir.
# Al final el programa nos mostrará la lista de alumnos, 
# la nota obtenida por cada uno de ellos y una leyenda si aprobó o no. 
# Se aprueba con una nota mayor e igual a 4.

# Ej:
# Juan Pérez obtuvo un 4 -> Aprobó
# Raúl González obtuvo un 9 -> Aprobó
# Ana Sanchez obtuvo un 2 -> Desaprobó

# Nota: Guarda la información en un diccionario cuyas claves serán los nombres de los alumnos y los valores las notas finales. Validar nota (1 al 10). Utilizar tres funciones, la primera para el programa principal, la segunda para la carga del diccionario, y la tercera para la impresión de las notas. El uso de excepciones es opcional.

def cargarNotas(cantidadAlumnos):
    alumnos = {}
    
    for i in range(cantidadAlumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        nota = int(input("Ingrese la nota del alumno: "))
        while nota < 1 or nota > 10:
            nota = int(input("Ingrese la nota del alumno: "))
        alumnos[nombre] = nota        
    return alumnos

def imprimirAprobados(alumnos):
    for alumno in alumnos:
        if alumnos[alumno] >= 4:
            print(f"{alumno} obtuvo un {alumnos[alumno]} -> Aprobó")
        if alumnos[alumno] < 4:
            print(f"{alumno} obtuvo un {alumnos[alumno]} -> Desaprobó")
            
def main():
    try:
        cantidadAlumnos = int(input("Ingrese la cantidad de alumnos: "))
    except ValueError:
        print("Ingrese un numero entero")
        cantidadAlumnos = int(input("Ingrese la cantidad de alumnos: "))
        
    alumnos = cargarNotas(cantidadAlumnos)
    imprimirAprobados(alumnos)
    
main()