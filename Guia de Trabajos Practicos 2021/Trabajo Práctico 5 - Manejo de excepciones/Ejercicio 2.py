# Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
# número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
# utilizando manejo de excepciones para detectar el error

def sumarCadenas(cadena1, cadena2):
    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        return numero1 + numero2
    except ValueError:
        return -1
    
def main():
    cadena1 = input("Ingrese un número: ")
    cadena2 = input("Ingrese otro número: ")
    resultado = sumarCadenas(cadena1, cadena2)
    if resultado == -1:
        print("Alguna de las cadenas no contiene un número válido")
    else:
        print("La suma es: ", resultado)
        
main()