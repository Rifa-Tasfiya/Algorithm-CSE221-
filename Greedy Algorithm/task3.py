# Task 3
def greedyAlgo(line, c):
    k = 0
    sequence = ""
    sorted_lst = sorted(line)
    stack = []
    jack_work = 0
    ji_work = 0
    for i in range(len(c)):
        if c[i] == "J":
            stack.append(sorted_lst[k])
            sequence += sorted_lst[k]
            jack_work += int(sorted_lst[k])
            k += 1
        elif c[i] == "j":
            temp = stack.pop()
            sequence += temp
            ji_work += int(temp)
    output = open("task3_output.txt", 'w')
    output.write(f"{sequence}\nJack will work for {jack_work}  hours\nJill will work for {ji_work} hours")
    output.close()


f = open("task3_input.txt", "r")
elem_no = f.readline()
line_lst = f.readline().split()
c = f.readline()
greedyAlgo(line_lst, c)
f.close()
print("CODE EXECUTED!!!!!!!!!!!!")
