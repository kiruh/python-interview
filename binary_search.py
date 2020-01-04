def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        current = arr[mid]
        if current == value:
            return value
        if current > value:
            right = mid - 1
        else:
            left = mid + 1
    return None


arr = [2, 7, 19, 34, 53, 72]

print(binary_search(arr, 72))
print(binary_search(arr, 11))
