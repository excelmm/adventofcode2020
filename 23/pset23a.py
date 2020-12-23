with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()

input = []
for i in rawinput[0]:
    input.append(int(i))
    
for _ in range(100):
    current_cup = input[0]
    three_cups = [input[1], input[2], input[3]]
    destination_cup = current_cup - 1
    if destination_cup < min(input):
        destination_cup = max(input)
    while destination_cup in three_cups:
        destination_cup -= 1
        if destination_cup < min(input):
            destination_cup = max(input)
            
    destination_cup_index = input.index(destination_cup)
    for i in three_cups:
        input.insert(destination_cup_index + 1, i)
        destination_cup_index += 1
    for i in three_cups:
        input.remove(i)
    input = input[1:] + [input[0]]

while input[0] != 1:
    input = input[1:] + [input[0]]

for i in input[1:]:
    print(i, end="")