'''
Problem 3a

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n.
    example of file content:
    4
    2 4 1 3

    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n^2) as described in the homework.
'''
def number_of_large_inversions_3a(file, delta) -> int:
    with open(file, "r") as f:
        lines = f.readlines()

    n = int(lines[0])
    array = list(map(int, lines[1].strip().split()))
    inversionCount = 0

    for count in range(n):
        for innerCount in range(count + 1, n):
            if array[count] > array[innerCount] and count + delta < innerCount:
                inversionCount = inversionCount + 1

    return inversionCount