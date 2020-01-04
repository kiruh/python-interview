def partition(array, start, end):
    pivot = array[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= right and array[right] >= pivot:
            right = right - 1
        while left <= right and array[left] <= pivot:
            left = left + 1
        if left <= right:
            array[left], array[right] = array[right], array[left]

    array[start], array[right] = array[right], array[start]
    return right


def quick_sort(array, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [29, 99, 27, 41, 66, 28, 44, 78, 87,
         19, 31, 76, 58, 88, 83, 97, 12, 21, 44]

quick_sort(array)
print(array)
