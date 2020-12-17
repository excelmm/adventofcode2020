const fs = require('fs');
const raw_input = fs.readFileSync('input.txt', {encoding: 'utf-8'}).split("\n").filter(x => x);
const lines = [];
const required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];

var input = '';
for (const line of raw_input) {
    if (line == '\r') {
        lines.push(input);
        input = '';
        continue;
    }
    input += line;
}
lines.push(input);

var count = 0;
for (const line of lines) {
    var i = 0;
    for (const item of required)
        if (line.split(item).length - 1) ++i;
    if (i >= 7) ++count;
}
console.log(count);