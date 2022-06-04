# Task 4
def countSquareNum(lst):
    a, b = int(lst[0]), int(lst[1])
    if a == 0 and b == 0:
        return
    count = 0
    i = int(a ** (1 / 2))
    while (i * i) <= b:
        count += 1
        i += 1
    return count


f = open("task4_input.txt", "r")
output_f = open("task4_output.txt", "w")
output_str = ""
flag = True
while flag:
    data = f.readlines()
    for i in data:
        line_lst = i.split()
        if line_lst[0] == "0" and line_lst[1] == "0":
            flag = False
            break
        counter = countSquareNum(line_lst)
        output_str += str(counter) + "\n"

    output_f.write(output_str)
f.close()
output_f.close()
print("CODE EXECUTED!!!!!!!!!!")