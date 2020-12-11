import copy

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().splitlines()


    for i in range(len(rawinput)):
        rawinput[i] = '.' + rawinput[i] + '.'

    floor = ''
    for i in range(len(rawinput[0])):
        floor += '.'
    rawinput.append(floor)
    rawinput.insert(0, floor)
    input = []
    for i in rawinput:
        input.append(list(i))

    while True:
        input2 = copy.deepcopy(input)

        for i in range(1, len(input) - 1):
            for j in range(1, len(input[i]) - 1):
                if count2(input2, i, j, i, j, 0) == 0 and input2[i][j] == 'L':
                    input[i][j] = "#"
                if count2(input2, i, j, i, j, 0) >= 5 and input2[i][j] == '#':
                    input[i][j] = "L"
        
        if input == input2:
            break
    
    count = 0
    for i in input:
        count += i.count("#")
    print(count)
            

def count2(input, initi, initj, i, j, dir):

    rows = len(input)
    cols = len(input[0])

    count = 0
    if dir == 0:
        if i == 0:
            count = 0
        elif input[i - 1][j] == '#':
            count = 1
        elif input[i - 1][j] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i - 1, j, dir)
        return count + count2(input, initi, initj, initi, initj, dir=1)
    elif dir == 1:
        if i == 0 or j == cols - 1:
            count = 0
        elif input[i - 1][j + 1] == '#':
            count = 1
        elif input[i - 1][j + 1] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i - 1, j + 1, dir)
        return count + count2(input, initi, initj, initi, initj, dir=2)
    elif dir == 2:
        if j == cols - 1:
            count = 0
        elif input[i][j + 1] == '#':
            count = 1
        elif input[i][j + 1] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i, j + 1, dir)
        return count + count2(input, initi, initj, initi, initj, dir=3)
    elif dir == 3:
        if i == rows - 1 or j == cols - 1:
            count = 0
        elif input[i + 1][j + 1] == '#':
            count = 1
        elif input[i + 1][j + 1] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i + 1, j + 1, dir)
        return count + count2(input, initi, initj, initi, initj, dir=4)
    elif dir == 4:
        if i == rows - 1:
            count = 0
        elif input[i + 1][j] == '#':
            count = 1
        elif input[i + 1][j] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i + 1, j, dir)
        return count + count2(input, initi, initj, initi, initj, dir=5)
    elif dir == 5:
        if i == rows - 1 or j == 0:
            count = 0
        elif input[i + 1][j - 1] == '#':
            count = 1
        elif input[i + 1][j - 1] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i + 1, j - 1, dir)
        return count + count2(input, initi, initj, initi, initj, dir=6)
    elif dir == 6:
        if j == 0:
            count = 0
        elif input[i][j - 1] == '#':
            count = 1
        elif input[i][j - 1] == 'L':
            count = 0
        else:
            return count + count2(input, initi, initj, i, j - 1, dir)
        return count + count2(input, initi, initj, initi, initj, dir=7)
    elif dir == 7:
        if i == 0 or j == 0:
            return 0
        elif input[i - 1][j - 1] == '#':
            return 1
        elif input[i - 1][j - 1] == 'L':
            return 0
        else:
            return count + count2(input, initi, initj, i - 1, j - 1, dir)

    if input[i][j] == '#':
        count -= 1
    return count


if __name__ == "__main__":
    main()