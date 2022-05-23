"""Problem-3"""


def insertion_sort(arr_id, arr_marks):
    for i in range(len(arr_id) - 1):
        current_id = arr_id[i + 1]
        current_marks = arr_marks[i + 1]
        j = i
        while j >= 0:
            if int(arr_marks[j]) < int(current_marks):
                arr_marks[j + 1] = arr_marks[j]
                arr_id[j + 1] = arr_id[j]
            else:
                break
            j = j - 1
        arr_id[j + 1] = current_id
        arr_marks[j + 1] = current_marks
    return arr_id


def write_file(arr_id, arr_marks):
    sorted_id = insertion_sort(arr_id, arr_marks)
    output_str = ""
    for i in sorted_id:
        output_str += str(i) + " "
    output_file = open("output3.txt", "w")
    output_file.write(output_str)


input_data = open("input3.txt").read()
line_lst = input_data.split("\n")
temp_arr = line_lst[1].split()
arr_marks = line_lst[2].split()
arr_id = []
for i in temp_arr:
    arr_id.append(int(i))
write_file(arr_id, arr_marks)

print("Programme executed!!!!")
