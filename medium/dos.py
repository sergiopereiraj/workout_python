"""
Inversión de cadenas:

Escribe una función que tome una lista de cadenas
 y devuelva una nueva lista con cada cadena invertida.
Entrada: ["hello", "world", "python"]
Salida: ["olleh", "dlrow", "nohtyp"]
"""

entrada = ['hello', 'world', 'python']

"""
def inversion (x:list):
    new_list = [i[::-1] for i in x]         
    return new_list
"""

def inversion(x:list):
    new_list = []
    for i in x:
        new_list.append(i[::-1])
    return new_list

print(inversion(entrada))