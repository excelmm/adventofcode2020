import copy

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read()

    deck_p1 = rawinput.split("\n\n")[0].split("\n")[1:]
    deck_p2 = rawinput.split("\n\n")[1].split("\n")[1:]

    for i in range(len(deck_p1)):
        deck_p1[i]  = int(deck_p1[i])
    for i in range(len(deck_p2)):
        deck_p2[i]  = int(deck_p2[i])

    winner = play(deck_p1, deck_p2)
    
    if winner == "p1":
        print(countAnswer(deck_p1))
    if winner == "p2":
        print(countAnswer(deck_p2))


def countAnswer(deck):
    ans = 0
    current_multiply = len(deck)
    for i in deck:
        ans += i * current_multiply
        current_multiply -= 1
    return ans
 

def play(deck_p1, deck_p2):

    winner = ""
    visiteddecks_p1 = []
    visiteddecks_p2 = []
    
    while (len(deck_p1) and len(deck_p2)):

        if deck_p1 in visiteddecks_p1 and deck_p2 in visiteddecks_p2:
            return "p1"

        visiteddecks_p1.append(copy.deepcopy(deck_p1))
        visiteddecks_p2.append(copy.deepcopy(deck_p2))

        card_p1 = deck_p1.pop(0)
        card_p2 = deck_p2.pop(0)

        if card_p1 <= len(deck_p1) and card_p2 <= len(deck_p2):
            new_deck_p1 = copy.deepcopy(deck_p1[:card_p1])
            new_deck_p2 = copy.deepcopy(deck_p2[:card_p2])
            winner = play(new_deck_p1, new_deck_p2)
        else:
            winner = "p1" if card_p1 > card_p2 else "p2"

        if winner == "p1":
            deck_p1.append(card_p1)
            deck_p1.append(card_p2)
        else:
            deck_p2.append(card_p2)
            deck_p2.append(card_p1)

    winner = "p1" if len(deck_p1) else "p2"
    return winner

if __name__ == "__main__":
    main()
