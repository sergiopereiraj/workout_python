"""
Remover duplicados:

Escribe una función que tome un array y devuelva 
una nueva lista sin duplicados, manteniendo el orden original.
Entrada: [1, 2, 2, 3, 4, 4, 5]
Salida: [1, 2, 3, 4, 5]
"""

entrada = [1, 2, 2, 3, 4, 4, 5]

def only_unique(x:list):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(only_unique(entrada))