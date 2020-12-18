import enum
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
    total = 1
    evals = input.split('*')
    for i in evals:
        total *= eval(i)
    return total

if __name__ == "__main__":
    main()