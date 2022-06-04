#Task-1
def Dijkstra(Graph, source):
    global min_dist
    dist = {source: 0}
    priority_que = []
    prev_node = {}
    for v in Graph:
        if v != source:
            dist[v] = float('inf')
            prev_node[v] = None
        priority_que.append(v)

    while len(priority_que) != 0:
        d = {}
        for p in priority_que:
            d.update({p: dist[p]})
        min_dist = min(d, key=d.get)
        priority_que.remove(min_dist)
        for key, val in Graph[min_dist].items():
            temp = dist[min_dist] + val
            if temp < dist[key]:
                dist[key] = temp
            prev_node[key] = min_dist

    return dist[min_dist]


line = open("input1.txt", "r")
t = line.readline()
output_file = open("output1.txt", "w")
output = ""
for i in range(int(t)):
    s = line.readline()
    nm_lst = s.split()
    n = int(nm_lst[0])
    m = int(nm_lst[1])
    g = {j: {} for j in range(1, n + 1)}

    for k in range(m):
        x = line.readline()
        temp_lst = x.split(" ")
        u, v, w = int(temp_lst[0]), int(temp_lst[1]), int(temp_lst[2])
        g[u][v] = w

    output += str(Dijkstra(g, 1)) + "\n"

output_file.write(output)
line.close()
output_file.close()
print("CODE EXECUTED!!!!!!!!!!!!!!!!!")
