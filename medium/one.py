"""
Verificador de Palíndromos:
Escribe una función que verifique si una cadena de texto es un palíndromo
 (se lee igual hacia adelante y hacia atrás, ignorando espacios y puntuación).
"""


n = input("Insert your word: ")

name = "ana"

def palindrome(x,y):
    clear = x.lower()
    return clear == y[::-1]

print(palindrome(n, name))