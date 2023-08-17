# Escribir un programa que pida a1 usuario que introduzca una frase por consola y muestre
# invertida

def main():
    frase = input("Ingrese una frase: ")
    # Opcion 1: Recorrer la frase de atras para adelante
    print(frase[::-1])
    
    # Usando un ciclo for
    fraseInvertida = ""
    for i in range(len(frase) - 1, -1, -1):
        fraseInvertida = fraseInvertida + frase[i]
        
    print(fraseInvertida)
        
main()