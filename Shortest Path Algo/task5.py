# Task-5
import heapq


def Network(Graph, source):
    distance = {source: float('inf')}
    priority_Q = []
    prev_nodes = {}
    visited_nodes = []
    for i in range(len(Graph) + 1):
        visited_nodes.append(False)

    for key in Graph:
        if key != source:
            distance[key] = float('-inf')
        prev_nodes[key] = None

    heapq.heappush(priority_Q, source)
    while len(priority_Q) != 0:
        p = heapq._heappop_max(priority_Q)  # extract_max
        if not visited_nodes[p]:
            visited_nodes[p] = True
            for key, value in Graph[p].items():
                minimum = min(distance[p], value)
                if minimum > distance[key]:
                    prev_nodes[key] = p
                    distance[key] = minimum
                    heapq.heappush(priority_Q, key)
                    heapq._heapify_max(priority_Q)

    size = len(Graph)
    for k in range(1, size):
        if distance[k] == float('-inf'):
            distance[k] = -1

    distance[source] = 0
    data_rate = [distance[i] for i in range(1, size + 1)]
    return data_rate


def generate_output_format(g, s):
    global output_str
    temp_str = ""
    link = Network(g, s)
    for i in link:
        temp_str += str(i) + " "

    output_str += temp_str + "\n"


output_str = ""
f_output = open("output5.txt", "w")
with open("input5.txt") as openfileobj:
    t = int(openfileobj.readline())
    for i in range(t):
        nm_lst = openfileobj.readline().split()

        if nm_lst[1] == 0:
            s = int(openfileobj.readline())
            g = {nm_lst[0]: {}}  # edges
            generate_output_format(g, source)
        else:
            g = {}
            for j in range(int(nm_lst[1])):
                edges_line = openfileobj.readline().split()
                g[(int(edges_line[0]), int(edges_line[1]))] = int(edges_line[2])

            n = []
            for k in range(1, int(nm_lst[0]) + 1):
                n.append(k)

            nodeAdj = {}
            for v in n:
                nodeAdj.update({v: {}})

            for (u, nm_lst), w in g.items():
                nodeAdj[u][nm_lst] = w
            source = int(openfileobj.readline())
            generate_output_format(nodeAdj, source)

f_output.write(output_str)
openfileobj.close()
f_output.close()
print("CODE EXECUTED!!!!!!!!!!!!!!!!!!")