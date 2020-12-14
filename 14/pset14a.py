import re

def main():
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    sumofall = [0] * 100000
    mask = ''
    for i in input:
        if 'mask' in i:
            mask = i[7:]
            continue 
        regex = re.search(r'mem\[(\d+)\] = (.*)', i)
        address = regex.group(1)
        numberToWrite = regex.group(2)
        numberToWriteBinary = bin(int(numberToWrite))[2:]
        for i in range(len(mask) - len(numberToWriteBinary)):
            numberToWriteBinary = "0" + numberToWriteBinary
        for i, char in enumerate(mask): 
            if char != 'X':
                numberToWriteBinary = numberToWriteBinary[:i] + char + numberToWriteBinary[i + 1:]
        sumofall[int(address)] = int(numberToWriteBinary, 2)
    print(sum(sumofall))


if __name__ == "__main__":
    main()