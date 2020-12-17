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
    if ((pw.charAt(min - 1) == letter && pw.charAt(max - 1) != letter) || (pw.charAt(min - 1) != letter && pw.charAt(max - 1) == letter)) count++;
}
console.log(count);