"""
Producto cartesiano de arrays:

Escribe una función que tome dos arrays y devuelva su producto cartesiano como una lista de tuplas.
Entrada: [1, 2] y ['a', 'b']
Salida: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

"""
entrada = [1, 2]
dos = ['a', 'b']

def new_way(x:list, y:list):
    new_list = []
    for i in x:
        for j in y:
            new_list.append((i, j))   
    return new_list

print(new_way(entrada, dos))