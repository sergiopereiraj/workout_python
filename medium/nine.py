"""
Contador de Caracteres:
Escribe una función que reciba una cadena de texto
y devuelva un diccionario con la frecuencia de cada carácter en la cadena.
"""

n = input("what's your character string?: ")

def count_character(x:str):
    count = {}
    for i in x:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count   


print(count_character(n))