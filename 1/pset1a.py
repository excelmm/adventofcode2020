with open("pset1.txt", "r") as f:
    list = f.read().splitlines()
    
numlist = []

for i in list:
    numlist.append(int(i))

for i in range(len(numlist) - 2):
    for j in range(i + 1, len(numlist) - 1):
        if numlist[i] + numlist[j] == 2020:
            print("result:", numlist[i], "*", numlist[j], "=", numlist[i] * numlist[j])
            exit(0)