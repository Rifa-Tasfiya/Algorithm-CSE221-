"""Problem-4"""


def doMergeSortedArr(arr, p, q, r):
    l_size = q - p + 1
    r_size = r - q
    left_arr = [0] * l_size
    right_arr = [0] * r_size

    for idx_first_subarr in range(0, l_size):
        left_arr[idx_first_subarr] = arr[p + idx_first_subarr]

    for idx_sec_subarr in range(0, r_size):
        right_arr[idx_sec_subarr] = arr[q + 1 + idx_sec_subarr]

    idx_first_subarr = 0
    idx_sec_subarr = 0
    idx_merged_arr = p

    while idx_first_subarr < l_size and idx_sec_subarr < r_size:
        if left_arr[idx_first_subarr] <= right_arr[idx_sec_subarr]:
            arr[idx_merged_arr] = left_arr[idx_first_subarr]
            idx_first_subarr += 1
        else:
            arr[idx_merged_arr] = right_arr[idx_sec_subarr]
            idx_sec_subarr += 1
        idx_merged_arr += 1

    while idx_first_subarr < l_size:
        arr[idx_merged_arr] = left_arr[idx_first_subarr]
        idx_first_subarr += 1
        idx_merged_arr += 1

    while idx_sec_subarr < r_size:
        arr[idx_merged_arr] = right_arr[idx_sec_subarr]
        idx_sec_subarr += 1
        idx_merged_arr += 1


def doMergeSort(arr, p, r):
    if p < r:
        q = p + (r - p) // 2

        doMergeSort(arr, p, q)
        doMergeSort(arr, q + 1, r)
        doMergeSortedArr(arr, p, q, r)


def write_file(arr):
    doMergeSort(arr, 0, len(arr) - 1)
    sorted_arr = []
    for i in range(len(arr)):
        sorted_arr.append(arr[i])
    output_str = ""
    for i in sorted_arr:
        output_str += str(i) + " "
    output_file = open("output4.txt", "w")
    output_file.write(output_str)
    output_file.close()


input_data = open("input4.txt").read()
line_lst = input_data.split("\n")
temp_arr = line_lst[1].split()
arr = []
for i in range(int(line_lst[0])):
    arr.append(int(temp_arr[i]))
write_file(arr)
print("Programme executed!!!!")
