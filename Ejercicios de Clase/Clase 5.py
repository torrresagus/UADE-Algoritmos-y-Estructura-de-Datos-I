# Escribir un programa que pregunte eI nombre completo del usuario
# despues de que el usuario introduzca, muestre por pantalla <NOMBRE>
# tiene <n> letras, donde <NOMBRE> es el nombre del usuario en mayusculas
# <n> la cantidad de letras del nombre

def main():
    nombre = input("Ingrese su nombre completo: ")
    cantidadEspacios = nombre.count(" ")
    cantidadLetras = len(nombre) - cantidadEspacios    
    print(nombre.upper() + " tiene " + str(cantidadLetras) + " letras")
    
main()