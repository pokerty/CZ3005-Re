# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
import json
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
# Create a graph given in
# the above diagram
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

graph = Graph()
# GRAPH PLUS 1 BECAUSE IT STARTS FROM 1 INSTEAD OF 0

for i in distdata:
    j = i.split(',')
    graph.addEdge(int(j[0]), int(j[1]), float(distdata[i]))
# EVERY NODE INDEX WILL MINUS 1

graph.BFS(2)
# Closing file
G.close()
Dist.close()
Cost.close()
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")

 
# This code is contributed by Neelam Yadav