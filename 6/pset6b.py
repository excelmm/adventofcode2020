import copy

with open("pset6.txt", "r") as f:
    text = f.read().splitlines()

inputs = []
temp = ''

for i in text:
    if i == '':
        inputs.append(temp)
        temp = ''
        continue
    temp += " " + i
inputs.append(temp)

inputs2 = []

for i in inputs:
    temp3 = []
    temp2 = ''
    smallcount = 0
    for j in i:
        if j == ' ' and smallcount == 0:
            smallcount += 1
            continue
        if j == ' ':
            temp3.append(temp2)
            temp2 = ''
            continue
        temp2 += j
    temp3.append(temp2)
    inputs2.append(temp3)

count = 0

for i in inputs2:
    questions = []
    if len(i) == 1:
        for j in range(len(i)):
            for k in range(len(i[j])):
                questions.append(i[j][k])

        count += len(questions)
        continue

    for j in range(len(i)):
        if j == 0:
            for k in range(len(i[j])):
                questions.append(i[j][k])
            continue
        questions2 = copy.deepcopy(questions)
        for a in range(len(questions)):
            if questions[a] not in i[j]:
                questions2.remove(questions[a])
        
        questions = copy.deepcopy(questions2)
    
    count += len(questions2)

print(count)


    

