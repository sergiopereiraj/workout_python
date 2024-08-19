"""
Productos de pares:

Escribe una función que tome una lista de números 
y devuelva una nueva lista con el producto de cada par de elementos adyacentes.
Entrada: [1, 2, 3, 4]
Salida: [2, 6, 12]

"""

entrada = [1, 2, 3, 4]
"""
def exit(x:list):
    new_list = [x[i] * x[i + 1] for i in range(len(x) - 1)]
    return new_list
"""

def exit(x:list):
    new_list = []
    for i in range(len(x) - 1):
        new_list.append(x[i] * x[i + 1])
    return new_list

print(exit(entrada))