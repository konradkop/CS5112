import time
import random
import matplotlib.pyplot as plt
from p3_b import number_of_large_inversions_3b
from p3_a import number_of_large_inversions_3a

def generate_test_case(n):
    """Generates a test case with n integers ordered randomly."""
    return n, random.sample(range(1, n + 1), n)

def save_test_case_to_file(file_path, n, ordering):
    """Saves the generated test case to a file."""
    with open(file_path, 'w') as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, ordering)))

def run_performance_analysis():
    runtimes_a = []
    runtimes_b = []
    test_sizes = []

    for i in range(10):
        n = (i + 1) * 1000  # Increase size for each test case
        ordering = random.sample(range(1, n + 1), n)
        
        # Save test case to a temporary file
        file_path = f'test_case_{n}.txt'
        save_test_case_to_file(file_path, n, ordering)

        # Measure runtime for number_of_large_inversions_3a
        start_time = time.time()
        number_of_large_inversions_3a(file_path, delta=0)
        end_time = time.time()
        runtimes_a.append(end_time - start_time)

        # Measure runtime for number_of_large_inversions_3b
        start_time = time.time()
        number_of_large_inversions_3b(file_path, delta=0)
        end_time = time.time()
        runtimes_b.append(end_time - start_time)

        test_sizes.append(n)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(test_sizes, runtimes_a, marker='o', label='3a Runtime')
    plt.plot(test_sizes, runtimes_b, marker='o', label='3b Runtime')
    plt.title('Runtime Comparison of number_of_large_inversions_3a and 3b')
    plt.xlabel('Size of Input (n)')
    plt.ylabel('Runtime (seconds)')
    plt.grid()
    plt.xticks(test_sizes)
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig('p3_runtime_comparison.png', format='png')
    plt.close()  # Close the plot to free memory

    # Determine the point where 3b dominates
    for i in range(len(test_sizes)):
        if runtimes_b[i] < runtimes_a[i]:
            print(f"3b dominates over 3a at n = {test_sizes[i]}")

# Example usage
run_performance_analysis()
