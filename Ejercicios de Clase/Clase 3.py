# Escribir una programa que pregunte el nombre del usuario
# en la consola y un numero entero e imprima por pantalla en lineas distintas
# el nombre del usuario tantas veces como el numero introducido

def main():
    nombre = input("Ingrese su nombre: ")
    numero = int(input("Ingrese un numero: "))
    
    print((nombre + "\n") * numero)
    
main()