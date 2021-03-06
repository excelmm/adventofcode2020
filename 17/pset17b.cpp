#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

const int SPACELIMIT = 31;
const int MIDDLE = floor(SPACELIMIT / 2);

int count_around(char[SPACELIMIT][SPACELIMIT][SPACELIMIT][SPACELIMIT], int, int, int, int);

int main() {
    
    char space[SPACELIMIT][SPACELIMIT][SPACELIMIT][SPACELIMIT];
    
    // Initialise space
    for (int a = 0; a < SPACELIMIT; ++a)
        for (int i = 0; i < SPACELIMIT; ++i)
            for (int j = 0; j < SPACELIMIT; ++j)
                for (int k = 0; k < SPACELIMIT; ++k)
                    space[a][i][j][k] = '.';

    // Place input into space
    std::vector<std::string> raw_input;
    ifstream myfile("input.txt");
    std::string line;
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            raw_input.push_back(line);
        }
        myfile.close();
    }

    int start_index = MIDDLE - floor(raw_input.size() / 2);
    
    for (int i = 0; i < raw_input.size(); ++i) 
        for (int j = 0; j < raw_input[i].length(); ++j) 
            space[MIDDLE][MIDDLE][i + start_index][j + start_index] = raw_input[i].at(j);

    // Start the game of life
    for (int iteration = 0; iteration < 6; ++iteration) {

        // Copy the space
        char space2[SPACELIMIT][SPACELIMIT][SPACELIMIT][SPACELIMIT];
        for (int a = 0; a < SPACELIMIT; ++a)
            for (int i = 0; i < SPACELIMIT; ++i) 
                for (int j = 0; j < SPACELIMIT; ++j)
                    for (int k = 0; k < SPACELIMIT; ++k)
                        space2[a][i][j][k] = space[a][i][j][k];

        for (int a = 0; a < SPACELIMIT; ++a) {
            for (int i = 0; i < SPACELIMIT; ++i) {
                for (int j = 0; j < SPACELIMIT; ++j) {
                    for (int k = 0; k < SPACELIMIT; ++k) {
                        if (space[a][i][j][k] == '#' && !(count_around(space2, a, i, j, k) == 2 || count_around(space2, a, i, j, k) == 3))
                            space[a][i][j][k] = '.';
                        if (space[a][i][j][k] == '.' && count_around(space2, a, i, j, k) == 3)
                            space[a][i][j][k] = '#';
                    }
                }
            }
        }
    }

    int count = 0;
    for (int a = 0; a < SPACELIMIT; ++a)
        for (int i = 0; i < SPACELIMIT; ++i) 
            for (int j = 0; j < SPACELIMIT; ++j)
                for (int k = 0; k < SPACELIMIT; ++k)
                    if (space[a][i][j][k] == '#')
                        ++count;
    cout << count << endl;

    return 0;
}

int count_around (char space[SPACELIMIT][SPACELIMIT][SPACELIMIT][SPACELIMIT], int superslice, int slice, int row, int col) {

    // Outer edges of space (not indeded to be reached)
    if (superslice == 0 || superslice == SPACELIMIT - 1 || slice == 0 || slice == SPACELIMIT - 1 || row == 0 || row == SPACELIMIT - 1 || col == 0 || col == SPACELIMIT - 1)
        return 0;
    
    int count = 0;
    for (int a = superslice - 1; a < superslice + 2; ++a)
        for (int i = slice - 1; i < slice + 2; ++i)
            for (int j = row - 1; j < row + 2; ++j)
                for (int k = col - 1; k < col + 2; ++k)
                    if (space[a][i][j][k] == '#')
                        ++count;
                
    if (space[superslice][slice][row][col] == '#')
        --count;

    return count;
}