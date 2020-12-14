import re
from itertools import chain, combinations
import copy

def main():
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    sumofall = {}
    mask = ''
    for i in input:

        # Parse inputs
        if 'mask' in i:
            mask = i[7:]
            continue
        regex = re.search(r'mem\[(\d+)\] = (.*)', i)
        initialAddress = regex.group(1)
        initialValue = regex.group(2)
        
        initialAddressBinary = bin(int(initialAddress))[2:]

        # Convert initial address to binary
        for i in range(len(mask) - len(initialAddressBinary)):
            initialAddressBinary = "0" + initialAddressBinary

        # get the memmory address
        for i, char in enumerate(mask): 
            if char != '0':
                initialAddressBinary = initialAddressBinary[:i] + char + initialAddressBinary[i + 1:]

        # Find out indexes of "X" in the address
        Xindexes = []
        for i, char in enumerate(initialAddressBinary):
            if char == 'X':
                Xindexes.append(i)

        # Write for every possible combination of floating bits
        combs = list(powerset(Xindexes))
        for i in combs:
            newAddressBinary = copy.deepcopy(initialAddressBinary)
            for j in i:
                newAddressBinary = newAddressBinary[:j] + "1" + newAddressBinary[j + 1:]
            newAddressBinary = newAddressBinary.replace("X", "0")
            sumofall[int(newAddressBinary, 2)] = int(initialValue)

    # Sum final
    sum = 0
    for i, j in sumofall.items():
        sum += j       
    print(sum)


# Find all subsets of a set
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

if __name__ == "__main__":
    main()