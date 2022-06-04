# Task-1
def assignmentSelection(assign_lst, n):
    selected = [assign_lst[0]]
    count = 1
    f = assign_lst[0][1]
    for i in range(1, n):
        if assign_lst[i][0] >= f:
            count += 1
            f = assign_lst[i][1]
            selected.append(assign_lst[i])

    return count, selected


def outputFormatGenerator(assign_lst):
    output_f = open("task1_output.txt", "w")
    todo_assign = assignmentSelection(assign_lst, len(assign_lst))
    output_str = f"{todo_assign[0]}\n"
    for i in todo_assign[1]:
        output_str += str(i[0]) + " " + str(i[1]) + "\n"
    output_f.write(output_str)
    output_f.close()


file_input = open("task1_input.txt", "r")
assign_no = file_input.readline()
assign_lst = []
for i in range(int(assign_no)):
    assign_interval = file_input.readline().split()
    temp_tuple = (int(assign_interval[0]), int(assign_interval[1]))
    assign_lst.append(temp_tuple)
assign_lst.sort(key=lambda x: x[1])
outputFormatGenerator(assign_lst)
file_input.close()
print("CODE EXECUTED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
