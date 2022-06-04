# Task-3
def DFS_visit(graph, node):
    global visited, printed
    visited[int(node)-1] = 1
    printed.append(int(node))
    for i in graph[int(node)]:
        if i not in visited:
            DFS_visit(graph, i)

def DFS(graph, end_point):
    global printed
    places = "Places: "
    for i in graph:
        if i not in visited:
            DFS_visit(graph, i)
    end_idx = printed.index(int(end_point))
    for j in range(0, end_idx+1):
        places += str(printed[j]) + " "
    return places



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

def write_file():
    p = DFS(g, "12")
    output_f = open("output3.txt", "w")
    output_f.write(p)
    output_f.close()
    f.close()
    print("CODE EXECUTED!!!!!!!!!!")

f = open("input-1,2,3.txt", "r")
n = int(f.readline())
visited = [0] * n
printed = []
g = doBuildGraph()
write_file()



