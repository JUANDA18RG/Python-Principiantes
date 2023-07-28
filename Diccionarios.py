# Author juan david ramirez
# Date: 20/07/2023

# se hace el manejo de diccionarios

# diccionarios
product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

print(product)
print(type(product))


# para saber que metodos tiene un diccionario
print(dir(product))

# para saber si un elemto existe en un diccionario
print('name' in product)

# para agregar un elemento a un diccionario
product["name"] = "book2"
print(product)

# para eliminar un elemento de un diccionario
product.pop("name")
print(product)


# un diccionario puede tener otro diccionario
person = {
    "first_name": "juan",
    "last_name": "ramirez",
    "age": 30,
    "address": {
        "country": "colombia",
        "city": "bogota"
    }
}

print(person)
print(type(person))
