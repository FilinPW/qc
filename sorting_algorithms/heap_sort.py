def heap_sort(arr):
    """
    Heap Sort algorithm implementation.

    Args:
        arr: List of comparable elements to be sorted

    Returns:
        List: Sorted list in ascending order
    """
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            # Recursively heapify affected sub-tree
            heapify(arr, n, largest)

    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Call heapify on reduced heap
        heapify(arr, i, 0)

    return arr


# Test the algorithm
if __name__ == "__main__":
    import random

    # Generate test data
    test_data = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", test_data)

    # Test heap sort
    heap_sorted = heap_sort(test_data.copy())
    print("Heap sorted:", heap_sorted)

    # Additional test with known values
    print("\nAdditional tests:")

    # Test with already sorted array
    sorted_array = [1, 2, 3, 4, 5]
    print(f"Heap sort of {sorted_array}: {heap_sort(sorted_array.copy())}")