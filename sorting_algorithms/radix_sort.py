def radix_sort(arr):
    """
    Radix Sort algorithm implementation.

    Args:
        arr: List of non-negative integers to be sorted

    Returns:
        List: Sorted list in ascending order
    """
    if not arr:
        return arr

    # Find the maximum number to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit
    exp = 1  # Current digit position (1 for ones, 10 for tens, etc.)
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


def counting_sort_for_radix(arr, exp):
    """
    Helper function for radix sort - performs counting sort based on specific digit position.

    Args:
        arr: List of non-negative integers
        exp: Exponent representing the digit position (1 for ones, 10 for tens, etc.)
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # For digits 0-9

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]


# Test the algorithm
if __name__ == "__main__":
    import random

    # Generate test data
    test_data = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", test_data)

    # Test radix sort
    radix_sorted = radix_sort(test_data.copy())
    print("Radix sorted:", radix_sorted)

    # Additional test with known values
    print("\nAdditional tests:")

    # Test with duplicate values
    duplicates = [4, 7, 2, 4, 1, 7, 2, 4]
    print(f"Radix sort of {duplicates}: {radix_sort(duplicates.copy())}")