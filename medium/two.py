"""
Calculadora de Matrices:
Implementa una clase en Python que permita realizar operaciones básicas con matrices
 (suma, resta, multiplicación).

"""



one = int(input("which is your firts number?: "))

two = int(input("which is your second number?: "))

class calculator:
    def add(x,y):
        return x + y
    
    def subtract(x,y):
        return x - y
    
    def multiply(x,y):
        return x * y
    
    def divide(x,y):
        return x / y
    

result = calculator.add(one, two)

print(result)