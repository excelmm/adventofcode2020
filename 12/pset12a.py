with open("input.txt" , "r") as f:
    rawinput = f.read().splitlines()

x = 0
y = 0
currentdirarray = ['E', 'S', 'W', 'N']
currentdirindex = 0

for i in rawinput:
    steps = int(i[1:])
    if i[0] == 'F':
        if currentdirarray[currentdirindex] == 'E':
            x += steps
        elif currentdirarray[currentdirindex] == 'S':
            y -= steps
        elif currentdirarray[currentdirindex] == 'W':
            x -= steps
        else:
            y += steps
    elif i[0] == 'R':
        currentdirindex += steps // 90
        if currentdirindex > 3:
            currentdirindex -= 4
    elif i[0] == 'L':
        currentdirindex -= steps // 90
        if currentdirindex < 0:
            currentdirindex += 4
    elif i[0] == 'E':
        x += steps
    elif i[0] == 'S':
        y -= steps
    elif i[0] == 'W':
        x -= steps
    else :
        y += steps

print(abs(x) + abs(y))