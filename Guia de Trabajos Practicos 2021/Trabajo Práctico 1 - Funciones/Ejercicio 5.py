#Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones
#de asteriscos, donde la cantidad de filas se recibe como parámetro:
#**********
#**********
#**********
#**********
#**********

#**
#****
#******
#********
#**********

def imprimirPatron1(filas):
    for i in range(filas):
        print("**********")
        
def imprimirPatron2(filas):
    for i in range(filas):
        for j in range(i+1):
            print("*", end="")
        print()
    
def main():
    filas = int(input("Ingrese la cantidad de filas: "))
    imprimirPatron1(filas)
    imprimirPatron2(filas)
    
main()
