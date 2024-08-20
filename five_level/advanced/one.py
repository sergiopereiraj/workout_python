"""
Write a function that takes a list and returns a new list with the squares (**2) of the numbers,
 without modifying the original list.
"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

list_fiveteen = create_list_int(15)
print(list_fiveteen)

def squares (x):
    return [x[i]**2 for i in range(len(x))]

print(squares(list_fiveteen))