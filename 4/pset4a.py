with open("input.txt", "r") as f:
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

count = 0

for i in inputs:
    if 'byr:' in i and 'iyr:' in i and 'eyr:' in i and 'hgt:' in i and 'hcl:' in i and 'ecl:' in i and 'pid:' in i:
        count += 1

print(count)