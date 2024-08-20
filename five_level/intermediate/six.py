"""
Sort a list of strings alphabetically, 
then convert it into a list of tuples where each tuple contains the string and its length.
"""

words = ["hey", "there", "what", "you", "doing?"]

sort_ed = sorted(words)

#print(sort_ed)

def sorted_and_length (x:list):
    new_list = [(x[i], len(x[i])) for i in range(len(x))]

    return tuple(new_list)

print(sorted_and_length(sort_ed))