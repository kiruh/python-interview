def counting_sort(arr, exp):
    n = len(arr)
    # count number of occurences of each digit
    count = [0] * (10)
    for i in range(0, n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # calculate position from which to insert
    # items of given digit
    positions = [0] * (10)
    total = 0
    for digit in range(0, 10):
        total += count[digit]
        positions[digit] = total - 1

    # build output
    # iterate backwards
    output = [0] * (n)
    for i in range(n-1, -1, -1):
        digit = (arr[i] // exp) % 10
        position = positions[digit]
        output[position] = arr[i]
        positions[digit] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    largest = max(arr)
    exp = 1
    while largest//exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr = [29, 99, 27, 41, 66, 28, 44, 78, 87,
       19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
radix_sort(arr)
print(arr)
