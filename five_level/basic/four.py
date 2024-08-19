"""
Convert a list of integers into a list of floating-point numbers.

"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

ten = create_list_int(10)

def become_float (x:list):
    return [float(x[i]) for i in range(len(x))]
result = become_float(ten)
print(result)