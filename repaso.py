shopping = ["Agua","Huevos","Aceite","Sal","Limón"]

print("Shopping: ")
print("Imprimiendo la lista completa")
print(shopping)

print("Shopping 0:3:")
print("Imprimiendo los elementos desde el índice 0 hasta el 2 (no incluye el índice 3)")
print(shopping[0:3])

print("Shopping :3:")
print("Imprimiendo los elementos desde el inicio hasta el índice 2 (equivalente al anterior)")
print(shopping[:3])

print("Shopping 2:4:")
print("Imprimiendo los elementos desde el índice 2 hasta el índice 3")
print(shopping[2:4])

print("Shopping -1:-4:-1")
print("Imprimiendo los elementos desde el final hacia atrás, desde el índice -1 hasta el -3")
print(shopping[-1:-4:-1])

print("Shopping ::-1  Invertir lista:")
print("Imprimiendo la lista en orden inverso")
print(shopping[::-1])

print("Shopping reversed:")
print("Imprimiendo la lista en orden inverso usando la función reversed")
print(list(reversed(shopping)))

print("Shopping reverse:")
shopping.reverse()
print("Invertir la lista in-place, lo que significa que la lista original es modificada")
print(shopping)

print("Shopping * 3")
print("Repitiendo la lista tres veces")
print(shopping * 3)

frase = "Hoy me saco un 10 (diez)"
print(frase[::4])

print(frase.find("PUTA"))

shopping.append("2")

print("  3  ".join(shopping))


shopping_str = "55 + 68 + 78 + 74 + 45 + 26"
print(shopping_str)
lsita = (shopping_str.split("+"))
print(lsita)
for i in range(len(lsita)):
    lsita[i] = lsita[i].strip()

print(lsita)

fecha = "12/31/20"
# 12/31/20 -> 12-31-2020
# fecha_final = fecha.replace("/", "-")
fecha_final = fecha.split("/")
print(fecha_final)
fecha_final = "-".join(fecha_final)
print(fecha_final)


values = "32,45,11,87,20,48"	
int_values = [int(value) for value in values.split(",") if int(value) % 2 == 0]

print(int_values)

text = 	"Hello, World!"	
word1, word2 = text.split()
print(word1, "hola", word2)

person = {
    "name": "guido",
    "putadad": "traga leche"
}

lista = ["guido"]

print(person["name"])
print(lista[0])
person["name"] = "puta"
lista[0] = "puta"

print(lista[0])
print(person["name"])

print(dict.fromkeys(["nombre", "apellido"], ["None", "hola"]))

print(person.get("name"))

rae = {
 	"bifronte" : 	"De dos frentes o dos caras"	,
 	"anarcoide"	: 	"Que tiende al desorden"	,
 	"montuvio"	: 	"Campesino de la costa"	
 }

print(rae.get("bifronte"))
print(rae.get("programación"))
print(rae.get("programació",	"No disponible"))


person["name"] = "hola"
person["programacion"] = "pyrhon"

print(person)

for i , clave in enumerate(person):
    print(i, clave, person[clave])
    
print("pene" in person)

for valor, descen in person.items():
    print(valor, descen)
    
for valor in person.values():
    print(valor)

for key in person.keys():
    print(key)
    
words = ("sun", "space", "electronica", "rocket", "earth", "arbol")

words_length = {w: len(w) for w in words if w[0] not in "aeiou"}

print(words_length)


mount_height = 3718.5
print(f"{mount_height:1.4f}")	


valor = 0b10010011
print(f"{valor:b}")
print(f"{valor:x}")
print(f"{valor:o}")
print(f"{valor:e}")
print(f"{valor:f}")

pi = 12345.6789

print(f"{pi:11.3f}")

texto = "hola    mundo \n nuevo"
partes = texto.split()
print(partes)



hola = ["1","2","5","4","6","8"]

print(hola)

string = "--".join(hola)

print(string)

listaNueva = string.split("--")

print(listaNueva)