"""
Given a list of numbers, generate a new list
 where each number is the average of its neighbors.
"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

list_fiveteen = create_list_int(15)


def list_avg (x:list):
    new_list = []
    new_list.append((x[0] + x[1])/2)

    for i in range(1, (len(x) - 1)):
        new_list.append((x[i-1] + x[i] + x[i + 1])/3 )

    new_list.append((x[-2] + x[-1])/2)

    return new_list
print(list_fiveteen)
print(list_avg(list_fiveteen))