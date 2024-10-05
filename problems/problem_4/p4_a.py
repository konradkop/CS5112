'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n^2).
'''
def most_frequent_difference_a(values, d_mode) -> int:

    n = len(values)
    output = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                difference = values[i] - values[j]
                if (difference == d_mode):
                    output += 1
    
    return output
