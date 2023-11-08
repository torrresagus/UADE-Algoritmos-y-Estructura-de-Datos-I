#ABM de alumnos
#Realizar un programa que guarde en un archivo students.txt
#el legajo, nombre completo, la edad y la nota final

def printStudents():
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()
            for item in data:
                identity, fullname, age, finalScore = item.strip().split(";")
                print(f" El legajo {identity} con el nombre completo: {fullname} con la edad: {age} tiene como nota final: {finalScore}")
    except FileNotFoundError:
        print("error")

def updateStudent():
    try:
        identifyToFind = input("Ingrese el legajo: ")
        with open("students.txt", "r+") as f:
            data = f.readlines() #["registro1", "registro2", ...]
            f.seek(0)
            f.truncate()
            for item in data:
                identity, fullname, age, finalScore = item.strip().split(";")
                if (identity == identifyToFind):
                    fullname = input("Ingrese el nombre completo: ")
                    age = int(input("Ingrese la edad: "))
                    finalScore = int(input("Ingrese la nota final: "))
                    studentToUpdate = identifyToFind + ";" + fullname + ";" + str(age) + ";" + str(finalScore) + "\n"
                    f.write(studentToUpdate)
                else:
                    f.write(item)
    except FileNotFoundError:
        print("error en archivo")

def deleteStudent():
    try:
        identifyToFind = input("Ingrese el legajo: ")
        with open("students.txt", "r+") as f:
            data = f.readlines() #["registro1", "registro2", ...]
            f.seek(0)
            f.truncate()
            for item in data:
                identity, fullname, age, finalScore = item.strip().split(";")
                if (identity != identifyToFind):
                    f.write(item)
    except FileNotFoundError:
        print("error")
            
def loadFile():
    try:
        with open("students.txt", "a") as f:
            identify = input("Ingrese el legajo: ")
            while identify != "*":
                 fullname = input("Ingrese el nombre completo: ")
                 age = int(input("Ingrese la edad: "))
                 finalScore = int(input("Ingrese la nota final: "))
                 student = identify + ";" + fullname + ";" + str(age) + ";" + str(finalScore) + "\n"
                 f.write(student)
                 identify = input("Ingrese el legajo: ")
    except FileNotFoundError:
        print("No se encontro el archivo")

def main():
    try:
        idMenu = int(input("Ingrese 1 para (ALTA) 2 para (BAJA), 3 para (MODIFICAR) y 4 para (IMPRIMIR) y 0 para terminar: "))
        while idMenu != 0:
            if (idMenu == 1):
                loadFile()
            elif (idMenu == 2):
                deleteStudent()
            elif (idMenu == 3):
                updateStudent()
            elif (idMenu == 4):
                printStudents()
            else:
                print("ERROR DE MENU")
            idMenu = int(input("Ingrese 1 para (ALTA) 2 para (BAJA), 3 para (MODIFICAR) y 4 para (IMPRIMIR) y 0 para terminar: "))
    except ValueError:
        print("ERROR DE VALUE ERROR")
main()