# Task-1
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
    g = doBuildGraph()
    output_f = open("output1.txt", "w")
    output_f.write(str(g))


f = open("input-1,2,3.txt", "r")
n = int(f.readline())
write_file()
print("CODE EXECUTED!!!!!!!!")
