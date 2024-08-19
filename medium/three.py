"""
Generador de Contraseñas:
Escribe una función que genere una contraseña aleatoria de longitud especificada,
combinando letras mayúsculas, minúsculas, dígitos y caracteres especiales.
"""



import random

n = int(input("how many chracter your pw?: "))

def newPassword(x):
    chracter = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    password = ""
    for i in range(x):
        password += random.choice(chracter)
    return password

print(newPassword(n))