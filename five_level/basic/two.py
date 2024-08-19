"""
Write a program that iterates over a list of words and converts each word to uppercase.

"""

words = ["hey", "there", "what", "you", "doing?"]

def become_to_uppercase (x:list):
    return [(x[i]).upper() for i in range(len(x))]

print(become_to_uppercase(words))
