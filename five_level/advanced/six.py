"""
Reorder the elements of a list in random order without using Python's shuffle function.

"""

import random

one = [1 ,2 ,3 , 4, 5, 6, 7, 8, 9, 10]

def new_random_order (x:list):
    new_list = []
    for i in range(len(x)):
        index = random.randrange(len(x))
        new_list.append(x.pop(index))
    return new_list


print(new_random_order(one))
