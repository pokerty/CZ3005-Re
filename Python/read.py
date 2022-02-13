
import json

G = open('G.json')
Dist = open('Dist.json')

# returns JSON object as
# a dictionary
mapdata = json.load(G)
distdata = json.load(Dist)
# Iterating through the json
# list

for i in distdata:
    j = i.split(',')
    print(j[0])
    # print(distdata[i])
    # print(mapdata[i])
 
# Closing file
G.close()
Dist.close()