import re

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().splitlines()
    input = []
    for i in rawinput:
        input.append(simplify(i.replace(" ", "")))
    
    total = 0
    for i in input:
        total += calc(i)
    print(total)


def simplify(input):
    while ('(' in input):
        matches = re.findall(r"(\([ 0-9+*]+\))", input)
        for i in matches:
            input = input.replace(str(i), str(calc(i.replace("(", "").replace(")", ""))))
    return input


def calc(input):
    answer = 0
    current_op = '+'
    number = ''
    for i in input:
        if i != '*' and i != '+':
            number += i
        else:
            if current_op == '*':
                answer *= int(number)
            elif current_op == '+':
                answer += int(number)
            if i == '+':
                current_op = '+'
            elif i == '*':
                current_op = '*'
            number = ''
    if current_op == '*':
        answer *= int(number)
    elif current_op == '+':
        answer += int(number)
    return answer



if __name__ == "__main__":
    main()