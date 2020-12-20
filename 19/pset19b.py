from os import terminal_size
import re

def main():
    with open("input.txt", "r") as f:
        rulesinput, texts = f.read().split("\n\n")
        rulesinput = rulesinput.split("\n")
        texts = texts.split("\n")
    
    rules = {}
    for i in rulesinput:
        name = i.split(": ")[0]
        ruleset = i.split(": ")[1]
        ruleset = ruleset.split(" | ")
        ruleset2 = []
        for i in ruleset:
            ruleset3 = i.split(" ")
            ruleset2.append(ruleset3)
        rules[name] = ruleset2
    # print(rules)

    fitsRule0 = getRegex(rules, '0')
    fitsRule42 = getRegex(rules, '42')
    fitsRule31 = getRegex(rules, '31')


    count = 0
    for i in texts:
        if re.fullmatch(fitsRule0, i):
            count += 1
        if check_repeat(i, fitsRule42, fitsRule31, fitsRule0):
            count += 1
    print(count)


def getRegex(rules, rule):
    return "("+"|".join( "".join(getRegex(rules, x) if x.isdigit() else x.replace("\"", "") for x in p) for p in rules[rule]) +")"


def check_repeat(line, fitsRule42, fitsRule31, fitsRule0):
    if re.match(fitsRule42, line) and not re.fullmatch(fitsRule0, line):
        i, j = 0, 0
        while (m := re.match(fitsRule42, line)):
            low, high = m.span()
            line, i = line[high:], i + 1
        if len(line) == 0: return False
        while (m := re.match(fitsRule31, line)):
            low, high = m.span()
            line, j = line[high:], j + 1
        return len(line) == 0 and i > j
    else: return False


if __name__ == "__main__":
    main()