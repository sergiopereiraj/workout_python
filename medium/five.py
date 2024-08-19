"""
Detector de Números Primos:
Escribe una función que determine si un número es primo. python if else one linepython
Luego, utiliza esa función para encontrar todos los números primos en un rango dado.
"""
n = int(input("what number?: "))

def is_prime(x:int):
    if x < 2:
        False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

print(is_prime(n))