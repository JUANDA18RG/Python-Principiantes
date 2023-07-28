# author juan david ramirez grismaldo
# date 20/07/2023

# se hace el manejo de modulos en python
import datetime  # se importa el modulo datatime
import math  # se importa el modulo math
import random  # se importa el modulo random
import numpy as np  # se importa el modulo numpy y se le asigna el alias np
# se importa el modulo colorama y se le asigna el alias colorama
import colorama as col


# se utiliza el modulo datetime
print(datetime.date.today())  # se imprime la fecha de hoy
print(datetime.timedelta(minutes=100))  # se imprime el tiempo en minutos

# se utiliza el modulo math
print(math.pi)  # se imprime el valor de pi
print(math.e)  # se imprime el valor de e
print(math.sin(90))  # se imprime el seno de 90

# se utiliza el modulo random
print(random.randint(1, 1000))  # se imprime un numero aleatorio entre 1 y 1000

# se utiliza el modulo numpy
a = np.array([1, 2, 3])  # se crea un arreglo de 1 dimension
print(a)  # se imprime el arreglo
print(type(a))  # se imprime el tipo de dato del arreglo


# se crea una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona("juan", 20)  # se crea un objeto de la clase persona
print(persona1.nombre)  # se imprime el nombre del objeto


# se crea una clase
class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):  # se crea un metodo
        print("hola mi nombre es " + self.nombre)


persona2 = Persona2("juan", 20)  # se crea un objeto de la clase persona
persona2.saludar()  # se llama al metodo saludar del objeto


# se utiliza el modulo colorama
print(col.Fore.BLUE + "hola mundo")  # se imprime en color azul
