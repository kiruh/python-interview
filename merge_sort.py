def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    arr1 = [arr[left + i] for i in range(0, n1)]
    arr2 = [arr[mid + 1 + j] for j in range(0, n2)]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge_sort(arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


arr = [29, 99, 27, 41, 66, 28, 44, 78, 87,
       19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
merge_sort(arr)
print(arr)
