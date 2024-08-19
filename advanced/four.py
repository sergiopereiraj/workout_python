"""
Compresión y descompresión de arrays:

Implementa una función para comprimir un array (usando Run-Length Encoding o algún otro método) 
y luego otra para descomprimirlo.
Entrada: [1, 1, 2, 2, 2, 3, 3, 4]
Salida comprimida: [(1, 2), (2, 3), (3, 2), (4, 1)]
Salida descomprimida: [1, 1, 2, 2, 2, 3, 3, 4]
"""

entrada = [1, 1, 2, 2, 2, 3, 3, 4]

def run_length(x:list):
    count = 1
    new_list = []
    for i in range(1, len(x)):
        if x[i] == x[i -1]:
            count += 1
        else:
            new_list.append((x[i -1], count))
            count = 1
    new_list.append((x[-1], count))
    return new_list

print(run_length(entrada))