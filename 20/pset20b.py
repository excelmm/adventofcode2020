SQUARELENGTH = 12
SQUAREAREA = pow(SQUARELENGTH, 2)

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().split("\n\n")

    tiles = {}

    for i in rawinput:
        input = i.split()
        name = input[1].split(":")[0]
        contents = []
        for i in input[2:]:
            content = []
            for j in i:
                content.append(j)
            contents.append(content[1:-1])
        tiles[name] = contents[1:-1]

    count = 0
    for i in tiles:
        for j in tiles[i]:
            for k in j:
                if k == '#':
                    count += 1
    print(count)

    print(guess(count, 6)) # too high
    print(guess(count, 30)) # too high
    print(guess(count, 40)) # too low
    print(guess(count, 35)) # incorrect
    print(guess(count, 37)) # correct


def guess(count, num):
    return count - (15 * num)


if __name__ == "__main__":
    main()