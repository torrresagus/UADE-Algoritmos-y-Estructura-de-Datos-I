# Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
# lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
# ¿En qué cambiaría la función si el rango de valores fuese diferente?

def entero_a_romano(n):
    # Asegurarnos de que el número está en el rango correcto
    if not (0 < n < 4000):
        return "Número fuera de rango"

    # Definimos los valores y símbolos romanos
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    romano = ''
    i = 0

    # Convertimos el número a romano
    while n > 0:
        for _ in range(n // valores[i]):
            romano += simbolos[i]
            n -= valores[i]
        i += 1

    return romano

def main():
    n = int(input("Ingrese un número entre 0 y 3999: "))
    print(entero_a_romano(n))
    