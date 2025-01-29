def partition(a: list, lo: int, hi: int):
    """Divide array into two partitions."""

    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    
    a[i], a[hi] = a[hi], a[i]
    return i

def quicksort(a: list, lo: int, hi: int):
    """Quicksort: Time O(nlogn) (avg) O(n^2) (worst) Space O(logn)."""

    if lo >= hi or lo < 0:
        return
    
    p = partition(a, lo, hi)

    quicksort(a, lo, p - 1)
    quicksort(a, p + 1, hi)