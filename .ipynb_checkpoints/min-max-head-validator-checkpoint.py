# Created by Tahim Bhuiya

def is_min_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return False
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return False
    return True

def is_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        if 2 * i + 1 < n and arr[i] < arr[2 * i + 1]:
            return False
        if 2 * i + 2 < n and arr[i] < arr[2 * i + 2]:
            return False
    return True