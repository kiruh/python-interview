def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [29, 99, 27, 41, 66, 28, 44, 78, 87,
       19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
insertion_sort(arr)
print(arr)
