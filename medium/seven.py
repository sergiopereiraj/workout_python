"""
Simulador de Dados:
Escribe una función que simule el lanzamiento de dos dados y calcule la frecuencia de aparición
 de cada posible suma (de 2 a 12) en un número grande de lanzamientos.
"""
import random

n = int(input("how many time do you want shoot the dices?: "))

def random_dados(x):
    one_dices = random.randrange(1,6)
    two_dices = random.randrange(1,6)
    avg_dices = ((one_dices * x)+ (two_dices * x))/ x
    return avg_dices

print(random_dados(n)) 