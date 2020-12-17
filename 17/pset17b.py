import copy

SPACELIMIT = 31
MIDDLE = SPACELIMIT // 2

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().splitlines()

    space = []
    for a in range(SPACELIMIT):
        superslice = []
        for i in range(SPACELIMIT):
            slice = []
            for j in range(SPACELIMIT):
                row = []
                for k in range(SPACELIMIT):
                    row.append(".")
                slice.append(row)
            superslice.append(slice)
        space.append(superslice)

    for index, i in enumerate(rawinput):
        for indexj, j in enumerate(i):
            space[MIDDLE][MIDDLE][index - len(rawinput) // 2 + MIDDLE][indexj- len(rawinput) // 2 + MIDDLE] = j
            
    for iteration in range(6):
        space2 = copy.deepcopy(space)
        for indexa, a in enumerate(space): # For every 3d superslice
            for indexi, i in enumerate(a): # For every 2d slice
                for indexj, j in enumerate(i): # For every row
                    for indexk, k in enumerate(j): # For every cell
                        if k == "#" and countaround(space2, indexa, indexi, indexj, indexk) not in [2, 3]:
                            space[indexa][indexi][indexj][indexk] = "."
                        if k == "." and countaround(space2, indexa, indexi, indexj, indexk) == 3:
                            space[indexa][indexi][indexj][indexk] = "#"

    count = 0
    for a in space:
        for i in a:
            for j in i:
                for k in j:
                    if k == "#":
                        count += 1
                
    print(count)


def countaround (space, superslice, slice, row, col):
    count = 0
    if superslice in [0, SPACELIMIT - 1] or slice in [0, SPACELIMIT - 1] or row in [0, SPACELIMIT - 1] or col in [0, SPACELIMIT - 1]:
        return 0;
    for a in range(superslice - 1, superslice + 2):
        for i in range(slice - 1, slice + 2):
            for j in range(row - 1, row + 2):
                for k in range(col - 1, col + 2):
                    if space[a][i][j][k] == "#":
                        count += 1
    
    if space[superslice][slice][row][col] == "#":
        count -= 1
    return count
        


if __name__ == "__main__":
    main()