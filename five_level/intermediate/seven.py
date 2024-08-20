"""
Extract the vowels from a string and place them in a list.
"""

the_string = "Extract the vowels from a string and place them in a list."

def extract_vowels (x:str):
    new_list = []
    for i in x:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"
            or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            new_list.append(i)
        else:
            continue
    return new_list

print(extract_vowels(the_string))
