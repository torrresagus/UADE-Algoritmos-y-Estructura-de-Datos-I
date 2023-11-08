# Ejercicio 2 (Puntaje: 25%)
# La raíz cuadrada de un número puede obtenerse mediante 
# la función sqrt() del módulo math. Escribir un programa 
# que utilice esta función para calcular la raíz cuadrada 
# de un número cualquiera ingresado a través del teclado. 
# El programa debe utilizar manejo de excepciones para evitar errores si se 
# ingresa un número negativo. 

# Nota: se deben utilizar al menos dos funciones y las excepciones que 
# crea conveniente. Debe elevar excepciones entre funciones y utilizar las 
# cláusulas else (si cree conveniente) y finally.      

import math

class Negativo(Exception):
    pass

def calculate_squar_root(number):
    if number < 0:
        raise Negativo
    else:
        raiz = math.sqrt(number)
        return raiz
    
def main():
    try:
        numero = float(input("Ingrese un numero para obtner su raiz cuadrada: "))
        raiz = calculate_squar_root(numero)
                    
    except ValueError:
            print("El numero no pude ser un string")
    except Negativo:
        print("El numero no puede ser negativo")
    else:
        print(raiz)
    finally:
        print("Fin del programa")

main()


