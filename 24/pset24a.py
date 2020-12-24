SIZE = 201
MIDDLE = SIZE // 2

with open("input.txt", "r") as f:
	rawinput = f.read().splitlines()

grid = []
for i in range(SIZE):
	row = []
	for j in range(SIZE):
		row.append("w")
	grid.append(row)

for line in rawinput:
	i, j = MIDDLE, MIDDLE
	line_ptr = 0
	while line_ptr < len(line):
		dir = line[line_ptr : line_ptr + 2]
		if dir == "se":
			i += 1
			j += 1
		elif dir == "sw":
			i += 1
			j -= 1
		elif dir == "ne":
			i -= 1
			j += 1
		elif dir == "nw":
			i -= 1
			j -= 1
		elif dir[:1] == "w":
			j -= 2
		elif dir[:1] == "e":
			j += 2
		if dir [:1] in ["w", "e"]:
			line_ptr += 1
		else:
			line_ptr += 2
	grid[i][j] = "w" if grid[i][j] =="b" else "b"
	
count = 0
for i in grid:
	for j in i:
		if j == "b": count += 1
print(count)