# Task-4
from queue import Queue

def BFS(visited, graph, node, end_point):
    global q, discovery_time
    visited[int(node)-1] = 1
    q.put(node)
    while not q.empty():
        m = q.get()
        neighbour = graph.get(int(m))
        for i in neighbour:
            if visited[i-1] == 0:
                visited[i-1] = 1
                q.put(i)
                discovery_time[i-1] = discovery_time[m-1] + 1

    return discovery_time[-1]  # Number of bridge



f = open("input4.txt", "r")
output_f = open("output4.txt", "a")
line = f.readline()
for i in range(int(line)):
    graph = {}
    temp_lst = f.readline().split()
    n, m = int(temp_lst[0]) , int(temp_lst[1])
    for j in range(m):
        read_line = f.readline().split()
        if int(read_line[0]) not in graph:
            graph.update({int(read_line[0]): [int(read_line[1])]})
        else:
            graph[int(read_line[0])].append(int(read_line[1]))

        if int(read_line[1]) not in graph:
            graph.update({int(read_line[1]): [int(read_line[0])]})
        else:
            graph[int(read_line[1])].append(int(read_line[0]))
    q = Queue()
    visited = [0] * n
    discovery_time = [0] * n
    output_f.writelines(str(BFS(visited, graph, 1, n)) + "\n")
print("CODE EXECUTED!!!!!!!!!!!!!")




