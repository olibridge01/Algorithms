def heapify(a: list, n: int, i: int):
    """Construct a max heap from array a."""

    largest = i
    l = 2 * i + 1 # Left child
    r = 2 * i + 2 # Right child

    if l < n and a[i] < a[l]:
        largest = l
    if r < n and a[largest] < a[r]:
        largest = r
    
    # Change root if needed
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heapsort(a: list):
    """Heapsort: Time O(nlogn) Space O(1)."""
    n = len(a)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(a, n, i)
    
    # Extract max value (root of heap) one at a time
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)