"""
Given a list of lists, flatten it into a single list.
"""

list_of_list = [[1, 2, 3], ['one', 'two', 'three'], [1, 2, 3], 
                ['one', 'two', 'three'], [1, 2, 3], 
                ['one', 'two', 'three']]

def flatten (x:list):
    new_list = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            new_list.append(x[i][j])
    return new_list

print(flatten(list_of_list))