"""
Implement a function that converts a list of strings into a list of their SHA-256 hashes.
"""
from hashlib import sha256

str_list = ["a", "b", "c", "x"]

def become_to_sha256 (x:list):
    return [sha256(i.encode('utf')).hexdigest() for i in x]

print(become_to_sha256(str_list))