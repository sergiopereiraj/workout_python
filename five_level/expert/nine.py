"""
Convert a list of numbers into their binary representation.
"""

number_list = [4, 5, 6, 7, 8, 9, 11]

def to_binary(x:list):
    return [bin(i) for i in x]

print(to_binary(number_list))