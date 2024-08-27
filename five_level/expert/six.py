"""
Write a function that takes a list of numbers and returns 
a list with duplicates removed, but keeps the first occurrence of each duplicate.
"""

number_list = [1, 2, 2, 3, 4, 4, 5]

def delete_duplicate (x:list):
    return list(dict.fromkeys(x))

print(delete_duplicate(number_list))