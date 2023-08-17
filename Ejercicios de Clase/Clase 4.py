# Escribir un programa que pregunte el nombre completo de una persona
# despues muestre por pantalla el nombre completo del usuario tres veces
# una con todas las letras en minuscula y la otras con mayuscula
# y otra solo con la primera letra del nombre y eI apellido
# en mayuscula. EI usuario debe introducir su nombre combinando mayusculas y minusculas

def main():
    nombre = input("Ingrese su nombre completo: ")
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.title())
    
main()