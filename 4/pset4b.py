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

print(inputs)
print(inputs2)


for i in inputs2:
    valid = 0
    byr = 0
    iyr = 0
    eyr = 0
    hgt = 0
    hcl = 0
    ecl = 0
    pid = 0
    if len(i) <= 6:
        continue
    for j in i:
        if 'byr' in j:
            if len(j) != 8 or int(j[4:8]) < 1920 or len(j) != 8 or int(j[4:8]) > 2002:
                break
            valid += 1
            byr += 1
        if 'iyr' in j:
            if len(j) != 8 or int(j[4:8]) < 2010 or len(j) != 8 or int(j[4:8]) > 2020:
                break
            valid += 1
            iyr += 1
        if 'eyr' in j:
            if len(j) != 8 or int(j[4:8]) < 2020 or len(j) != 8 or int(j[4:8]) > 2030:
                break
            valid += 1
            eyr += 1
        if 'hgt' in j:
            if len(j) not in [8, 9]:
                break
            if 'cm' in j:
                if int(j[4:-2]) < 150 or int(j[4:-2]) > 193:
                    break
            if 'in' in j:
                if int(j[4:-2]) < 59 or int(j[4:-2]) > 76:
                    break
            if 'cm' not in j and 'in' not in j:
                break
            valid += 1
            hgt += 1
        if 'hcl' in j:
            if j[4] != '#' or len(j) != 11:
                break
            if j[5:11].isalnum() is False:
                break
            valid += 1
            hcl += 1
        if 'ecl' in j:
            if len(j) != 7:
                break
            if 'amb' not in j and 'blu' not in j and 'brn' not in j and 'gry' not in j and 'grn' not in j and 'hzl' not in j and 'oth' not in j:
                break
            valid += 1
            ecl += 1
        if 'pid' in j:
            if len(j) != 13:
                break
            if j[5:14].isnumeric() is False:
                break
            valid += 1
            pid += 1
        print(i, valid)
    if valid >= 7 and byr == 1 and iyr == 1 and eyr == 1 and hgt == 1 and hcl == 1 and ecl == 1 and pid == 1:
        count += 1

print(count)

        