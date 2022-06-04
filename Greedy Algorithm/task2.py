# Task-2
def scheduleIntervals(task_intervals, nmLst):
    m_lst = [0] * int(nmLst[1])  # m= persons
    total_activity = 0
    task_size = len(task_intervals)
    m_size = len(m_lst)
    for i in range(task_size):
        for j in range(m_size):
            if task_intervals[i][0] >= int(m_lst[j]):
                m_lst[j] = task_intervals[i][1]
                total_activity += 1
                break
    return total_activity


task_intervals = []
with open("task2_input.txt") as openfileobj:
    nmLst = openfileobj.readline().split()
    for l in range(int(nmLst[0])):
        temp_interval = openfileobj.readline().split()
        temp_tuple = (int(temp_interval[0]), int(temp_interval[1]))
        task_intervals.append(temp_tuple)
task_intervals.sort(key=lambda x: x[1])

# -------------------------------------------------- / Write Output / --------------------------------------------------
output_f = open("task2_output.txt", "w")
output_f.write(str(scheduleIntervals(task_intervals, nmLst)))
output_f.close()
print("CODE EXECUTED!!!!!!!!!!!!!!!!!!!!!!!!!!!")



