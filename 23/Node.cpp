#include <iostream>
#include <fstream>

using namespace std;

class Node {
    public:
        int val = 0;
        Node* next = NULL;

        Node() {}

        Node(int val, Node* ptrprev, Node* ptrnext) {
            this->val = val;
            this->next = ptrnext;
        }
};