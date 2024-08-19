"""
Convert a list of strings into a single string, separated by commas.

"""
words = ["hey", "there.", "what", "are", "you", "doing?"]

def become_to_str (x:list):
    return " ".join(x)

print(become_to_str(words))