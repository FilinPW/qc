def counting_sort(arr):
    """
    Counting Sort algorithm implementation.

    Args:
        arr: List of non-negative integers to be sorted

    Returns:
        List: Sorted list in ascending order
    """
    if not arr:
        return arr

    # Find the maximum element in the array
    max_val = max(arr)

    # Create count array to store count of individual elements
    count = [0] * (max_val + 1)

    # Store count of each element
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


# Test the algorithm
if __name__ == "__main__":
    import random

    # Generate test data
    test_data = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", test_data)

    # Test counting sort
    counting_sorted = counting_sort(test_data.copy())
    print("Counting sorted:", counting_sorted)

    # Additional test with known values
    print("\nAdditional tests:")

    # Test with reverse sorted array
    reverse_sorted = [5, 4, 3, 2, 1]
    print(f"Counting sort of {reverse_sorted}: {counting_sort(reverse_sorted.copy())}")

    # Test with duplicate values
    duplicates = [4, 7, 2, 4, 1, 7, 2, 4]
    print(f"Counting sort of {duplicates}: {counting_sort(duplicates.copy())}")