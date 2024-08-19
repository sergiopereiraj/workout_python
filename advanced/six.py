"""
Transformación y validación de datos:

Dado un array de datos que pueden ser números, cadenas, o None, 
escribe una función que filtre los elementos None, 
convierta las cadenas que representan números a enteros, 
y devuelva una lista con los valores válidos.
Entrada: [None, "3", 4, "5a", "6", None, "10"]
Salida: [3, 4, 6, 10]
"""

entrada = [None, "3", 4, "5a", "6", None, "10"]

def new_arr (x:list):
    result = []
    for i in x:
        if i is None:
            continue
        elif isinstance(i, int):
            result.append(i)
        elif isinstance(i, str):
            try:
                result.append(int(i))
            except:
                continue
    return result
print(new_arr(entrada))