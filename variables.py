# se hace el manejo de variables
# Author: Juan David Ramirez Grismaldo
# Date: 19/07/2021
name = "juan david"
print(name)
print(type(name))
print(id(name))

# conventiones
book_name = "i robot"  # snake case
bookName = "digital fortress"  # camel case
BookName = "asdasd"  # pascal case

# constantes
PI = 3.1416
MY_NAME = "juan david"

# variables dinamicas
book_name = "i robot"
book_name = 1234

# variables de tipo string
name = "juan david"
print(name[0])
print(name[-1])
print(name[0:3])
print(name[0:])
print(name[:3])
print(name[1:-1])
print(name[1:5:2])
print(name[1::2])
print(name[::-1])


# concatenacion
first_name = "juan david"
last_name = "ramirez grismaldo"
full_name = first_name + " " + last_name
print(full_name)

# metodos de string
# upper es para poner en mayuscula
print(full_name.upper())
# lower es para poner en minuscula
print(full_name.lower())
print(full_name.title())

# el split es para separar las palabras
print(full_name.split(" "))
# el find es para buscar una palabra
print(full_name.find("david"))
# el replace es para reemplazar una palabra
print(full_name.replace("david", "daniel"))
# LEN es para saber la longitud de una palabra
print(len(full_name))
# IN es para saber si una palabra esta en una frase
print("david" in full_name)
# NOT IN es para saber si una palabra no esta en una frase
print("david" not in full_name)
