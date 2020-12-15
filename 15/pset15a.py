with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()

rawinput2 = rawinput[0].split(",")
input = []
for i in rawinput2:
    input.append(int(i))

said = []
for i in range(2020):
    if i < len(input):
        said.append(input[i])
        continue
    if said.count(said[i - 1]) == 1:
        said.append(0)
        continue
    else:
        lastsaid = -1
        beforethat = -1
        for j in range(len(said)):
            if said[len(said) - j - 1] == said[i - 1]:
                if lastsaid == -1:
                    lastsaid = len(said) - j
                else:
                    beforethat = len(said) - j
                    break
        said.append(lastsaid - beforethat)


print(said[2019])