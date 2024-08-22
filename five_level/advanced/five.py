"""
Convert a list of floating-point numbers to integers and round the values.
"""
floating_point = [3.5, 6.5, 6.6, 17.9, 8.7]

def round_value (x:list):
    return [round(i) for i in x]

print(round_value(floating_point))