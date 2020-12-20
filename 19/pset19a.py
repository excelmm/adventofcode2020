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
    count = 0
    for i in texts:
        if re.fullmatch(fitsRule0, i):
            count += 1
    print(count)


def getRegex(rules, rule):
    return "("+"|".join( "".join(getRegex(rules, x) if x.isdigit() else x.replace("\"", "") for x in p) for p in rules[rule]) +")"


if __name__ == "__main__":
    main()