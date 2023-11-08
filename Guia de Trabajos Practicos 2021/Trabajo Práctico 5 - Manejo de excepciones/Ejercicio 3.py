# Desarrollar una función que devuelva una cadena de caracteres con el nombre del
# mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
# obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
# Devolver una cadena vacía si el número de mes es inválido. La detección de meses
# inválidos deberá realizarse a través de excepciones.  

class noEsMes(Exception):
    pass

def buscar_meses(numero, meses):
    if numero < 1 or numero > 12:
        raise noEsMes
    else:
        return(meses[numero - 1])
    
def main():
    try:
        meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
        numero = int(input("Ingrese un numero de Mes"))
        
        mes = buscar_meses(numero, meses)
    except ValueError:
        print("No ingreso un numero entero")
    except noEsMes:
        print("El numero ingresado no pertenece a un mes!")
    else:
        print(f"El mes es {mes}")
    finally:
        print("El programa finalizo correctamente")
main()