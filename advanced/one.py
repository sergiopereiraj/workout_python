"""
Matriz de suma acumulativa:

Dada una matriz bidimensional de enteros, escribe una función que devuelva una nueva matriz donde cada elemento sea la suma acumulativa de todos los elementos anteriores en la misma fila.
Entrada: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Salida: [[1, 3, 6], [4, 9, 15], [7, 15, 24]]

"""

entrada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
promp = [1, 2, 3]

def summation (x:list):
    long = len(x)
    new_list = []
    for i in range(long):
        if i < 1 :
            new_list.append(x[i])
        elif i == 1:
            new_list.append(x[i -1] + x[i])
        else:
            new_list.append(new_list[1] + x[i])
    return new_list

def nested_sum(x:list):
    long = len(x)
    new_list = []
    for i in range(long):
        new_list.append(summation(x[i]))
    return new_list

print(summation(promp))
print(nested_sum(entrada))
