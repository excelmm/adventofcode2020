with open("input.txt", "r") as f:
    input = f.read().splitlines()

executed = [0]*len(input)
accumulator = 0
i = 0
while True:
    if input[i][0:3] == 'acc':
        if input[i][4] == '+':
            accumulator += int(input[i][5:])
        else:
            accumulator -= int(input[i][5:])
    elif input[i][0:3] == 'jmp':
        if input[i][4] == '+':
            i += int(input[i][5:]) - 1
        else:
            i -= (int(input[i][5:]) + 1)
    if executed[i] == 1:
        break
    executed[i] = 1
    i += 1

print(accumulator)