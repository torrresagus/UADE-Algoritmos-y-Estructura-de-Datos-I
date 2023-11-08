# Escribir un programa que lea y escriba los datos de un archivo llamado divisas.txt,
# y los guarde en una variable diccionario. Ejemplo del diccionario
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}.  Luego, que pregunte al usuario
# por una divisa y muestre su símbolo o un mensaje de aviso si la divisa
# no está en el diccionario.
# Nota: Se deben utilizar al menos dos funciones y las excepciones que
# crea conveniente.


def escribir_archivo():
    nombreDivisa = input("Ingrese una divisa: ")
    while nombreDivisa != "-1":
        simbolo = input("Ingrese simbolo de divisa: ")
        with open("divisas.txt", "a") as archivo:
            archivo.write(f"{nombreDivisa};{simbolo}\n")
            archivo.close()
        nombreDivisa = input("Ingrese una divisa: ")

def leerDivisas(nombreArchivo):
    diccionario = {}
    with open(nombreArchivo,"r") as archivo:
        lineas = archivo.readlines()
        
        # lineas = ["usd;$", 
        #           "ars;a$s", 
        #           "euro;$$"]
        
        for linea in lineas:
            nombre, simbolo = linea.split(";")
            diccionario[nombre] = simbolo
            
        archivo.close

    return diccionario

def buscarDivisa(dict, divisa):
    if divisa in dict.keys():
        return dict[divisa]
    else:
        return False

def main():
    escribir_archivo()
    nombreArchivo = "divisas.txt"
    dict = leerDivisas(nombreArchivo)
    divisaBuscar = input("Ingrese divisa a buscar: ")
    
    simbolo = buscarDivisa(dict, divisaBuscar)
    
    if simbolo:
        print(f"El simbolo de la {divisaBuscar} es: {simbolo}")
    else:
        print("No se encontro la divisa")

main()