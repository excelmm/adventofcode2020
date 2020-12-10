count = 0
database = {}

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().splitlines()

    input = []
    for i in rawinput:
        input.append(int(i))
    input.append(0) 

    input.sort()

    for i in input:
        database[i] = 0

    adj_list = dict()
    for i in input:
        adj_list[i] = []
    for i in range(len(input) - 3):
        for j in range(i + 1, i + 4):
            if input[j] - input[i] <= 3:
                adj_list[input[i]].append(input[j])

    for i in range(len(input) - 3, len(input) - 2):
        for j in range(i + 1, i + 3):
            if input[j] - input[i] <= 3:
                adj_list[input[i]].append(input[j])

    adj_list[input[-2]] = [input[-1]]

    database[input[-1]] = 1

    count = dfs(0, adj_list, input[-1])
    
    print(count)


def dfs(node, adj_list, destination):
    count = 0
    if database[node] != 0:
        return database[node]
    for x in adj_list[node]:
        if x == destination:
            count += 1
            return count
        count += dfs(x, adj_list, destination)
    database[node] = count
    return count


if __name__ == "__main__":
    main()