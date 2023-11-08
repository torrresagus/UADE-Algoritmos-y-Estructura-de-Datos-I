# Escribir un programa que juegue con el usuario a adivinar un número. El programa
# debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
# eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
# adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
# el número. Si el usuario introduce algo que no sea un número se mostrará un
# mensaje en pantalla y se lo contará como un intento más.

import random

def cargar_numero(numero_random):
    intentos = 0
    
    while intentos != -1:
        try:
            intentos += 1
            numero = int(input("Ingrese un numero: "))
            if numero_random == numero:
                print(f"Ha encontrado el numero en {intentos} intentos")
                intentos = -1
                
            elif numero_random > numero:
                print("El numero es mayor")
            else:
                print("El numero es menor")
        except ValueError:
            print("Debe ingresar un numero")
            intentos += 1
                        
def main():
    numero_random = random.randint(1,500)
    cargar_numero(numero_random)
    

main()