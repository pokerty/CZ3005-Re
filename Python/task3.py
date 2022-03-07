import heapq
import json
import math
import time

def task3(g, dist, cost, coord, src, goal, budget):
    q = []
    goalx, goaly = coord[goal]
    srcx, srcy = coord[src]
    disttotarget = math.sqrt(math.pow((goalx - srcx), 2) + math.pow((goaly - srcy), 2))

    heapq.heappush(q, (disttotarget, 0, 0, [src]))
    visit = {src: set()}
    while q:
        p = heapq.heappop(q)
        path = p[3]
        # print(*path)
        cur = p[3][-1]

        if cur == goal:
            return path, p[1], p[2]
            
        for n in g[cur]:
            if n not in visit:
                visit[n] = set()
            visit[n].add(cur)
            tcost = p[2] + cost[str(cur) + ',' + str(n)]

            if tcost <= budget:
                tdist = p[1] + dist[str(cur) + ',' + str(n)]
                nx, ny = coord[n]
                heur = math.sqrt(math.pow((goalx - nx), 2) + math.pow((goaly - ny), 2))
                dist_heur = tdist + heur
                newpath = p[3] + [n]

                if n not in visit[cur]:
                    heapq.heappush(q, (dist_heur, tdist, tcost, newpath))
    return None




G = open('G.json')
Dist = open('Dist.json')
Cost = open('Cost.json')
Coord = open('Coord.json')

# returns JSON object as
# a dictionary
mapdata = json.load(G)
distdata = json.load(Dist)
costdata = json.load(Cost)
coorddata = json.load(Coord)
# Iterating through the json
# list

start_time = time.time()
result = task3(mapdata, distdata, costdata, coorddata, '1', '50', 287932)
end_time = time.time()
# Closing file
G.close()
Dist.close()
Cost.close()
Coord.close()


if result is None:
    print('No path under the budget exists.')
else:
    print('Shortest path:', end=' ')
    print('->'.join(str(x) for x in result[0]))
    print('Shortest distance: ' + str(result[1]))
    print('Total energy cost: ' + str(result[2]))
print("\n--- Time taken for finding the shortest path (printing time exclusive): %s seconds ---" % (end_time - start_time))