"""
Check if a specific element is present in a list.

"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

new_list = create_list_int(10)

print(new_list)

n = int(input("Do you choose a number between 1 to 10?: "))

def inspector (x:list, number:int):
    return number in x


print(inspector(new_list, n))