# Escribir un programa que pida a1 usuario un frase y una vocal
# dsp muestre en la pantalla la misma frase con la vocal introducida en mayuscula. (todas)

def main():
    frase = input("Ingrese una frase: ")
    vocal = input("Ingrese una vocal: ")
    vocal.lower()
    vocales = ["a", "e", "i", "o", "u"]
    
    # Opcion 1: Recorrer la frase
    fraseModificada = ""
    for i in range(len(frase)):
        if frase[i] == vocal and vocal in vocales:
            fraseModificada = fraseModificada + frase[i].upper()
        else:
            fraseModificada = fraseModificada + frase[i]       
    print(fraseModificada)

    # Opcion 2: Usando replace
    print(frase.replace(vocal, vocal.upper()))

    # Solo debe ponerse en mayuscula la primera mayuscula
    primera = True
    for i in range(len(frase)):
        if frase[i] == vocal and primera and vocal in vocales:
            fraseModificada = fraseModificada + frase[i].upper()
            primera = False
        else:
            fraseModificada = fraseModificada + frase[i]
    print(fraseModificada)
    
    # Opcion 2: Usando replace
    print(frase.replace(vocal, vocal.upper(), 1))
    
main()