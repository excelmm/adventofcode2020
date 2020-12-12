from os import X_OK


with open("input.txt" , "r") as f:
    rawinput = f.read().splitlines()

x = 0
y = 0
wpx = 10
wpy = 1

for i in rawinput:
    oldwpx = wpx
    oldwpy = wpy
    steps = int(i[1:])
    if i[0] == 'F':
        x += steps * wpx
        y += steps * wpy
    elif i[0] == 'R':
        if steps == 90:
            wpy = (-1) * (oldwpx)
            wpx = (oldwpy)
        elif steps == 180:
            wpx = (-1) * (oldwpx)
            wpy = (-1) * (oldwpy)
        elif steps == 270:
            wpx = (-1) * (oldwpy)
            wpy = oldwpx
    elif i[0] == 'L':
        if steps == 90:
            wpx = (-1) * (oldwpy)
            wpy = oldwpx
        elif steps == 180:
            wpx = (-1) * (oldwpx)
            wpy = (-1) * (oldwpy)
        elif steps == 270:
            wpy = (-1) * (oldwpx)
            wpx = (oldwpy)
    elif i[0] == 'E':
        wpx += steps
    elif i[0] == 'S':
        wpy -= steps
    elif i[0] == 'W':
        wpx -= steps
    else :
        wpy += steps

print(abs(x) + abs(y))