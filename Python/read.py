
import json

G = open('G.json')
Dist = open('DistTest.json')

# returns JSON object as
# a dictionary
mapdata = json.load(G)
distdata = json.load(Dist)
# Iterating through the json
# list

for i in distdata:
    j = i.split(',')
    print(int(j[0]), int(j[1]), float(distdata[i]))
    # print(distdata[i])
    # print(mapdata[i])
 
# Closing file
G.close()
Dist.close()