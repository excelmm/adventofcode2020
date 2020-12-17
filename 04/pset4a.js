const fs = require('fs');
const raw_input = fs.readFileSync('input.txt', {encoding: 'utf-8'}).split('\n\r').filter(x => x);
const required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];

var answer = 0;
for (const line of raw_input) {
    var count = 0;
    const list = line.split(/\s+/g).filter(x => x);
    for (const field of list) {
        const matches = field.match('(\\w+):(.*)');
        const name = matches[1];
        if (required.indexOf(name) != -1) ++count;
    }
    if (count >= 7) ++answer;
}
console.log(answer);