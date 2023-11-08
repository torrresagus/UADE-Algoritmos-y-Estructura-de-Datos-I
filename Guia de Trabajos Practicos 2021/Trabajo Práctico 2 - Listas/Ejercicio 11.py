# Resolver el siguiente problema, diseñando las funciones a utilizar:
# Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
# ingresa se anuncia en la recepción indicando su número de afiliado (número entero
# de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
# turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
# se solicita:
#   a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
#       los pacientes atendidos por turno en el orden que llegaron a la clínica.
#   b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
#       atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
#       que se ingrese -1 como número de afiliado. 

def cargarPacientes():
    lista = []
    nro_afiliado = int(input("Ingrese el número de afiliado: "))
    while nro_afiliado != -1:
        tipo_atencion = int(input("Ingrese el tipo de atención (0: Urgencia, 1: Turno): "))
        lista.append((nro_afiliado, tipo_atencion))
        nro_afiliado = int(input("Ingrese el número de afiliado: "))
    return lista

def mostrarListados(lista):
    lista_urgencia = [i[0] for i in lista if i[1] == 0]
    lista_turno = [i[0] for i in lista if i[1] == 1]
    print("Listado de pacientes atendidos por urgencia: ", lista_urgencia)
    print("Listado de pacientes atendidos por turno: ", lista_turno)
    
def buscarPaciente(lista):
    nro_afiliado = int(input("Ingrese el número de afiliado: "))
    while nro_afiliado != -1:
        cant_urgencia = len([i for i in lista if i[0] == nro_afiliado and i[1] == 0])
        cant_turno = len([i for i in lista if i[0] == nro_afiliado and i[1] == 1])
        print("El paciente con número de afiliado", nro_afiliado, "fue atendido", cant_urgencia, "veces por urgencia y", cant_turno, "veces por turno.")
        nro_afiliado = int(input("Ingrese el número de afiliado: "))
        
def main():
    lista = cargarPacientes()
    mostrarListados(lista)
    buscarPaciente(lista)
    
main()
