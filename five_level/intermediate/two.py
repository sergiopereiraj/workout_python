"""
Convert a list of strings into a list of integers if each string represents a number.

"""

string_list = ['1', '2', '3', 'four', '5', 'six', 'seven']

def only_int (x:list):
    new_list = []
    for i in x:
        if i.isdigit():
            new_list.append(int(i))
        else:
            continue
    return new_list

print(only_int(string_list))