"""
Given a list of numbers, find the contiguous subsequence with the maximum sum.
"""

list_number = [1, -2, 3, 5, -1, 2]

def contiguous_subsequence (x:list):
    nw = sorted(x)
    new_list = []
    for i in nw:
        firts = [nw[0], nw[1]]
        new_list.append(firts)
        for j in range((len(nw) - 1)):
            two = [nw[j -1], nw[j], nw[j + 1]]
            new_list.append(two)
        last = [nw[-2], nw[-1]]
        new_list.append(last)
    n_l = [sum(i) for i in new_list]
    sort_n_l = sorted(n_l)
    return (sort_n_l[-1] + sort_n_l[-2])

print(contiguous_subsequence(list_number))