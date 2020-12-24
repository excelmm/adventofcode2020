import copy

SIZE = 251
MIDDLE = SIZE // 2

def main():
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

	for _ in range(100):
		grid2 = copy.deepcopy(grid)
		for i in range(1, SIZE - 1):
			for j in range(2, SIZE - 2):
				if grid2[i][j] == "b" and count_around(grid2, i, j)[1] not in [1, 2]:
					grid[i][j] = "w"
				if grid2[i][j] == "w" and count_around(grid2, i, j)[1] == 2:
					grid[i][j] = "b"

		
	count = 0
	for i in grid:
		for j in i:
			if j == "b": count += 1
	print(count)
	
	
def count_around(grid, i, j):
	countw, countb = 0, 0
	if grid[i][j - 2] == "w": countw += 1 
	else: countb += 1
	if grid[i][j + 2] == "w": countw += 1 
	else: countb += 1
	if grid[i + 1][j + 1] == "w": countw += 1 
	else: countb += 1
	if grid[i - 1][j - 1] == "w": countw += 1 
	else: countb += 1
	if grid[i + 1][j - 1] == "w": countw += 1 
	else: countb += 1
	if grid[i - 1][j + 1] == "w": countw += 1 
	else: countb += 1
	return countw, countb
		
main()