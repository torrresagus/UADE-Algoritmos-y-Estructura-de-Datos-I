# Utilizar la técnica de listas por comprensión para construir una lista con todos los
# números impares comprendidos entre 100 y 200.

def main():
    lista = [i for i in range(100, 201) if i % 2 != 0]
    print(lista)
    
main()
