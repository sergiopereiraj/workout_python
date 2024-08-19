import json


"""
Conversión de objetos anidados:

Dada una lista de diccionarios anidados, escribe una función que convierta 
cada diccionario en una cadena JSON, y luego convierte la lista de cadenas JSON 
de nuevo a la estructura original.
Entrada: [{"a": 1, "b": {"c": 2}}, {"d": 3, "e": {"f": 4}}]
Salida: ['{"a": 1, "b": {"c": 2}}', '{"d": 3, "e": {"f": 4}}']
"""
entrada = [{"a": 1, "b": {"c": 2}}, {"d": 3, "e": {"f": 4}}]

def become (x:dict):
    new_dict = []
    for i in range(len(x)):
        new_dict.append(json.dumps(x[i]))
    return new_dict


in_order_to = become(entrada)

def de_become (x:dict):
    new_dict = []
    for i in range(len(x)):
        new_dict.append(json.loads(x[i]))
    return new_dict

print(become(entrada))
print(de_become(in_order_to))