# Los telefonos de una empresa tienen el siguiente formato
# prefijo-numero-extension donde el prefijo es el codigo del pais + 34
# y la extension tiene dos digitos por ejemplo +34-9122322345-56. Escribir
# un programa que pregunte por unn numero de telefono con este formato
# y muestre por pantalla el numero de telefono sin prefijo y la extension.

def main():
    numero = input("Ingrese un numero de telefono: ")
    numeroSinGuion = numero.split("-")
    print(f"El numero de telefono sin prefijo es {numeroSinGuion[1]}")    
    
main()