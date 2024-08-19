"""
Reverse the elements of a list without using the reverse() method.
"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

new_list = create_list_int(10)

def new_reverse (x:list):
    return x[::-1]

print(new_list[::-1])
print(new_reverse(new_list))