"""
Convert a list of tuples into a dictionary.
"""

list_of_tuples = [(1,2,3), ('one', 'two', 'three')]

def convert_dict (x:list):
    keys, values = x
    new_dict = dict(zip(keys, values))
    return new_dict

print(convert_dict(list_of_tuples))
