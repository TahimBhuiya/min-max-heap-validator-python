# Created by Tahim Bhuiya

# Function to check if a given list represents a min heap
def is_min_heap(arr):
    n = len(arr)  # Get the number of elements in the array
    # Iterate through all non-leaf parent nodes
    for i in range((n - 2) // 2 + 1):
        # Check if the left child exists and is smaller than the parent
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return False  # Violates min-heap property
         # Check if the right child exists and is smaller than the parent
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return False  # Violates min-heap property
    return True  # If no violations found, it's a valid min heap

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


    for label, arr in zip(['A', 'B', 'C'], [A, B, C]):
        if is_min_heap(arr):
            print(f"Array {label} is a min heap.")
        elif is_max_heap(arr):
            print(f"Array {label} is a max heap.")
        else:
            print(f"Array {label} is neither a max heap nor a min heap.")

if __name__ == "__main__":
    main()