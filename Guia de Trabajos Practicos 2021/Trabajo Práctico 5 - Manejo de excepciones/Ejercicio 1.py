# Desarrollar una función para ingresar a través del teclado un número natural. La
# función rechazará cualquier ingreso inválido de datos utilizando excepciones y
# mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
# número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando éste
# sea correcto. Escribir también un programa que permita probar el correcto
# funcionamiento de la misma.


class menor0(Exception):
    pass

class noNatural(Exception):
    pass

def comprobarNumero(numero):
    if numero > 0:
        raise menor0
    elif numero % 1 != 0:
        raise noNatural
        
def main():
    try:
        numero = float(input("Ingrese un numero: "))
        comprobarNumero(numero)
        
    except ValueError:
        print("El input no puede ser un string")
    except menor0:
        print("El numero no puede ser menor a 0")
    except noNatural:
        print("El numero debe ser natural")
    else:
        print("El numero ingresado es correcto")
    finally:
        print("El programa termino con exito")
        
main()