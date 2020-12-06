def compute(map, row, col):

    rowlen = len(map)
    collen = len(map[0])

    count = 0
    i = 0
    j = 0

    while True:
        if map[i][j] == '#':
            count += 1
        i += row
        j += col
        if j >= collen:
            j -= collen
        if i >= rowlen:
            break


    return count

with open("pset3.txt", "r") as f:
    map = f.read().splitlines()

print(compute(map, 1, 1) * compute(map, 1, 3) * compute(map, 1, 5) * compute(map, 1, 7) * compute(map, 2, 1))