from queue import PriorityQueue
import json

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

# Opening JSON file
G = open('G.json')
Dist = open('Dist.json')
Cost = open('Cost.json')

# returns JSON object as
# a dictionary
mapdata = json.load(G)
distdata = json.load(Dist)
costdata = json.load(Cost)

# Iterating through the json
# list

g = Graph(264347)
# GRAPH PLUS 1 BECAUSE IT STARTS FROM 1 INSTEAD OF 0

for i in distdata:
    j = i.split(',')
    g.add_edge(int(j[0]), int(j[1]), float(distdata[i]))
# EVERY NODE INDEX WILL MINUS 1

# Closing file
G.close()
Dist.close()
Cost.close()

# g = Graph(9)
# g.add_edge(0, 1, 4)
# g.add_edge(0, 6, 7)
# g.add_edge(1, 6, 11)
# g.add_edge(1, 7, 20)
# g.add_edge(1, 2, 9)
# g.add_edge(2, 3, 6)
# g.add_edge(2, 4, 2)
# g.add_edge(3, 4, 10)
# g.add_edge(3, 5, 5)
# g.add_edge(4, 5, 15)
# g.add_edge(4, 7, 1)
# g.add_edge(4, 8, 5)
# g.add_edge(5, 8, 12)
# g.add_edge(6, 7, 1)
# g.add_edge(7, 8, 3) 

D = dijkstra(g, 1)

print(D)