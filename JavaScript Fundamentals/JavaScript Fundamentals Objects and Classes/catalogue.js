function catalogue(inputArr) {
    inputArr.sort((a, b) => a.localeCompare(b));
    let capitalLetter = [];
    inputArr.map((a) => {
        if(a[0] !== capitalLetter[capitalLetter.length - 1]) {
            capitalLetter.push(a[0]);
        }
    })

    let index = 0;

    for (let capitalLetterChar of capitalLetter) {
        console.log(capitalLetterChar);
    
        while (index < inputArr.length && inputArr[index][0] === capitalLetterChar){
            let info = inputArr[index].split(' : ').join(': ');
            console.log(`  ${info}`);
            index += 1;
        }
    }
}


catalogue([
    'Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
    ]
    );