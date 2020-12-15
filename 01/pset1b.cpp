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
    
    bool found = false;
    for (int i = 0; i < input.size() - 1; ++i) {
        for (int j = i + 1; j < input.size(); ++j) {
            if (std::count(input.begin(), input.end(), 2020 - input[i] - input[j])){
                cout << input[i] * input[j] * (2020 - input[i] - input[j]) << endl;
                found = true;
                break;
            }
        }
        if (found == true) break;
    }
    
    return 0;
}