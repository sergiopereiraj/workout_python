"""
Merge two lists into one, alternating their elements.
"""

one = [1, 2, 3]
two = ['one', 'two', 'three']

def mix (x:list, y:list):
    #new_list = [(x[i], y[i]) for i in range (len(x))]
    new_list = []
    for i in range(len(x)):
        new_list.append(x[i])
        new_list.append(y[i])

    return new_list

print(mix(one, two))