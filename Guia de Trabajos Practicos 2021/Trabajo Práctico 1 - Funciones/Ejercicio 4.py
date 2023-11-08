# Un comercio de electrodomésticos necesita para su línea de cajas un programa que
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
# dos números enteros, correspondientes al total de la compra y al dinero recibido.
# Informar cuántos billetes de cada denominación deben ser entregados al cliente
# como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
# existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
# si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
# de $20, 1 billete de $10 y 3 billetes de $1.


def calcularVuelto(totalCompra, dineroRecibido):
    if dineroRecibido < totalCompra:
        return -1
    else:
        vuelto = dineroRecibido - totalCompra
        billetes500 = vuelto // 500
        vuelto = vuelto % 500
        billetes100 = vuelto // 100
        vuelto = vuelto % 100
        billetes50 = vuelto // 50
        vuelto = vuelto % 50
        billetes20 = vuelto // 20
        vuelto = vuelto % 20
        billetes10 = vuelto // 10
        vuelto = vuelto % 10
        billetes5 = vuelto // 5
        vuelto = vuelto % 5
        billetes1 = vuelto // 1
        

        return billetes500, billetes100, billetes50, billetes20, billetes10, billetes5, billetes1

def imprimirVuelto(billetes500, billetes100, billetes50, billetes20, billetes10, billetes5, billetes1):
    print("Billetes de $500:", billetes500)
    print("Billetes de $100:", billetes100)
    print("Billetes de $50:", billetes50)
    print("Billetes de $20:", billetes20)
    print("Billetes de $10:", billetes10)
    print("Billetes de $5:", billetes5)
    print("Billetes de $1:", billetes1)

def main():
    totalCompra = int(input("Ingrese el total de la compra: "))
    dineroRecibido = int(input("Ingrese el dinero recibido: "))
    
    billetes500, billetes100, billetes50, billetes20, billetes10, billetes5, billetes1 = calcularVuelto(totalCompra, dineroRecibido)
    
    imprimirVuelto(billetes500, billetes100, billetes50, billetes20, billetes10, billetes5, billetes1)
    
main()