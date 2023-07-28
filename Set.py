# Author : juan david ramirez grismaldo
# Date : 19/07/2021

# se hace el manejo de set

# set
colors = {'red', 'green', 'blue'}
print(colors)
print(type(colors))

# para saber que metodos tiene un set
print(dir(colors))

# para saber si un elemto existe en un set
print('green' in colors)

# para agregar un elemento a un set
colors.add('violet')
print(colors)

# para eliminar un elemento de un set
colors.remove('red')
print(colors)

# para limpiar un set
colors.clear()
print(colors)
