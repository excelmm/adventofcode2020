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
    minitext = i[(-1) * (len(i) - colonindex - 2):]
    requirement = i[colonindex - 1]
    intrequirement = i[:(colonindex - 2)]
    colonindex = 0
    for j in range(len(intrequirement)):
        if intrequirement[j] == '-':
            break
        colonindex += 1
    bottom = int(intrequirement[:(colonindex)])
    top = int(intrequirement[(colonindex + 1):])

    if (minitext[bottom - 1] == requirement and minitext[top - 1] != requirement):
        count += 1
        continue

    if (minitext[bottom - 1] != requirement and minitext[top - 1] == requirement):
        count += 1
        continue

print(count)