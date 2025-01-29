def bubble_sort(a: list) -> None:
    """Bubble sort: Time O(n^2) Space O(1)."""

    for n in range(len(a) - 1, 0, -1):
        swap = False
        for i in range(n):

            # Swap elements if out of order
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swap = True
        
        # Break out of loop if no swaps made
        if not swap:
            break