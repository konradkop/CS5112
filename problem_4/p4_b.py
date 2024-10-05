# Problem 4b

# Input: 
#     values -- list of integers representing the numbers to analyze. 
#     d_mode -- the most frequent delta to find in the list.
# Output: 
#     integer containing the frequency of d_mode in the list.

# TODO: implement your solution in Θ(n log n).

def most_frequent_difference_b(values, d_mode) -> int:
    # If there are fewer than 2 values, return 0 since we can't compute a difference
    if len(values) < 2:
        return 0
    
    # Sort the values to facilitate finding differences
    values.sort()
    total_length = len(values)
    delta_count = 0  # Initialize a counter for the occurrences of d_mode

    # Initialize two pointers for traversing the sorted values
    left_pointer = 0 
    right_pointer = 1

    while right_pointer < total_length:
        # Calculate the difference between the two pointed values
        difference = values[right_pointer] - values[left_pointer]
        
        # If left pointer equals right pointer, move the right pointer to avoid same element comparison
        if left_pointer == right_pointer:
            right_pointer += 1     
        # If the calculated difference is greater than the target delta (d_mode)
        elif difference > abs(d_mode):
            left_pointer += 1  # Move the left pointer up to decrease the difference
        # If the calculated difference is less than the target delta (d_mode)   
        elif difference < abs(d_mode): 
            right_pointer += 1  # Move the right pointer up to increase the difference
        else: 
            # A match for the target delta is found
            delta_count += 1

            # Count duplicates for the right pointer
            duplicate_count_right = 0 
            while right_pointer + 1 < total_length and values[right_pointer + 1] == values[right_pointer]:
                right_pointer += 1  # Move right pointer if duplicates are found
                duplicate_count_right += 1  # Count each duplicate
                delta_count += 1  # Each duplicate also contributes to the count

            # Count duplicates for the left pointer
            duplicate_count_left = 0 
            while left_pointer + 1 < total_length and values[left_pointer + 1] == values[left_pointer]:
                left_pointer += 1  # Move left pointer if duplicates are found
                duplicate_count_left += 1  # Count each duplicate
                delta_count += 1  # Each duplicate also contributes to the count

            # Account for combinations of duplicates contributing to the delta
            delta_count += duplicate_count_left * duplicate_count_right

            # Reset the duplicate counters
            duplicate_count_right = 0 
            duplicate_count_left = 0

            # Move both pointers forward to continue searching
            right_pointer += 1
            left_pointer += 1

            # Ensure pointers do not end up at the same position
            if left_pointer == right_pointer:
                right_pointer += 1

    return delta_count  # Return the total count of occurrences of d_mode
