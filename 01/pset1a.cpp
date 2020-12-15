#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    std::vector<int> input;

    ifstream myfile("input.txt");
    string line;
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            input.push_back(stoi(line));
        }
        myfile.close();
    }
    else cout << "Unable to open file";
    
    for (int i: input) {
        if (std::count(input.begin(), input.end(), 2020 - i)){
            cout << i * (2020 - i) << endl;
            break;
        }
    }
    
    return 0;
}