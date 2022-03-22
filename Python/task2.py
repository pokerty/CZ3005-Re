import heapq
import json
import time

def task2(g, dist, cost, src, goal, budget):
    q = []
    heapq.heappush(q, (0, 0, [src]))
    visit = {src: set()}
    while q:
        p = heapq.heappop(q)
        path = p[2]
        cur = p[2][-1]

        if cur == goal:
            return path, p[0], p[1]

        for n in g[cur]:
            if n not in visit:
                visit[n] = set()
            visit[n].add(cur)
            tcost = p[1] + cost[str(cur) + ',' + str(n)]

            if (tcost <= budget) and (n not in visit[cur]):
                tdist = p[0] + dist[str(cur) + ',' + str(n)]
                newpath = p[2] + [n]
                heapq.heappush(q, (tdist, tcost, newpath))
    return None

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
start_time = time.time()
result = task2(mapdata, distdata, costdata, '1', '50', 287932)
end_time = time.time()

# Closing file
G.close()
Dist.close()
Cost.close()

if result is None:
    print('No path under the budget exists.')
else:
    print('Shortest path:', end=' ')
    print('->'.join(str(x) for x in result[0]))
    print('Shortest distance: ' + str(result[1]))
    print('Total energy cost: ' + str(result[2]))
print("\n--- Time taken for finding the shortest path (printing time exclusive): %s seconds ---" % (end_time - start_time))