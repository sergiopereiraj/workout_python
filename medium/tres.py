"""
Conversiones de tipos:

Dado un array de números en forma de cadenas,
 escribe una función que los convierta en enteros y devuelva su suma.
Entrada: ["1", "2", "3", "4"]
Salida: 10
"""
promp =  ["1", "2", "3", "4"]

"""
def conversion (x:list):
    new_list = [int(i) for i in x]
    count = 0
    for i in new_list:
        count += i
    return count
"""
def conversion (x:list):
    new_list = [int(i) for i in x]
    suma = sum(new_list)
    return suma

print(conversion(promp))