with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()

input = []
for i in rawinput:
    input.append(int(i))
input.append(0)

input.sort()
diff1, diff3 = 0, 0

if (input[0]) == 1:
    diff1 += 1
elif (input[0]) == 3:
    diff3 += 1

for i in range(1, len(input)):
    if input[i] - input[i - 1] == 1:
        diff1 += 1
    elif input[i] - input[i - 1] == 3:
        diff3 += 1

diff3 += 1

print(diff1 * diff3)