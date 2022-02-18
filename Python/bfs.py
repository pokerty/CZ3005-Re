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
 
    def backtrace(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        for i in path:
            print("old path is", i, end="->")
        path.reverse()
        for i in path:
            print("path is", i, end="->")
        return path

    # Function to print a BFS of graph
    def BFS(self, s, d):
        # dict for parent node
        parent = {}
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        cur = s;  #mark current node
        queue.append(cur)
        visited[cur] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            cur = queue.pop(0)
            # print("it is traversing", cur) #test
            # print (cur, end = " ")
            if cur == d: #if dest found
                path = []
                while cur!=s: #backtrace while parent not source
                    path.append(cur)
                    cur=parent[cur]
                # path.append(s) #add source
                path.reverse() #reverse
                print(s, end=" ") #start
                for i in path:
                    print("->", i, end=" ")
                # self.backtrace(parent, s, d)
                return 
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[cur]:
                if visited[i] == False:
                    parent[i] = cur #add parent of cur node to dict
                    # print ("parent of", i  ,"is", parent[i]) #test
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

for i in costdata:
    j = i.split(',')
    graph.addEdge(int(j[0]), int(j[1]))
    # graph.addEdge(int(j[0]), int(j[1]), int(costdata[i]))
# EVERY NODE INDEX WILL MINUS 1

print ("The breadth first traversal path for 1 to 50 is")
graph.BFS(1, 50)
# Closing file
G.close()
Dist.close()
Cost.close()
 


 
# This code is contributed by Neelam Yadav