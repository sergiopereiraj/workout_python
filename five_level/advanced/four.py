"""
Write a function that takes a list of lists and 
returns a new list with the sum of the elements in each sublist.
"""
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 17, 25]]

def sum_of_each_element (x:list):
    new_list = [sum(x[i]) for i in range(len(x))]
    return new_list

print(sum_of_each_element(list_of_list))