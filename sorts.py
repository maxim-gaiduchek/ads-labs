from time import time


def bubble_sort(arr: list) -> (int, int, float):
    n = len(arr)
    comparisons = 0
    swaps = 0
    start = time()

    for i in range(0, n - 1):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps += 1

            comparisons += 1

        if not swapped:
            break

    return comparisons, swaps, time() - start


def comb_sort(arr: list) -> (int, int, float):
    n = len(arr)
    gap = n
    swapped = True
    comparisons = 0
    swaps = 0
    start = time()

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.25))
        swapped = False

        for i in range(n - gap):
            j = i + gap

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
                swaps += 1

            comparisons += 1

    return comparisons, swaps, time() - start
