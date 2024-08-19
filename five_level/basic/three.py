"""
Sum all the elements in a list of integers

"""

def create_list_int(x):
    return [i for i in range(1, (x + 1))]

def total (x:list):
    return sum(x)

fifty = create_list_int(50)
result = total(fifty)

#print(fifty)

print(result)