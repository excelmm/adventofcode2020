with open("input.txt", "r") as f:
    rawinput = f.read()

deck_p1 = rawinput.split("\n\n")[0].split("\n")[1:]
deck_p2 = rawinput.split("\n\n")[1].split("\n")[1:]

print(deck_p1)
print(deck_p2)

while (len(deck_p1) and len(deck_p2)):
    card_1 = deck_p1.pop(0)
    card_2 = deck_p2.pop(0)
    if card_1 > card_2:
        deck_p1.append(card_1)
        deck_p1.append(card_2)
    else :
        deck_p2.append(card_2)
        deck_p2.append(card_1)

print(deck_p1)
print(deck_p2)

ans = 0
current_multiply = len(deck_p2)
for i in deck_p2:
    ans += int(i) * current_multiply
    current_multiply -= 1
print(ans)