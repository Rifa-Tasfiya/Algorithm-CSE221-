"""Problem-1 """
"""In this code, I used a flag called 'did_swap' which represents whether any consecutive element is swapped or not
while iterating inner loop. If there is no occurrence of the swapping of consecutive elements in the inner loop,
the outer loop stops/ breaks after the first execution.

This is how the following code provides time complexity θ(n) for the best case scenario"""


def bubbleSort(arr):
    arr_size = len(arr)
    for i in range(arr_size - 1):
        did_swapped = False
        for j in range(arr_size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                did_swapped = True

        if not did_swapped:
            break
    return arr


def write_file(arr):
    global arr_no
    sorted_arr = bubbleSort(arr)
    output_str = ""
    for i in sorted_arr:
        output_str += str(i) + " "
    if arr_no == 1:
        output = open("output1.txt", "w")
        output.write("Output-1: " + output_str + "\n")
    else:
        output = open("output1.txt", "a")
        output.write("Output " + str(arr_no) + " : " + output_str + "\n")


input_data = open("input1.txt").read()
line_lst = input_data.split("\n")
idx = 0
arr_no = 1
for i in line_lst:
    if idx % 2 != 0:
        temp_arr = i.split()
        arr = []
        for j in temp_arr:
            arr.append(int(j))
        write_file(arr)
        arr_no += 1

    idx += 1

print("Programme executed!!!!")
