# La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
# imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
# y año cualquiera basándose en la función suministrada. Considerar que la semana
# comienza en domingo.

def diaSemana(dia, mes, anio):
    if mes < 3:
        mes = mes + 12
        anio = anio - 1
    return (dia + 2 * mes + 3 * (mes + 1) // 5 + anio + anio // 4 - anio // 100 + anio // 400) % 7

def imprimirCalendario(mes, anio):
    if mes == 1:
        nombreMes = "Enero"
    elif mes == 2:
        nombreMes = "Febrero"
    elif mes == 3:
        nombreMes = "Marzo"
    elif mes == 4:
        nombreMes = "Abril"
    elif mes == 5:
        nombreMes = "Mayo"
    elif mes == 6:
        nombreMes = "Junio"
    elif mes == 7:
        nombreMes = "Julio"
    elif mes == 8:
        nombreMes = "Agosto"
    elif mes == 9:
        nombreMes = "Septiembre"
    elif mes == 10:
        nombreMes = "Octubre"
    elif mes == 11:
        nombreMes = "Noviembre"
    elif mes == 12:
        nombreMes = "Diciembre"
    
    print("Calendario de", nombreMes, "de", anio)
    print("Do Lu Ma Mi Ju Vi Sa")
    
    dia = 1
    diaPrimeraSemana = diaSemana(dia, mes, anio)
    for i in range(diaPrimeraSemana):
        print("  ", end="")
    while dia <= 31:
        if dia < 10:
            print(" ", end="")
        print(dia, end="")
        dia += 1
        diaSemanaActual = diaSemana(dia, mes, anio)
        if diaSemanaActual == 0:
            print()
        else:
            print(" ", end="")
    print()
    
def main():
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    imprimirCalendario(mes, anio)
    
main()
