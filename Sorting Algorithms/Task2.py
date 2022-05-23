"""Problem-2"""


def returnPreferredElements(arr, preferred_choice):
    arr_size = len(arr)
    for i in range(0, preferred_choice):  # Using selection sort
        min_pos = i
        for j in range(i + 1, arr_size):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr[:preferred_choice]


def write_file(arr, preferred_choice):
    global arr_no
    preferred_elem = returnPreferredElements(arr, preferred_choice)
    output_str = ""
    for i in preferred_elem:
        output_str += str(i) + " "
    if arr_no == 1:
        output = open("output2.txt", "w")
        output.write("Output-1: " + output_str + "\n")
    else:
        output = open("output2.txt", "a")
        output.write("Output-" + str(arr_no) + " : " + output_str + "\n")


input_data = open("input2.txt").read()
line_lst = input_data.split("\n")
idx = 0
arr_no = 1
preferred_choice = -1
for i in line_lst:
    if idx % 2 != 0:
        temp_arr = i.split()
        arr = []
        for j in temp_arr:
            arr.append(int(j))
        write_file(arr, preferred_choice)
        arr_no += 1
    else:
        temp_arr = i.split()
        preferred_choice = int(temp_arr[1])

    idx += 1

print("Programme executed!!!!")
