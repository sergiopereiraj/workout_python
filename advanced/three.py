"""
Reorganización de un array según la paridad:

Escribe una función que reorganice un array de tal forma que todos los números pares 
aparezcan antes que los impares, y mantén el orden relativo de los números.
Entrada: [3, 1, 2, 4, 7, 6, 5]
Salida: [2, 4, 6, 3, 1, 7, 5]

"""

entrada = [3, 1, 2, 4, 7, 6, 5]

def sort_to_pair(x:list):
    new_list_one = []
    new_list_two = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            new_list_one.insert(i, x[i])
        else:
            new_list_two.append(x[i])
    return new_list_one + new_list_two

print(sort_to_pair(entrada))