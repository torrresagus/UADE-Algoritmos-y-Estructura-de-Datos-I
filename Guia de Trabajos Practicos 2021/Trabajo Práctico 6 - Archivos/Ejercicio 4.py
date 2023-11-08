# Escribir un programa que lea un archivo de texto conteniendo un conjunto de
# apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
# ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
# cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
# ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
# Arslanian, Gustavo –> ARMENIA.TXT
# Rossini, Giuseppe –> ITALIA.TXT
# Pérez, Juan –> ESPAÑA.TXT
# Smith, John –> descartar
# El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
# escribir un programa para generarlo.

def getDataFromFile():
    try:
        with open("Apellidos.txt", "r+") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        raise FileNotFoundError
        
def writeDataToFile(data, country):
    try:
        with open(f"{country}.txt", "w") as file:
            file.writelines(data)
    except FileNotFoundError:
        raise FileNotFoundError
    
def listCreator(data, str):
    persons = []
    for person in data:
        lastName = person.split(",")[0].upper()
        if lastName.endswith(str):
            persons.append(person)
            
    return persons

def main():
    try:    
        data = getDataFromFile()
        armenia = listCreator(data, "IAN")
        italia = listCreator(data, "INI")
        españa = listCreator(data, "EZ")
                
        writeDataToFile(armenia, "ARMENIA")
        writeDataToFile(italia, "ITALIA")
        writeDataToFile(españa, "ESPAÑA")
    except FileNotFoundError:
        print("El archivo no existe")
        exit()
    else:
        print("Los archivos se crearon correctamente")
    finally:
        print("El programa finalizo correctamente")
    
main()