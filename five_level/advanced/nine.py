"""
Given a list of numbers, separate 
the positive and negative numbers into two different lists.
"""

number_list = [-1, 1, 15, -7856, 8, 17, 156, -800000000000000, 0]

def negative_or_positive (x:list):
    new_list_p = []
    new_list_n = []
    for i in x:
        if i == 0:
            new_list_p.append(i)
        elif i > 0:
            new_list_p.append(i)
        else:
            new_list_n.append(i)
    return f"list of positive:{sorted(new_list_p)}", f"list of negative:{sorted(new_list_n)}"

print(negative_or_positive(number_list))