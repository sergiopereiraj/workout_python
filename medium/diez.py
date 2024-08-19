"""
Contar elementos:

Escribe una función que tome una lista de números y devuelva un diccionario con la cuenta de cada elemento.
Entrada: [1, 2, 2, 3, 4, 4, 5]
Salida: {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}
"""
entrada = [1, 2, 2, 3, 4, 4, 5]

def count_number(x:list):
    count = {}
    for i in x:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print(count_number(entrada))
