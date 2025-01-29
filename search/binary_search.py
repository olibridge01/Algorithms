def binary_search(a: list, n: int) -> int:

    """Binary search on sorted array: Time O(logn)."""

    i = 0
    j = len(a)
    
    # Iteratively halve the search space and check which side n lies on
    while i <= j:
        mid = i + (j - i) // 2

        if n == a[mid]:
            return mid
        elif n < a[mid]:
            j = mid - 1
        elif n > a[mid]:
            i = mid + 1
    
    # Return -1 if n not found in a
    return -1