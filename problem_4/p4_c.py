# Problem 4c

# Input: 
#     values -- list of integers. 
#     d_mode -- most frequent delta.
# Output: 
#     integer containing the frequency of d_mode.

# TODO: implement your solution in Θ(n).

def most_frequent_difference_c(values, d_mode) -> int:
    frequency_map = {}  # Dictionary to store the frequency of each number
    count = 0  # Initialize count of occurrences of d_mode

    # Populate the frequency map with counts of each number
    for number in values:
        frequency_map[number] = frequency_map.get(number, 0) + 1

    # Handle the case where d_mode is 0
    if d_mode == 0:
        # Count pairs of identical elements
        for number in values:
            complement = number + d_mode  # Here, complement is just the same number
            # If the complement exists, add the count of its occurrences minus 1
            if complement in frequency_map:
                count += frequency_map[complement] - 1  # Avoid counting the same element
        return count  # Return the total count for d_mode = 0

    # Handle the case where d_mode is non-zero
    else:
        # For each number, calculate the complement for the given d_mode
        for number in values:
            complement = number + d_mode  # Calculate the required complement
            # If the complement exists in the frequency map, add its count to the total
            if complement in frequency_map:
                count += frequency_map[complement]  # Count the occurrences of the complement
        return count  # Return the total count for non-zero d_mode
