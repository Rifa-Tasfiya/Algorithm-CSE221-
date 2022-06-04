# Task-2
from queue import Queue

def BFS(visited, graph, node, end_point):
    global q
    string = "Places:"
    visited[int(node)-1] = 1
    q.put(node)
    while not q.empty():
        m = q.get()
        string += " " + str(m)
        if m == int(end_point):
            break
        neighbour = graph.get(int(m))
        for i in neighbour:
            if visited[i-1] == 0:
                visited[i-1] = 1
                q.put(i)
    return string


def doBuildGraph():
    global f, n
    graph = {}
    for i in range(n):
        line = f.readline().split()
        graph[int(line[0])] = []
        size = len(line)
        for j in range(1,size):
            graph[int(line[0])].append(int(line[j]))
    return graph

def write_file(g, visited):
    output_f = open("output2.txt", "w")
    output_f.write(BFS(visited, g, "1", "12"))
    output_f.close()
    f.close()
    print("CODE EXECUTED!!!!!!!!!!!!")

f = open("input-1,2,3.txt", "r")
n = int(f.readline())
q = Queue()
g = doBuildGraph()
visited = [0] * n
write_file(g,visited)






