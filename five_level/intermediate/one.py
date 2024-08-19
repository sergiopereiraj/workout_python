"""
Create a nested list (a list of lists) and access a specific element.
"""

long = 5
new_list = [i*[i, i+1, i-1] for i in range (1, long + 1)]
# [[1, 2, 0], [2, 3, 1, 2, 3, 1], [3, 4, 2, 3, 4, 2, 3, 4, 2], [4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3], [5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4]]

print(new_list[1][3])