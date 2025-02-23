# Quicksort Python Program

This Python program implements the Quicksort algorithm with both random and non-random pivot choices and provides the following functionalities:

- **Quicksort with Random Pivot**: Sorts an array using a pivot chosen randomly from the elements.
- **Quicksort with First Element Pivot**: Sorts an array using the first element as the pivot.
- **Quicksort with Last Element Pivot**: Sorts an array using the last element as the pivot.
- **Benchmarking**: Compares the performance of Quicksort with different pivot choices on best, worst, and average case scenarios and visualizes the results.

## How to Run

1. Clone the repository or download the `quicksort.py` file.
2. Navigate to the directory where `quicksort.py` is located using your terminal or command prompt.
3. Run the program:

   ```bash
   python quicksort.py


## Menu Options
Once you run the program, the following menu will be displayed:

**Run QuickSort on Random Pivot**
When you select option 1, you will be prompted to choose a case type (best, worst, or average) and the size of the array. The program will then run the Quicksort algorithm with a random pivot.

**Run QuickSort on First Element Pivot**
When you select option 2, you will be prompted to choose a case type and array size. The program will sort the array using the first element as the pivot.

**Run QuickSort on Last Element Pivot**
When you select option 3, you will be prompted to choose a case type and array size. The program will sort the array using the last element as the pivot.

**Benchmark Performance**
When you select option 4, the program will benchmark and compare the performance of Quicksort with different pivot choices on best, worst, and average case scenarios. It will generate graphs displaying the time taken for each case.

**Exit**
Select option 5 to exit the program.

## Notes

The program allows you to test Quicksort with three types of pivots: first, last, and random.
The program supports three types of cases: best, worst, and average:
Best Case: An already sorted array.
Worst Case: A reverse sorted array.
Average Case: A randomly shuffled array.
The benchmarking feature generates performance graphs comparing different pivot strategies.
The time taken for each sort is measured and displayed in seconds.
For performance testing, try with larger arrays to see more significant results
