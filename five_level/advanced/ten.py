"""
Write a function that takes a list and an integer n, 
and returns all possible combinations of n elements from the list.
"""

number_list = [1, 2, 3, "one"]

def mix_element (x:list):
    new_list = []
    for i in range(len(x)):
        for j in range(len(x)):
            nw = [x[i], x[j]]
            new_list.append(nw)
    return new_list

print(mix_element(number_list))