with open("test.txt", "r") as f:
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
        temp2.append(i[j] + i[j + 1] + i[j + 2])
            
    bagsAllocation[i[0] + i[1]] = temp2

# print(bagsAllocation['shinygold'])
bags = []

def dfsUtil(u, node, visited, road_used, parent, it):
    global bags
    if True:
        visited.add(u)

        road_used.append([parent, u])
        bags.append([parent, u, it])

        if len(bagsAllocation[u]) == 0:
            bags.append([u, "", 0])

        for x in bagsAllocation[u]:
            dfsUtil(x[1:], node, visited, road_used, u, x[0])

def dfs(i, node):
    visited = set()
    pathUsed = []
    dfsUtil(i, node, visited, pathUsed, -1, 0)

dfs('shinygold', 9)

finalbags = []
start = 0

for i in range(len(bags)):
    if len(finalbags) == 0:
        if bags[i][2] == 0 and bags[i][0] != -1:
            finalbags.append(bags[start:i + 1])
            start = i + 1
    else:
        if bags[i][2] == 0 and bags[i][0] != -1:
            for _ in range(len(bags)):
                j = 0
                if bags[start][0] == bags[j][1]:
                    break
                j += 1
            finalbags.append(bags[j:j + 1] + bags[start:i + 1])
            start = i + 1


def add(index, bags, end):
    if index == end - 1:
        return 1
    num = int(bags[index][2])
    if index == end - 2:
        return int(bags[index][2])
    else:
        return int(bags[index][2]) + int(bags[index][2]) * add(index + 1, bags, end)

print(bags)
print(finalbags)

finalbagsdict = {}

finaladd = 0
for i in finalbags:
    if i[0][0] == -1:
        if i[0][1] not in finalbagsdict:
            finalbagsdict[i[0][1]] = add(1, i, len(i))
        else:
            finalbagsdict[i[0][1]] = finalbagsdict.get(i[0][1]) + add(1, i, len(i))
    else:
        if i[0][0] not in finalbagsdict:
            finalbagsdict[i[0][0]] = add(0, i, len(i))
        else:
            finalbagsdict[i[0][0]] = finalbagsdict.get(i[0][0]) + add(0, i, len(i))
print(finalbagsdict)
