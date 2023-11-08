# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha válida (día, mes, año). Devolver True o False según la
# fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

def esBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False
    
def esFechaValida(dia, mes, anio):
    if anio > 0:
        if mes >= 1 and mes <= 12:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
                if dia >= 1 and dia <= 31:
                    return True
                else:
                    return False
            else:
                if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    if dia >= 1 and dia <= 30:
                        return True
                    else:
                        return False
                else:
                    if mes == 2:
                        if esBisiesto(anio):
                            if dia >= 1 and dia <= 29:
                                return True
                            else:
                                return False
                        else:
                            if dia >= 1 and dia <= 28:
                                return True
                            else:
                                return False
                    else:
                        return False
        else:
            return False
    else:
        return False
    
def main():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    
    if esFechaValida(dia, mes, anio):
        print("La fecha es valida")
    else:
        print("La fecha no es valida")
        
main()
