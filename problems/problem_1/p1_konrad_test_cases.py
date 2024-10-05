import time
import random
import matplotlib.pyplot as plt
from p1_b import stable_matching_1b
from p1_c import stable_matching_1c

def generate_test_case(n):
    """Generates a random test case with n students and hospitals."""
    students_preferences = [
        random.sample(range(n), n) for _ in range(n)
    ]
    hospitals_preferences = [
        random.sample(range(n), n) for _ in range(n)
    ]
    return f"{n}\n" + "\n".join(" ".join(map(str, prefs)) for prefs in students_preferences) + "\n" + \
           "\n".join(" ".join(map(str, prefs)) for prefs in hospitals_preferences)

def write_test_case_to_file(file_name, content):
    """Writes the generated test case to a file."""
    with open(file_name, 'w') as f:
        f.write(content)

def analyze_runtimes(num_cases=10, max_n=10):
    """Analyzes the runtimes of stable_matching_1b and stable_matching_1c functions for multiple test cases."""
    runtimes_b = []
    runtimes_c = []
    test_case_numbers = []

    for i in range(1, num_cases + 1):
        n = random.randint(2, max_n)  # Generate a random n between 2 and max_n
        test_case = generate_test_case(n)
        file_name = f'test_case_{i}.txt'
        write_test_case_to_file(file_name, test_case)

        # Timing the stable_matching_1b function
        start_time_b = time.time()
        output_b = stable_matching_1b(file_name)
        end_time_b = time.time()
        runtimes_b.append(end_time_b - start_time_b)

        # Timing the stable_matching_1c function
        start_time_c = time.time()
        output_c = stable_matching_1c(file_name)
        end_time_c = time.time()
        runtimes_c.append(end_time_c - start_time_c)

        # Record the test case number
        test_case_numbers.append(i)

    return test_case_numbers, runtimes_b, runtimes_c

def plot_runtimes(test_case_numbers, runtimes_b, runtimes_c):
    """Plots the runtimes of both methods and saves to a file."""
    plt.figure(figsize=(10, 6))
    plt.plot(test_case_numbers, runtimes_b, label='Method B', marker='o')
    plt.plot(test_case_numbers, runtimes_c, label='Method C', marker='x')

    plt.xlabel('Test Case Number')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime Comparison of Stable Matching Methods')
    plt.xticks(test_case_numbers)
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig('p1_runtime_comparison.png')
    plt.close()

if __name__ == "__main__":
    test_case_numbers, runtimes_b, runtimes_c = analyze_runtimes()
    
    # Print results for each case
    for i in range(len(test_case_numbers)):
        print(f"Test Case {test_case_numbers[i]}:")
        print(f"  Runtime B: {runtimes_b[i]:.6f} seconds")
        print(f"  Runtime C: {runtimes_c[i]:.6f} seconds\n")
    
    # Plot the runtimes
    plot_runtimes(test_case_numbers, runtimes_b, runtimes_c)
