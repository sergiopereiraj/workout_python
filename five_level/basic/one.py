"""
Create a list of integers from 1 to 10 and convert it into a list of strings.
"""

long = 10

def create_list_int(x):
    return [i for i in range(1, (x + 1))]
def become_to_str(x:list):
    return [str(x[i]) for i in range(len(x))]

to_become = create_list_int(long)
result= become_to_str(to_become)

print(to_become)
print(result)


