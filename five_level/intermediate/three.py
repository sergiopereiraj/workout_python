"""
Write a program that removes duplicates from a list while maintaining the original order.
"""

mylist = ["a", "b", "a", "c", "c"]

def delete_duplicates (x:list):
    return list(dict.fromkeys(x))

print(delete_duplicates(mylist))