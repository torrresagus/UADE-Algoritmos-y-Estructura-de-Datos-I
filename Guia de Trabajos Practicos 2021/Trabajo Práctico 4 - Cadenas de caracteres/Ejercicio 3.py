# Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos
# ubicados en posiciones impares de la clave maestra y la segunda con los dígitos
# ubicados en posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo:
# Si clave maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.

def obtener_claves(clave_maestra):
    # Convertimos la clave maestra a string para manipular los dígitos
    clave_maestra_str = str(clave_maestra)
    
    # Extraemos los dígitos en posiciones impares y pares
    clave1 = ""
    for i in range(0, len(clave_maestra_str), 2):
        clave1 = clave1 + clave_maestra_str[i]

    clave2 = ""
    for i in range(1, len(clave_maestra_str), 2):
        clave2 = clave2 + clave_maestra_str[i]
    
    # Opcion usando .join        
    clave1 = "".join([clave_maestra_str[i] for i in range(0, len(clave_maestra_str), 2)])
    clave2 = "".join([clave_maestra_str[i] for i in range(1, len(clave_maestra_str), 2)])
    
    return int(clave1), int(clave2)

def main():
    clave_maestra = int(input("Ingrese la clave maestra: "))
    clave1, calve2 = obtener_claves(clave_maestra)

    print("La clave 1 es:", clave1)
    print("La clave 2 es:", calve2)
    
main()