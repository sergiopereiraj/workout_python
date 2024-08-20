"""
Implement a program that converts a list of strings with date format ("DD/MM/YYYY") 
into a list of tuples ((DD, MM, YYYY)).
"""
"""
str_date = "DD/MM/YYYY"

def str_to_tuple (x:str):
    new = tuple(x.split("/"))
    
    return new
"""
str_date = "11/03/2013"

def str_to_tuple (x:str):
    new_str = x.split("/")
    new_list = [int(i) for i in new_str]
    new_tuple = tuple(new_list)
    return new_tuple

print(str_to_tuple(str_date))