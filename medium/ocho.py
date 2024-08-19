"""
Máximo y mínimo:

Escribe una función que tome una lista de números y devuelva
 una tupla con el valor máximo y mínimo.
Entrada: [3, 1, 4, 1, 5, 9, 2, 6]
Salida: (9, 1)

"""

promp = [3, 1, 4, 1, 5, 9, 2, 6]

def min_max(x:list):
    return (min(x), max(x))

print(min_max(promp))