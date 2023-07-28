# Author:  Juan David Ramirez Grismaldo
# Date:  19/07/2021
# se hace el manejo de listas


# listas
demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numerbers_lits = list((1, 8, 9, 27, 0, 5, 4, 6, 7, 2, 3))
print(numerbers_lits)

# rango de listas
list_range = list(range(1, 10))
print(list_range)

# dir es para saber que metodos tiene una lista
print(dir(colors))

# para saber la posicion de un elemento de una lista
print(colors[1])
# para saber la posicion de un elemento de una tupla
print(numerbers_lits[0])
# para saber si un elemto existe en una lista o tupla
print('green' in colors)
print('green' in numerbers_lits)

# para agregar un elemento a una lista
colors.append('violet')
print(colors)

# para agregar un elemento a una lista en una posicion especifica
colors.insert(1, 'black')
print(colors)
# elimir un elemento de una lista
colors.pop()
print(colors)
# elimir un elemento de una lista en una posicion especifica
colors.pop(1)
print(colors)
# elimir un elemento de una lista
colors.remove('red')
print(colors)
# para limpiar una lista
colors.clear()
print(colors)
# para ordenar una lista
numerbers_lits.sort()
print(numerbers_lits)
# para ordenar una lista de forma inversa
numerbers_lits.sort(reverse=True)
print(numerbers_lits)
# para ordenar una lista de forma inversa
print(sorted(numerbers_lits))
