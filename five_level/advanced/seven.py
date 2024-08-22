"""
Given a list of strings, sort the strings by the number of vowels they contain.
"""
str_list = ["apple", "banana", "pear"]

def count_vowel (x:list):
    new_list = []
    vowels = "aeiouAEIOU"

    for word in x:
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        new_list.append([word, count])
    one = sorted(new_list, key=lambda x: x[1])
    last_list = [i for i in x]
    return last_list
print(count_vowel(str_list))
