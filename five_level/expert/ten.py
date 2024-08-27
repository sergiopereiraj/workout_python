"""
Implement a program that sorts a list of strings by their length and, 
in case of a tie, alphabetically.
"""

str_list = ["hola", "quee", "haceees", "bb"]

def sort_by_length(x:list):
    str_plus_length = [[i, len(i)] for i in x]
    new_list = sorted(str_plus_length, key = lambda x:x[1])
    return [i[0] for i in new_list]

print(sort_by_length(str_list))