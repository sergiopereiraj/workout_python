"""
Encuentra subarrays con sumas específicas:

Escribe una función que encuentre todos los subarrays de un array dado que sumen un valor específico.
Entrada: [1, 2, 3, 4, 5] y objetivo 5
Salida: [[2, 3], [5]]
"""

promp = [1, 2, 3, 4, 5]

def detection (x):
    new_list = []
    item = 5
    for i in range(len(x)):
        if x[i - 1] + x[i] == item:
            new_list.append(x[i])

    return new_list

print(detection(promp))