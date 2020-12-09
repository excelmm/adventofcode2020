def main():
    with open("input.txt", "r") as f:
        inputraw = f.read().splitlines()

    input = []
    for i in inputraw:
        input.append(int(i))

    preamblesums = calculate(input[0:25])

    for i in range(25, len(input)):
        if (input[i]) not in preamblesums:
            print(input[i])
            exit(0)
        preamblesums = calculate(input[i - 24: i + 1])

    print(preamblesums)


def calculate(preamble):
    preamblesums = []
    for i in range(len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] != preamble[j]:
                preamblesums.append(preamble[i] + preamble[j])
    return preamblesums
    

if __name__ == "__main__":
    main()