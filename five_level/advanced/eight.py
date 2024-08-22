"""
Convert a list of tuples with coordinates (x, y) 
into a list of distances from the origin.
"""
import math

list_tuple = [(3, 4), (1, 1), (0, 2)]

def pythagorean_hypotenuse(x:list):
    new_list = []
    for i in x:
        total = math.sqrt(i[0]**2 + i[1]**2)
        new_list.append(total)
    return new_list

print(pythagorean_hypotenuse(list_tuple))
