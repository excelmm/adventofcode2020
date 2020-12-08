with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

ids = []

for i in inputs:
    first7sum = 0
    last3sum = 0
    multiplier = 64
    for j in i[0:7]:
        if j == "B":
            first7sum += multiplier
        multiplier //= 2
    multiplier = 4
    for j in i[7:10]:
        if j == "R":
            last3sum += multiplier
        multiplier //= 2
    
    ids.append(first7sum * 8 + last3sum)

for i in range(len(ids) - 1):
    for j in range(i + 1, len(ids)):
        if abs(ids[j] - ids[i]) == 2:
            if ((ids[j] + ids[i]) // 2) not in ids:
                print((ids[i] + ids[j]) // 2)
            
            