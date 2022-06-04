# Task-1
input_data = open("task1-input.txt").readline()
output_f = open("task1-output.txt", "w")
n = int(input_data)
output = f"{input_data}"
count = 0


while n > 0:
    m = int(max(list(str(n))))
    n = n - m
    output += " -> " + (str(n))
    count += 1

output_f.write(f"Steps: {output}\nMinimum number of steps: {count}")
output_f.close()
print("CODE EXECUTED!!!!!!!!!!")
