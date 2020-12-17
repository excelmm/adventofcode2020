const fs = require('fs');
const raw_input = fs.readFileSync('input.txt', {encoding: 'utf-8'}).split('\n\r').filter(x => x);
const eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'];

var answer = 0;
for (const line of raw_input) {
    var count = 0;
    const list = line.split(/\s+/g).filter(x => x);
    for (const field of list) {
        const matches = field.match('(\\w+):(.*)');
        const name = matches[1];
        const value = matches[2];
        switch (name) {
            case 'ecl': if (eyes.indexOf(value) != -1) ++count; break;
            case 'byr': if (Math.abs(parseInt(value) - 1961) <= 41) ++count; break;
            case 'iyr': if (Math.abs(parseInt(value) - 2015) <= 5) ++count; break;
            case 'eyr': if (Math.abs(parseInt(value) - 2025) <= 5) ++count; break;
            case 'hgt': if (value.split('cm').length == 2 && (parseInt(value.substring(0, value.length - 2)) >= 150 && parseInt(value.substring(0, value.length - 2)) <= 193)) ++count; 
                        else if (value.split('in').length == 2 && (parseInt(value.substring(0, value.length - 2)) >= 59 && parseInt(value.substring(0, value.length - 2)) <= 76)) ++count;
                        break;
            case 'hcl': if (value.match('#[a-f0-9]{6}')) ++count; break;
            case 'pid': if (value.match('^\\d{9}$')) ++count; break;
        }
    }
    if (count >= 7) ++answer;
}
console.log(answer);