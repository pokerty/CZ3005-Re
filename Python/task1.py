# A Python program for Dijkstra's shortest
# path algorithm for adjacency
# list representation of graph
 
from collections import defaultdict
import sys
import json
import time 

 
class Heap():
 
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []
 
    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode
 
    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t
 
    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
 
        if (left < self.size and
           self.array[left][1]
            < self.array[smallest][1]):
            smallest = left
 
        if (right < self.size and
           self.array[right][1]
            < self.array[smallest][1]):
            smallest = right
 
        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:
 
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
 
            # Swap nodes
            self.swapMinHeapNode(smallest, idx)
 
            self.minHeapify(smallest)
 
    # Standard function to extract minimum
    # node from heap
    def extractMin(self):
 
        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return
 
        # Store the root node
        root = self.array[0]
 
        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
 
        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
 
        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)
 
        return root
 
    def isEmpty(self):
        return True if self.size == 0 else False
 
    def decreaseKey(self, v, dist):
 
        # Get the index of v in  heap array
 
        i = self.pos[v]
 
        # Get the node and update its dist value
        self.array[i][1] = dist
 
        # Travel up while the complete tree is
        # not heapified. This is a O(Logn) loop
        while (i > 0 and self.array[i][1] <
                  self.array[(i - 1) // 2][1]):
 
            # Swap this node with its parent
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swapMinHeapNode(i, (i - 1)//2 )
 
            # move to parent index
            i = (i - 1) // 2;
 
    # A utility function to check if a given
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):
 
        if self.pos[v] < self.size:
            return True
        return False
 
 
class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
 
    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):
 
        # Add an edge from src to dest.  A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. Edge[0]
        # has the destination and edge[1] has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)
 
        # Since graph is undirected, add an edge
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)
    

    # Function for printing path found
    def printPath(self,pi,node,destination):
        if pi[node] == -1:  # current node is source
            print(node,end="->")
            return
        self.printPath(pi,pi[node],destination)
        if node != destination:
            print(node,end="->")
        else:
            print(node,end=' ')
    
    # Function for printing result
    def printResult(self,dist,pi,destination):
        print('Shortest path: ',end='')    # Printing shortest path
        self.printPath(pi,destination,destination)
        print("\nShortest distance: ")  # Printing respective distance
        print(dist[destination])

    # The main function that calculates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src,dest):
        start_time = time.time()  # Mark the start time of dijkstra algorithm
        
        V = self.V  # Get the number of vertices in graph
        dist = []   # dist values used to pick minimum
                    # weight edge in cut
        pi = []     # array for predecessors for each vertex
 
        # minHeap represents set E
        minHeap = Heap()
 
        #  Initialize min heap with all vertices.
        # dist and pi value of all vertices
        for v in range(V):
            dist.append(1e7)
            pi.append(-1)
            minHeap.array.append( minHeap.
                                newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)
 
        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])
 
        # Initially size of min heap is equal to V
        minHeap.size = V;
 
        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:
 
            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # End if the destination node is reached
            if u == dest:
                end_time = time.time()  # Mark the end time of execution
                self.printResult(dist,pi,dest)
                print("\n--- Time taken for finding the shortest path (printing time exclusive): %s seconds ---" % (end_time - start_time))
                return

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for edge in self.graph[u]:
 
                v = edge[0]
 
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if (minHeap.isInMinHeap(v) and
                     dist[u] != 1e7 and \
                   edge[1] + dist[u] < dist[v]):
                        dist[v] = edge[1] + dist[u]
                        pi[v] = u
                        # update distance value
                        # in min heap also
                        minHeap.decreaseKey(v, dist[v])
 
        
 
 
 # Opening JSON file
Dist = open('Dist.json')
G = open('G.json')
# returns JSON object as
# a dictionary
distdata = json.load(Dist)
# Iterating through the json
# list

graph = Graph(264347)
# GRAPH PLUS 1 BECAUSE IT STARTS FROM 1 INSTEAD OF 0

for i in distdata:
    j = i.split(',')
    graph.addEdge(int(j[0]), int(j[1]), float(distdata[i]))
# EVERY NODE INDEX WILL MINUS 1

graph.dijkstra(1,50)

# Closing file
Dist.close()
G.close()



 
