import math
def binary_to_int(binary_list):
    """Convert a binary list to an integer."""
    return int(''.join(map(str, binary_list)), 2)

def reference_multiply(x, y) -> int:
    """Multiply two binary lists."""
    # Step 1: Convert binary lists to integers
    int_x = binary_to_int(x)
    int_y = binary_to_int(y)

    # Step 2: Multiply the integers
    product = int_x * int_y
    return [int(bit) for bit in bin(product)[2:]]

def karatsuba_recursive(x, y):
    # Base case: if either number is less than 2, perform direct multiplication
    if x < 2 or y < 2:
        return x * y

    # Calculate the bit length of the larger number
    max_length = max(x.bit_length(), y.bit_length())
    # Determine the midpoint for splitting the numbers
    half_length = (max_length + 1) // 2

    # Split x and y into two halves
    high_x, low_x = divmod(x, 1 << half_length)  # High and low parts of x
    high_y, low_y = divmod(y, 1 << half_length)  # High and low parts of y

    # Recursive calls to compute products of the parts
    product_high = karatsuba_recursive(high_x, high_y)          # high_x * high_y
    product_low = karatsuba_recursive(low_x, low_y)            # low_x * low_y
    product_cross = karatsuba_recursive(high_x + low_x, high_y + low_y)  # (high_x + low_x) * (high_y + low_y)

    # Combine the results using the Karatsuba formula
    cross_terms = product_cross - product_high - product_low  # Cross term calculation

    # Shift and combine to get the final result
    return (product_high << (2 * half_length)) + (cross_terms << half_length) + product_low  # Final result

def karatsuba(x, y):
    # Convert binary representations to integers
    x_int = binary_to_int(x)
    y_int = binary_to_int(y)
    # Perform the recursive Karatsuba multiplication
    result = karatsuba_recursive(x_int, y_int)
    # Convert the result back to binary and return as a list of bits
    return [int(bit) for bit in bin(result)[2:]]  # Omit '0b' prefix and convert to list of bits


def fft(x, y):
    pass


x = [1, 1, 0, 1] # 13
y = [1, 0, 1, 1] # 11
# [1, 0, 0, 0, 1, 1, 1, 1] is 143.

reference_multiply_product = reference_multiply(x, y)
print("reference_multiply:", reference_multiply_product ) 

karatsuba_product = karatsuba(x, y)
print("Karatsuba_product:", karatsuba_product)
