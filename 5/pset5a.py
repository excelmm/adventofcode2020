with open("pset5.txt", "r") as f:
    inputs = f.read().splitlines()

max = 0

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
    
    if first7sum * 8 + last3sum > max:
        max = first7sum * 8 + last3sum

print(max)
    