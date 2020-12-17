const fs = require('fs');
const { exit } = require('process');
const file = fs.readFileSync('input.txt', 'utf-8');
const raw_input = file.split('\n').map(str => Number(str));

const set = new Set(raw_input);
for (const number of raw_input) {
    for (const number2 of raw_input) {
        if (set.has(2020 - number - number2)) {
            console.log(number * number2 * (2020 - number - number2));
            exit();
        }
    }
}