NUM = 30000000

with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()

rawinput2 = rawinput[0].split(",")
input = []
for i in rawinput2:
    input.append(int(i))

database = {}
for i, num in enumerate(input):
    database[num] = []
    database[num].append(i)

for i in range(len(input), NUM):
    previous = input[i - 1]
    if previous not in database:
        database[previous] = []
    if len(database[previous]) == 1:
        current = 0
    else:
        current = i - 1 - database[previous][-2]
    input.append(current)
    if current not in database:
        database[current] = []
    database[current].append(i)

print(input[NUM - 1])