"""Problem-5 (a)"""
import time


def doPartition(arr, starting_point, ending_point):
    piv = arr[starting_point]
    i = starting_point
    for j in range(starting_point + 1, ending_point + 1):
        if arr[j] <= piv:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i], arr[starting_point] = arr[starting_point], arr[i]
    return i


def doQuickSort(arr, start_point, end_point):
    if start_point < end_point:
        piv_pos = doPartition(arr, start_point, end_point)
        doQuickSort(arr, start_point, piv_pos - 1)
        doQuickSort(arr, piv_pos + 1, end_point)


def write_file(arr):
    global end
    output_file = open("output5(a).txt", "w")
    output_file.writelines("Unsorted Array: \n")
    output_file.writelines(str(arr) + "\n")
    doQuickSort(arr, 0, len(arr) - 1)
    output_file.writelines("Sorted Array: \n")
    output_file.writelines(str(arr) + "\n")
    output_file.close()


start = time.time()
input_data = open("input5(a).txt").read()
line_lst = input_data.split("\n")
temp_arr = line_lst[1].split()
arr = []
for i in range(int(line_lst[0])):
    arr.append(int(temp_arr[i]))
write_file(arr)
print("Programme executed!!!!")
end = time.time()
print(f"Total time taken to executed: {end - start}")
