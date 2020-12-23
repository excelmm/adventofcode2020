#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <iterator>
#include "Node.cpp"

using namespace std;

const int MOVES = 10000000;
const int CUPS = 1000000;

int main() {

    ifstream myfile("input.txt");
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

    // Add the rest of the numbers from 1 - CUPS to the Linked List
    for (int i = inputString.length() + 1; i <= CUPS; ++i) {
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
            int destinationVal = curr->val - 1;
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
    
    cout << (long long) curr->next->val * (long long) curr->next->next->val << endl;

    return 0;
}