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


def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [11, 9, 7, 5, 3, 1, -1, -3, -5, -7]
    C = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]