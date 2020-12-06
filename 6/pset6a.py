with open("input.txt", "r") as f:
    text = f.read().splitlines()

count = 0

inputs = []
temp = ''

for i in text:
    if i == '':
        inputs.append(temp)
        temp = ''
        continue
    temp += " " + i
inputs.append(temp)

for i in inputs:
    question = []
    for j in i:
        if j != ' ' and j not in question:
            question.append(j)
            count += 1

print(count)