#Resolver el siguiente problema diseñando y utilizando funciones:
#Un productor frutihortícola desea contabilizar sus cajones de nranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y
#cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
#caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de
#alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas
#cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
#reparto. Simular el peso de cada unidad generando un número entero al azar entre
#150 y 350.
#Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser inferior al 80%; encaso contrario el camión no serán despachado por su alto costo. 

import random

def generar_peso_naranja():
    return random.randint(150, 350)

def clasificar_naranjas(cantidad):
    aptas = 0
    para_jugo = 0

    for i in range(cantidad):
        peso = generar_peso_naranja()
        if 200 <= peso <= 300:
            aptas += 1
        else:
            para_jugo += 1
    
    return aptas, para_jugo

def calcular_cajones(aptas):
    cajones = aptas // 100
    sobrante = aptas % 100
    return cajones, sobrante

def calcular_camiones(cajones):
    peso_total = cajones * 25
    camiones_completos = peso_total // 500
    resto = peso_total % 500

    if resto >= 400:
        camiones_completos += 1

    return camiones_completos

def main():
    naranjas = int(input("Ingrese la cantidad total de naranjas cosechadas: "))
    
    aptas, para_jugo = clasificar_naranjas(naranjas)
    cajones, sobrante = calcular_cajones(aptas)
    camiones = calcular_camiones(cajones)
    
    print(f"\nCajones llenos: {cajones}")
    print(f"Naranjas aptas para jugo: {para_jugo}")
    if sobrante:
        print(f"Sobrante de naranjas para el siguiente reparto: {sobrante}")
    print(f"Camiones necesarios para transportar la cosecha: {camiones}")

main()
