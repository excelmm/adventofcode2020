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
                if count2(input2, i, j) == 0 and input2[i][j] == 'L':
                    input[i][j] = "#"
                if count2(input2, i, j) >= 4 and input2[i][j] == '#':
                    input[i][j] = "L"
        
        if input == input2:
            break
    
    count = 0
    for i in input:
        count += i.count("#")
    print(count)
            

def count2(input, i, j):
    count = 0
    count += "".join(input[i - 1][j - 1: j + 2]).count("#")
    count += "".join(input[i ][j - 1: j + 2]).count("#")
    count += "".join(input[i + 1][j - 1: j + 2]).count("#")
    if input[i][j] == '#':
        count -= 1
    return count


if __name__ == "__main__":
    main()