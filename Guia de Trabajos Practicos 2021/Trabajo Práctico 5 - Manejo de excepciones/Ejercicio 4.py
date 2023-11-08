# Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
# las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. 
# Realizar un programa para imprimir los números enteros entre 1 y 100000, y 
# que solicite confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

def imprimir_numeros():
    for i in range(1,100000):
        print(i)

def main():
    try:
        imprimir_numeros()
    except KeyboardInterrupt:
        detencion = input("Queres detener la impresion? (si/no):")
        if detencion == "si":
            print("La impresion fue detenida.")
        else:
            imprimir_numeros()

main()




