import matplotlib.pyplot as plt
import time
import random
from p4_b import most_frequent_difference_b
from p4_c import most_frequent_difference_c

def runtime_comparison():
    # Generate 10 exponentially increasing sizes starting from 10
    sizes = [10 * (2 ** i) for i in range(10)]  # Exponentially increasing sizes
    test_cases = 10  # Number of test cases for each size
    d_mode = 5  # Example d_mode value
    
    # Lists to store runtimes for each function
    runtimes_b = []
    runtimes_c = []

    for size in sizes:
        # Initialize cumulative runtimes for each function
        total_time_b = 0
        total_time_c = 0
        
        for _ in range(test_cases):
            # Generate a list of random integers
            values = [random.randint(1, 100) for _ in range(size)]
            
            # Measure execution time for most_frequent_difference_b
            start_time = time.time()
            most_frequent_difference_b(values, d_mode)
            total_time_b += time.time() - start_time
            
            # Measure execution time for most_frequent_difference_c
            start_time = time.time()
            most_frequent_difference_c(values, d_mode)
            total_time_c += time.time() - start_time
        
        # Calculate average runtimes for each function
        runtimes_b.append(total_time_b / test_cases)
        runtimes_c.append(total_time_c / test_cases)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, runtimes_b, marker='o', label='most_frequent_difference_b')
    plt.plot(sizes, runtimes_c, marker='o', label='most_frequent_difference_c')
    plt.title('Runtime Comparison of Difference Functions')
    plt.xlabel('Input Size (Number of Elements)')
    plt.ylabel('Average Execution Time (seconds)')
    plt.grid(True)
    plt.legend()
    plt.savefig('p4_runtime_comparison.png')  # Save the plot as a PNG
    plt.show()  # Optionally display the plot

# Run the runtime comparison function
runtime_comparison()
