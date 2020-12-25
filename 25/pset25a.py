with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()

doorKey = int(rawinput[0])
cardKey = int(rawinput[1])
initialDoorKey = doorKey
initialCardKey = cardKey

doorLoops, doorS, doorV = 0, 7, 1
cardLoops, cardS, cardV = 0, 7, 1

while True:
    doorLoops += 1
    doorV *= doorS
    doorV %= 20201227
    if doorV == initialDoorKey:
        break

while True:
    cardLoops += 1
    cardV *= cardS
    cardV %= 20201227
    if cardV == initialCardKey:
        break

ansV = 1
for _ in range(cardLoops):
    ansV *= doorKey
    ansV %= 20201227

print(ansV)