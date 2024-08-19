"""
Rotación de lista:

Escribe una función que tome una lista y un número n, y devuelva la lista rotada n posiciones a la derecha.
Entrada: ([1, 2, 3, 4, 5], 2)
Salida: [4, 5, 1, 2, 3]

"""

entrada = ([1, 2, 3, 4, 5], 2)

def rotation(x:list):
    number = x[1]
    new_list = x[0][number:]
    second = x[0][:number]
    return new_list + second

print(rotation(entrada))