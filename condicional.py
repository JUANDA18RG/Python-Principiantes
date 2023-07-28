# Author juan david ramirez
# Date: 20/07/2023

# se hace el manejo de condiciones

if True:
    print("se cumple la condicion")


# se hace el manejo de condiciones

if False:
    print("se cumple la condicion")
else:
    print("no se cumple la condicion")

# se hace el manejo con variables y condiciones
x = 5
y = 10

if x > y:
    print("x es mayor que y")
else:
    print("x no es mayor que y")


# se hace el manejo con variables y condiciones

name = "juan"
lastname = "ramirez"

if name == "juan":
    if lastname == "ramirez":
        print("tu eres juan ramirez")
    else:
        print("tu no eres juan ramirez")

# comprobacion de multiples condiciones

if name == "juan" and lastname == "ramirez":
    print("tu eres juan ramirez")
else:
    print("tu no eres juan ramirez")
