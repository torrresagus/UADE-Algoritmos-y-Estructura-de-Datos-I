# La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
# módulo math. Escribir un programa que utilice esta función para calcular la raíz
# cuadrada de un número cualquiera ingresado a través del teclado. El programa
# debe utilizar manejo de excepciones para evitar errores si se ingresa un número
# negativo.

import math
class EsNegativo(Exception):
    pass

def raiz_cuadrada(numero):
    if numero < 0:
        raise EsNegativo
    else:
        return math.sqrt(numero)
    
def main():
    try:
        numero = float(input("Ingrese un numero: "))
        raiz = raiz_cuadrada(numero)
        
    except ValueError:
        print("Ingrese un numero, no un caracter")
    except EsNegativo:
        print("No se puede calcular la raiz cuadrada de un numero negativo")
    else:
        print(f"La raiz cuadrada de {numero} es {raiz}")
    finally:
        print("El programa finalizo correctamente")
        
main()