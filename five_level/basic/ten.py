"""
Find the maximum number in a list of numbers.
"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

new_list = create_list_int(600)

def find_max (x:list):
    return max(x)

print(find_max(new_list))