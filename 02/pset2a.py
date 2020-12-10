with open("input.txt", "r") as f:
    text = f.read().splitlines()

count = 0   

for i in text:
    colonindex = 0
    for j in range(len(i)):
        if i[j] == ':':
            break
        colonindex += 1
    # print(colonindex)
    text = i[(-1) * (len(i) - colonindex - 2):]
    requirement = i[colonindex - 1]
    intrequirement = i[:(colonindex - 2)]
    colonindex = 0
    for j in range(len(intrequirement)):
        if intrequirement[j] == '-':
            break
        colonindex += 1
    bottom = int(intrequirement[:(colonindex)])
    top = int(intrequirement[(colonindex + 1):])
    # print(text)
    # print(requirement)
    # print(bottom, top)
    count2 = 0
    for j in text:
        if j == requirement:
            count2 += 1
    if bottom <= count2 <= top:
        count += 1

print(count)