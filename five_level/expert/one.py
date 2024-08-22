"""
Write a function that takes two lists and returns True 
if they are permutations of each other.
"""

one = [1, 2, 3]
two = [3, 1, 2]
three = [7, 15, 18]

def permutation (x:list, y:list):
    for list_one in x:
        for list_two in y:
            if list_one in y:
                return True
            elif list_two in x:
                return True
            else:
                return False


print(permutation(one, two))
print(permutation(one, three))