"""
Calculate the product of all elements in a list of numbers.
"""
def create_list_int(x):
    return [i for i in range(1, (x + 1))]

list_int = create_list_int(3)
#print(list_int)

def product (x:list):
    producto = 1
    for i in x:
        producto *= i
    return producto

print(product(list_int))