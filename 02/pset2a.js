const fs = require('fs');
const file = fs.readFileSync('input.txt', 'utf-8');
const raw_input = file.split('\n').filter(x => x);

var count = 0;
for (const line of raw_input) {
    const matches = line.match('(\\d+)-(\\d+) (\\w): (.*)');
    const min = matches[1];
    const max = matches[2];
    const letter = matches[3];
    const pw = matches[4];
    const re = "/" + letter + "/g";
    if (pw.split(letter).length - 1 >= min && pw.split(letter).length - 1 <= max) count++;
}
console.log(count);