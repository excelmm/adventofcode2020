with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()
    
minute = int(rawinput[0])
rawinputlist = rawinput[1].split(',')
input = []
for i in rawinputlist:
	if i != 'x':
		input.append(int(i))

min = 1000000
minid = 0

for i in input:
	if (i - minute % i) < min:
		min = i - minute % i
		minid = i
		
print(min * minid)