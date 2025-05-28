 # Binary Search. 

# Binary search implementation (works on sorted lists)

def binary_search(arr, target):
    """Performs binary search on a sorted list."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

# Example usage
arr = [5, 10, 15, 20, 25]
target = 20
print("Target found at index:", binary_search(arr, target))

