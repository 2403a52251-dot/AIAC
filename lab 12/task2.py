def bubble_sort(arr):
    """
    Sorts a list in-place using the bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n-1):
        # Last i elements are already sorted
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    bubble_sort(sample_list)
    print("Sorted list:", sample_list)
