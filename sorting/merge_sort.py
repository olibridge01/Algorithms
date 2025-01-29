def merge(a1: list, a2: list) -> list:
    """Merge two arrays."""

    i = j = 0
    res = []

    # Iterate through a1 and a2 and add to res in correct order
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i += 1
        else:
            res.append(a2[j])
            j += 1
    
    # Add remainder to res
    while i < len(a1):
        res.append(a1[i])
        i += 1
    while j < len(a2):
        res.append(a2[j])
        j += 1
    
    return res

def merge_sort(a: list) -> list:
    """Merge sort: Time O(nlogn) Space O(n)."""

    # Base case when array is length 1
    if len(a) == 1:
        return a
    
    # Split array in half, recursively sort and merge
    mid = len(a) // 2
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))