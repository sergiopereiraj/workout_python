"""
Implement a program that converts a list of strings into a list of their ASCII representations.
"""
#test = "A"
#print(ord(test))

list_str = ["a", "b", "c"]

def str_to_ASCII (x:list):
    return [ord(i) for i in x]

print(str_to_ASCII(list_str))