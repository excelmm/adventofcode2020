with open("input.txt", "r") as f:
    input = f.read().splitlines()

bagsAllocation = {}
rawdata = []
splitupdata = []
temp = ''

for i in input:
    rawdata.append(i)
    splitupdata.append(i.split(" ", -1))

for i in splitupdata:
    temp2 = []
    for j in range(len(i)):
        temp = i[4:]
    for j in range(4, len(i) - 3, 4):
        temp2.append(i[j + 1] + i[j + 2])
            
    bagsAllocation[i[0] + i[1]] = temp2

count = 0
finalcount = -1
bags = []

def dfsUtil(u, node, visited, road_used, parent, it):
    global bags
    if u not in visited:
        visited.add(u)

        road_used.append([parent, u])

        for x in bagsAllocation[u]:
            if x == 'shinygold':
                if road_used[0][1] not in bags:
                    bags.append(road_used[0][1])
                return
            dfsUtil(x, node, visited, road_used, u, it + 1)

def dfs(i, node):
    visited = set()
    pathUsed = []
    dfsUtil(i, node, visited, pathUsed, -1, 0)

for i in bagsAllocation:
    dfs(i, 9)

print(len(bags))