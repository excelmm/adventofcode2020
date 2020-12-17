import copy

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().splitlines()

    space = []
    for i in range(31):
        slice = []
        for j in range(31):
            row = []
            for k in range(31):
                row.append(".")
            slice.append(row)
        space.append(slice)

    for index, i in enumerate(rawinput):
        for indexj, j in enumerate(i):
            space[15][index - len(rawinput) // 2 + 15][indexj- len(rawinput) // 2 + 15] = j
            
    for _ in range(6):
        space2 = copy.deepcopy(space)
        for indexi, i in enumerate(space): # For every 2d slice
            for indexj, j in enumerate(i): # For every row
                for indexk, k in enumerate(j): # For every cell
                    if k == "#" and countaround(space2, indexi, indexj, indexk) not in [2, 3]:
                        space[indexi][indexj][indexk] = "."
                    if k == "." and countaround(space2, indexi, indexj, indexk) == 3:
                        space[indexi][indexj][indexk] = "#"

    count = 0
    for i in space:
        for j in i:
            for k in j:
                if k == "#":
                    count += 1
                
    print(count)


def countaround (space, slice, row, col):
    count = 0
    if slice in [0, 30] or row in [0, 30] or col in [0, 30]:
        return 0;
    for i in range(slice - 1, slice + 2):
        for j in range(row - 1, row + 2):
            for k in range(col - 1, col + 2):
                if space[i][j][k] == "#":
                    count += 1
    
    if space[slice][row][col] == "#":
        count -= 1
    return count
        


if __name__ == "__main__":
    main()