# Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
# que no sean múltiplos de 5. A y B se ingresar desde el teclado. 

def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    lista = [i for i in range(a, b+1) if i % 7 == 0 and i % 5 != 0]
    print(lista)
    
    