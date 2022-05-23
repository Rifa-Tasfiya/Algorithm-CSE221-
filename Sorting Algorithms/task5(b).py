"""Problem-5 (b)"""


def doPartition(arr, starting_point, ending_point):
    piv = arr[starting_point]
    i = starting_point
    for j in range(starting_point + 1, ending_point + 1):
        if arr[j] <= piv:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i], arr[starting_point] = arr[starting_point], arr[i]
    return i


def findK(arr, start_point, end_point, k):
    if start_point == end_point:
        return arr[start_point]
    pivot_pos = doPartition(arr, start_point, end_point)

    temp = pivot_pos - start_point + 1
    if temp == k:
        return arr[pivot_pos]
    elif temp < k:
        return findK(arr, pivot_pos + 1, end_point, k - temp)

    else:
        return findK(arr, start_point, pivot_pos - 1, k)


arr_2 = [1, 3, 4, 5, 9, 7, 10]
print(findK(arr_2, 0, len(arr_2) - 1, 5))
print(findK(arr_2, 0, len(arr_2) - 1, 7))
print(findK(arr_2, 0, len(arr_2) - 1, 2))
