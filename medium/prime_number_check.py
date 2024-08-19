"""def tree_chrismas(x):
    for i in range(x):
        print(" " * (x-i-1) + "*" * (2*i + 1))
    print(" " *(x-1) + "*")


n = int(input("what is your number?: "))

print(tree_chrismas(n)) """
n = input("what is your sentence?: ")
n2 = n.split(" ")

"""def countWord (x):
    count = 0
    for i in x:
        count += 1
    return count"""
def countWord(x):
    count = {}
    for i in x:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    
print(len(n2))
print(countWord(n2))