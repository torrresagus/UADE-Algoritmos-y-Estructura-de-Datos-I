# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
#  a. Sumar N días a una fecha.
#  b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

def diaSiguinte(dia, mes, anio):
    dia += 1
    if dia > 30:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio

def sumarNDias(dia, mes, anio, n):
    for i in range(n):
        dia, mes, anio = diaSiguinte(dia, mes, anio)
    return dia, mes, anio

def cantidadDiasEntreFechas(dia1, mes1, anio1, dia2, mes2, anio2):
    cantidadDias = 0
    while dia1 != dia2 or mes1 != mes2 or anio1 != anio2:
        dia1, mes1, anio1 = diaSiguinte(dia1, mes1, anio1)
        cantidadDias += 1
    return cantidadDias

def main():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    dia, mes, anio = diaSiguinte(dia, mes, anio)
    print("El dia siguiente es:", dia, mes, anio)
    
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    n = int(input("Ingrese la cantidad de dias a sumar: "))
    dia, mes, anio = sumarNDias(dia, mes, anio, n)
    print("La fecha es:", dia, mes, anio)
    
    dia1 = int(input("Ingrese el dia: "))
    mes1 = int(input("Ingrese el mes: "))
    anio1 = int(input("Ingrese el anio: "))
    dia2 = int(input("Ingrese el dia: "))
    mes2 = int(input("Ingrese el mes: "))
    anio2 = int(input("Ingrese el anio: "))
    cantidadDias = cantidadDiasEntreFechas(dia1, mes1, anio1, dia2, mes2, anio2)
    print("La cantidad de dias entre las fechas es:", cantidadDias)
    
main()
