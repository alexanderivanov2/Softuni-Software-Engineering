function solve(input) {
    let patternNames = /[A-Za-z]+/g;
    let patternNumbers = /\d/g;
    let names = input.shift().split(', ');
    let obj = {}

    for (let name of names) {
        obj[name] = 0;
    }

    let txt = input.shift();

    while (txt != 'end of race'){
        let chars = txt.matchAll(patternNames);
        let nums = txt.matchAll(patternNumbers);
        let name = ''
        let km = 0;
        for (let el of chars) {
            name += el;
        }

        if (obj.hasOwnProperty(name)) {
            for(let n of nums) {
                km += Number(n);
            }
            obj[name] += km;
        }
        txt = input.shift();
    }

    let objSort = Object.entries(obj).sort((a, b) => b[1] - a[1]);
    console.log(`1st place: ${objSort[0][0]}`);
    console.log(`2nd place: ${objSort[1][0]}`);
    console.log(`3rd place: ${objSort[2][0]}`);

}

// solve(['George, Peter, Bill, Tom',
// 'G4e@55or%6g6!68e!!@ ',
// 'R1@!3a$y4456@',
// 'B5@i@#123ll',
// 'G@e54o$r6ge#',
// '7P%et^#e5346r',
// 'T$o553m&6',
// 'end of race'])

solve(['Ronald, Bill, Tom, Timmy, Maggie, Michonne',
'Mi*&^%$ch123o!#$%#nne787) ',
'%$$B(*&&)i89ll)*&) ',
'R**(on%^&ald992) ',
'T(*^^%immy77) ',
'Ma10**$#g0g0g0i0e',
'end of race']);