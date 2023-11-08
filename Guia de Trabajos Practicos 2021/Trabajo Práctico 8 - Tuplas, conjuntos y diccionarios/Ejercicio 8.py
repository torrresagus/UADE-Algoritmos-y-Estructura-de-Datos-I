# Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
# 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

# Funciones: Imprimir, main, carga

def imprimir(diccionario):
    for clave, valor in diccionario.items():
        print(clave, ":", valor)
        
def main():
    diccionario = {}
    carga(diccionario)
    imprimir(diccionario)
    
def carga(diccionario):
    for i in range(1, 21):
        diccionario[i] = i**2
        
main()
