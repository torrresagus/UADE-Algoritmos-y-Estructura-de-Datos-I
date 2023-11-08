# Desarrollar una función que reciba como parámetros dos números enteros positivos
# y devuelva el número que resulte de concatenar ambos valores. Por ejemplo, si
# recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de
# Python no vistas en clase.


def concatenarNumeros(numero1, numero2):
    numero1 = str(numero1)
    numero2 = str(numero2)
    numeroConcatenado = numero1 + numero2
    numeroConcatenado = int(numeroConcatenado)
    return numeroConcatenado


def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    numeroConcatenado = concatenarNumeros(numero1, numero2)
    print("El numero concatenado es:", numeroConcatenado)
    
main()
