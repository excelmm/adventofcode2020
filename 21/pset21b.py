from typing import final
from hopcroftkarp import HopcroftKarp

with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()

ingredientsList = set()
possibleIngredients = {}
allergenCanBe = {}
allergenNotPossibleToBe = {}

for i in rawinput:
    ingredients = i.split("(")[0].split(" ")[:-1]
    allergens = i[:-1].split("(")[1].split(" ")[1:]

    for ingredient in ingredients:
        ingredientsList.add(ingredient)

    for allergen in allergens:
        allergen = allergen.replace(",", "")
        if allergen not in possibleIngredients:
            possibleIngredients[allergen] = set()
            for i in ingredients:
                possibleIngredients[allergen].add(i)
        else:
            tempset = set()
            for i in possibleIngredients[allergen]:
                if i not in ingredients:
                    tempset.add(i)
            possibleIngredients[allergen] = {j for j in possibleIngredients[allergen] if j not in tempset}


candidates = [i for i in ingredientsList]
for i in ingredientsList:
    for k, v in possibleIngredients.items():
        for j in v:
            if i == j and i in candidates:
                candidates.remove(i)

answer = HopcroftKarp(possibleIngredients).maximum_matching(keys_only=True)
sortedKeys = sorted(answer)
for i in sortedKeys:
    print(answer[i], ",", sep="", end="")