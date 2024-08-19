"""
Convert a list of booleans (True, False) to integers (1, 0).
"""

list_boolean = [True, False, True, False, True, False]

def become_to_int (x:list):
    new_list = []
    for i in x:
        if i == True:
            new_list.append(1)
        elif i == False:
            new_list.append(0)
    
    return new_list


print(become_to_int(list_boolean))