#Una persona desea llevar el control de los gastos realizados al viajar en el 
#subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un 
#esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar 
#una función que reciba como parámetro la cantidad de viajes realizados en un
#determinado mes y devuelva el total gastado en viajes. Realizar también un programa 
#para verificar el comportamiento de la función.

#Cantidad de viajes     Valor del pasaje
#1 a 20                 Averiguar valor actualizado
#21 a 30                20% de descuento sobre tarifa máxima
#31 a 40                30% de descuento sobre tarifa máxima
#Más de 40              40% de descuento sobre tarifa máxima    

def gastoTotal(cantidad, valor):
    gastoTotal = 0
    if cantidad >= 1 and cantidad <= 20:
        gastoTotal = valor * cantidad
    elif cantidad >= 21 and cantidad <= 30:
        gastoTotal = (valor * cantidad) * 0.8
    elif cantidad >= 31 and cantidad <= 40:
        gastoTotal = (valor * cantidad) * 0.7
    else:
        gastoTotal = (valor * cantidad) * 0.6

    return gastoTotal

def main():
    viajes = int(input("Ingrese la cantidad de viajes realizados: "))
    valor = int(input("Ingrese el valor del pasaje: "))
    
    print("El gasto total es de: ", gastoTotal(viajes, valor))
    
main()        
