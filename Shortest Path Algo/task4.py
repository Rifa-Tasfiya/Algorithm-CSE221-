# Task 4
def Dijkstra(Graph, source):
    global min_dist, path_cost
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
    path_cost = dist.get("MOGHBAZAR")
    return prev_node


def generateOutputFormat(graph, source):
    global path
    x = Dijkstra(graph, source)
    temp_path = ['MOGHBAZAR']
    visited_rev = "MOGHBAZAR"
    for j in range(0, len(x)):
        for key, val in x.items():
            if key == visited_rev:
                visited_rev = val
                temp_path.append(val)
    temp_path.reverse()
    for i in temp_path:
        path += str(i) + " "



path = ""
path_cost = 0
g = {}
output_f = open("output4.txt", "w")
with open("input4.txt") as openfileobj:
    for l in openfileobj:
        temp_lst = l.split()
        if len(temp_lst) != 0:
            u, v, w = temp_lst[0], temp_lst[1], int(temp_lst[2])
            if u not in g:
                g[u] = {}
            if v not in g:
                g[v] = {}
            g[u][v] = w
    generateOutputFormat(g, "Motijheel")

output_f.write("Sortest Path: " + path + "\n" + "Minimum level of traffic: " + str(path_cost))
openfileobj.close()
output_f.close()
print("CODE EXECUTED!!!!!!!!!!!!!!")
