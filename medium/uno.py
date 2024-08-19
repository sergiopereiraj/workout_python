"""
Suma de elementos únicos:

Dado un array de números, escribe una función
 que devuelva la suma de los elementos únicos en el array.
Entrada: [1, 2, 2, 3, 4, 4, 5]
Salida: 1 + 3 + 5 = 9
"""
n = [1, 2, 2, 3, 4, 4, 5]
def suma_function(x:list):
    as_a_result = 0
    for i in x:
        as_a_result += i
    return as_a_result

print(suma_function(n))