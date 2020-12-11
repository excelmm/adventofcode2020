def main():
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    bagsAllocation = {}
    rawdata = []
    splitupdata = []
    temp = ''

    for i in input:
        rawdata.append(i)
        splitupdata.append(i.split(" ", -1))

    for i in splitupdata:
        temp2 = []
        for j in range(len(i)):
            temp = i[4:]
        for j in range(4, len(i) - 3, 4):
            temp2.append(i[j] + i[j + 1] + i[j + 2])
                
        bagsAllocation[i[0] + i[1]] = temp2

    print(add('shinygold', bagsAllocation))


def add(key, bagsAllocation):
    summation = 0
    if len(bagsAllocation.get(key)) == 0:
        return 0
    for i in bagsAllocation.get(key):
        summation += int(i[0]) + int(i[0]) * add(i[1:], bagsAllocation)
    return summation

if __name__ == "__main__":
    main()