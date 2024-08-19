"""
Promedio de valores:

Escribe una función que tome una lista de números y devuelva su promedio.
Entrada: [1, 2, 3, 4, 5]
Salida: 3.0

"""

entrada = [1, 2, 3, 4, 5]

def avr(x:list):
    count = 0
    long = len(x)
    for i in x:
        count += i
    promedio = count/long
    return promedio

print(avr(entrada))