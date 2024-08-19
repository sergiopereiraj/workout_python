"""
Filter the even numbers from a list and store them in a new list.
"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

total_list = create_list_int(25)

def even_number (x:list):
    new_list = []
    for i in x:
        if i % 2 == 0:
            new_list.append(i)
        else:
            continue
    return new_list

even_number_list = even_number(total_list)
print(even_number_list)