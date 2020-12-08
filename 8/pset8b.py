import copy

with open("input.txt", "r") as f:
    input = f.read().splitlines()

executed = [0]*len(input)
accumulator, swapindex, i = 0, 0, 0

while True:
    if input[swapindex][0:3] != 'jmp' and input[swapindex][0:3] != 'nop':
        i = 0
        swapindex += 1
        continue
    while True:
        if input[i][0:3] == 'acc':
            if input[i][4] == '+':
                accumulator += int(input[i][5:])
            else:
                accumulator -= int(input[i][5:])
        elif input[i][0:3] == 'jmp':
            if i == swapindex:
                i += 1
                continue
            if input[i][4] == '+':
                i += int(input[i][5:]) - 1
            else:
                i -= (int(input[i][5:]) + 1)
        elif input[i][0:3] == 'nop':
            if i == swapindex:
                if input[i][4] == '+':
                    i += int(input[i][5:]) - 1
                else:
                    i -= (int(input[i][5:]) + 1)
        if i == len(input) - 1:
            print(accumulator)
            exit()
        if executed[i] == 1:
            i = 0
            swapindex += 1
            executed = [0] * len(input)
            accumulator = 0
            break
        executed[i] = 1
        i += 1