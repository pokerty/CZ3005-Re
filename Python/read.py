
import json

G = open('G.json')
Dist = open('DistTest.json')
Cost = open('Cost.json')

# returns JSON object as
# a dictionary
mapdata = json.load(G)
distdata = json.load(Dist)
costdata = json.load(Cost)
# Iterating through the json
# list

for i in distdata:
    j = i.split(',')
    print(int(j[0]), int(j[1]), float(distdata[i]), int(costdata[i]))
    # print(distdata[i])
    # print(mapdata[i])
 
# Closing file
G.close()
Dist.close()
Cost.close()