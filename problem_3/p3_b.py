'''
Problem 3b

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n. 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n log n) as described in the homework.
'''
def number_of_large_inversions_3b(file, delta=0) -> int:
    n = 0
    numbers = []

    with open(file, "r") as f:
        n = int(f.readline())
        d_pref = f.readline().split()
        numbers = [int(x) for x in d_pref]

    # This will store the original indices of each number in the range 1 to n
    arr_ = {num: i for i, num in enumerate(numbers)}
    arr = [arr_[i] for i in range(1, n + 1)]

    inversions = 0

    def merge_sort(arr):
        nonlocal inversions  # Use the outer scope inversions variable
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        nonlocal inversions  # Use the outer scope inversions variable
        mergedList = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                mergedList.append(left[i])
                i += 1
            else:
                # Count large inversions
                for k in range(i, len(left)):
                    if left[k] > delta + right[j]:
                        inversions += len(left) - k
                        break
                mergedList.append(right[j])
                j += 1

        # Append remaining elements
        mergedList.extend(left[i:])
        mergedList.extend(right[j:])
        return mergedList

    merge_sort(arr)
    return inversions

# Example usage
# print(number_of_large_inversions_3b('p3b_test.txt', 0))

