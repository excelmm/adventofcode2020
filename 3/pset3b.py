with open("pset3.txt", "r") as f:
    map = f.read().splitlines()

rowlen = len(map)
collen = len(map[0])

count = 0
i = 0
j = 0

while True:
    if map[i][j] == '#':
        count += 1
    i += 2
    j += 1
    if j >= collen:
        j -= collen
    if i >= rowlen:
        break


print(count)