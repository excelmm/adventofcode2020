#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <iterator>
#include "C:\\Users\\Excel PC\\Documents\\GitHub\\excelmm\\adventofcode2020\\23\\Node.cpp"

using namespace std;

const int MOVES = 100;
const int CUPS = 9;

int main() {

    ifstream myfile("C:\\Users\\Excel PC\\Documents\\GitHub\\excelmm\\adventofcode2020\\23\\input.txt");
    std::map<int, Node*> nodes;
    std::string inputString;
    getline(myfile, inputString);

    // Initialise Linked List from input
    Node* ptrPrev = new Node();
    for (char iChar: inputString) {
        int i = iChar - '0';
        Node* ptrNew = new Node(i, NULL, NULL);
        if (ptrPrev->val) {
            ptrPrev->next = ptrNew;
        }
        nodes.insert(std::pair<int, Node*>(i, ptrNew));
        ptrPrev = ptrNew;
    }

    // Make Linked List circular
    Node* curr = nodes.at(inputString[0] - '0');
    ptrPrev->next = curr;

    // Start the game
    for (int i = 0; i < MOVES; ++i) {
        Node* cup1 = curr->next;
        Node* cup2 = cup1->next;
        Node* cup3 = cup2->next;
        curr->next = cup3->next;
        int cupValues[3] = {cup1->val, cup2->val, cup3->val};
        int destinationVal = curr->val - 1;
        if (destinationVal < 1) destinationVal = CUPS;
        while (std::find(cupValues, std::end(cupValues), destinationVal) != std::end(cupValues)) {
            --destinationVal;
            if (destinationVal < 1) destinationVal = CUPS;
        }
        Node* destination = nodes.at(destinationVal);
        cup3->next = destination->next;
        destination->next = cup1;
        
        curr = curr->next;
    }

    // Find "1" cup
    while (curr->val != 1) {
        curr = curr->next;
    }
    curr = curr->next;
    
    while (curr->val != 1) {
        cout << curr->val;
        curr = curr->next;
    }

    return 0;
}