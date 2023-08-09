#Desarrollar una función que reciba tres números positivos y devuelva el mayor de
#los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también
#un programa para ingresar los tres valores, invocar a la función y mostrar el
#máximo hallado, o un mensaje informativo si éste no existe.

def mayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    else:
        if num2 > num1 and num2 > num3:
            return num2
        else:
            if num3 > num1 and num3 > num2:
                return num3
            else:
                return -1
            
def main():
    num1 = int(input("Ingrese el primer numero positivo: "))
    num2 = int(input("Ingrese el segundo numero positivo: "))
    num3 = int(input("Ingrese el tercer numero positivo: "))
    
    numMayor = mayor(num1, num2, num3)
    
    if numMayor == -1:
        print("No existe un numero mayor estricto")
    else:
        print("El numero mayor es: ", numMayor)

main()