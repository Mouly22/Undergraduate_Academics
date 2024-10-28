from queue import PriorityQueue

def find_shortest_paths(graph, start):
    pq = PriorityQueue()
    parents = {}
    visited = {}
    distances = {}

    for node in graph.keys():
        parents[node] = None
        visited[node] = False
        distances[node] = float('inf')

    distances[start] = 0
    pq.put((0, start))
    val = ''
    while not pq.empty():
        weight, node = pq.get()
        if visited[node]:
            continue
        visited[node] = True
        if node in graph:
            for neighbor, edge_weight in graph[node]:
                new_distance = weight + edge_weight
                if distances[neighbor] > new_distance:
                    distances[neighbor] = new_distance
                    pq.put((new_distance, neighbor))
                    parents[neighbor] = node
    
                    
    for m, n in distances.items():
        if n == float('inf'):
            n = -1
        val += str(n) + ' '
    out61.write(val)


inp61 = open('/Users/mouly/Downloads/input1_2.txt', 'r')
out61 = open('/Users/mouly/Downloads/output1_2.txt', 'w')
line1 = inp61.readline().split()
graph = {}
ulst = []
for val in range(int(line1[1])):
    lines = inp61.readline().split()
    if int(lines[0]) not in graph.keys():
        graph[int(lines[0])] = [(int(lines[1]), int(lines[2]))]
    else:
        graph[int(lines[0])].append((int(lines[1]), int(lines[2])))
    if int(lines[0]) not in ulst:
        ulst.append(int(lines[0]))
    if int(lines[1]) not in ulst:
        ulst.append(int(lines[1]))
g = {}
for elm in ulst:
    if elm in graph.keys():
        g[elm] = graph[elm]   
    else:
        g[elm] = []  
graph = g.copy()     


start = int(inp61.readline())

distances = find_shortest_paths(graph, start)
out61.close()
