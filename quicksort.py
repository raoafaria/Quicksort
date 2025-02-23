import random
import time
import numpy as np
import matplotlib.pyplot as plt


# Quicksort with non-random and random pivot choice
def quicksort(arr, pivot_type='first', recursion_depth=0, max_recursion_depth=1000):
    # Base case: if the array is empty or has one element, return it as is
    if len(arr) <= 1:
        return arr

    # Check for recursion depth
    if recursion_depth > max_recursion_depth:
        print("Max recursion depth reached!")
        return arr

    # Pivot selection
    if pivot_type == 'first':
        pivot = arr[0]
    elif pivot_type == 'last':
        pivot = arr[-1]
    elif pivot_type == 'random':
        pivot = random.choice(arr)
    else:
        raise ValueError("Pivot type must be 'first', 'last', or 'random'")

    # Partition the array into left and right subarrays based on the pivot
    left = [x for x in arr[1:] if x < pivot]  # exclude pivot from left
    right = [x for x in arr[1:] if x > pivot]  # exclude pivot from right
    middle = [arr[0]] + [x for x in arr[1:] if x == pivot]  # pivot and duplicates

    # Prevent unnecessary recursion on trivially small subarrays
    if not left or not right:
        return middle  # If either side is empty, return just the middle

    # Recursively apply quicksort on left and right subarrays
    left_sorted = quicksort(left, pivot_type, recursion_depth + 1, max_recursion_depth)
    right_sorted = quicksort(right, pivot_type, recursion_depth + 1, max_recursion_depth)

    return left_sorted + middle + right_sorted


# Generate a "best case" (already sorted array)
def best_case(n):
    return list(range(n))


# Generate a "worst case" (reverse sorted array)
def worst_case(n):
    return list(range(n, 0, -1))


# Generate a "average case" (randomly shuffled array)
def average_case(n):
    return np.random.randint(0, n, n).tolist()


# Benchmark quicksort for different pivot types and cases
def benchmark_quicksort(pivot_type, case_type, sizes):
    times = []
    for size in sizes:
        if case_type == 'best':
            arr = best_case(size)
        elif case_type == 'worst':
            arr = worst_case(size)
        elif case_type == 'average':
            arr = average_case(size)
        else:
            raise ValueError("Case type must be 'best', 'worst', or 'average'")

        start_time = time.time()
        quicksort(arr, pivot_type)
        end_time = time.time()

        times.append(end_time - start_time)

    return times


# Plot benchmarking results for non-random pivot (first and last)
def plot_benchmarks():
    sizes = [100, 500, 1000, 5000, 10000, 20000]

    # Benchmark for first pivot (non-random)
    best_times_first = benchmark_quicksort('first', 'best', sizes)
    worst_times_first = benchmark_quicksort('first', 'worst', sizes)
    average_times_first = benchmark_quicksort('first', 'average', sizes)

    # Benchmark for last pivot (non-random)
    best_times_last = benchmark_quicksort('last', 'best', sizes)
    worst_times_last = benchmark_quicksort('last', 'worst', sizes)
    average_times_last = benchmark_quicksort('last', 'average', sizes)

    # Benchmark for random pivot
    best_times_random = benchmark_quicksort('random', 'best', sizes)
    worst_times_random = benchmark_quicksort('random', 'worst', sizes)
    average_times_random = benchmark_quicksort('random', 'average', sizes)

    # Plot results for non-random pivot (first and last)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, best_times_first, label="Best (first pivot)", marker='o')
    plt.plot(sizes, worst_times_first, label="Worst (first pivot)", marker='o')
    plt.plot(sizes, average_times_first, label="Average (first pivot)", marker='o')

    plt.plot(sizes, best_times_last, label="Best (last pivot)", marker='o')
    plt.plot(sizes, worst_times_last, label="Worst (last pivot)", marker='o')
    plt.plot(sizes, average_times_last, label="Average (last pivot)", marker='o')

    plt.plot(sizes, best_times_random, label="Best (random pivot)", marker='o')
    plt.plot(sizes, worst_times_random, label="Worst (random pivot)", marker='o')
    plt.plot(sizes, average_times_random, label="Average (random pivot)", marker='o')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Benchmarking')
    plt.legend()
    plt.show()


# Menu Prompt for user input
def menu():
    print("\nQuicksort Performance Benchmarking")
    print("1. Run QuickSort on Random Pivot")
    print("2. Run QuickSort on First Element Pivot")
    print("3. Run QuickSort on Last Element Pivot")
    print("4. Benchmark Performance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        pivot_type = 'random'
        case_type = input("Enter case type (best, worst, average): ")
        size = int(input("Enter the array size: "))
        arr = generate_case(case_type, size)
        start_time = time.time()
        quicksort(arr, pivot_type)
        end_time = time.time()
        print(f"Time taken for random pivot: {end_time - start_time} seconds")
        menu()

    elif choice == '2':
        pivot_type = 'first'
        case_type = input("Enter case type (best, worst, average): ")
        size = int(input("Enter the array size: "))
        arr = generate_case(case_type, size)
        start_time = time.time()
        quicksort(arr, pivot_type)
        end_time = time.time()
        print(f"Time taken for first element pivot: {end_time - start_time} seconds")
        menu()

    elif choice == '3':
        pivot_type = 'last'
        case_type = input("Enter case type (best, worst, average): ")
        size = int(input("Enter the array size: "))
        arr = generate_case(case_type, size)
        start_time = time.time()
        quicksort(arr, pivot_type)
        end_time = time.time()
        print(f"Time taken for last element pivot: {end_time - start_time} seconds")
        menu()

    elif choice == '4':
        plot_benchmarks()
        menu()

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        exit()

    else:
        print("Invalid choice, please try again.")
        menu()


# Generate array based on case type
def generate_case(case_type, size):
    if case_type == 'best':
        return best_case(size)
    elif case_type == 'worst':
        return worst_case(size)
    elif case_type == 'average':
        return average_case(size)
    else:
        raise ValueError("Invalid case type. Choose 'best', 'worst', or 'average'.")


# Main function to run the menu
if __name__ == "__main__":
    menu()
