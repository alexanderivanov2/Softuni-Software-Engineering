function solve(input) {
    let nOfMessage = Number(input.shift())
    let patternStar = /[star]/gi;
    let patternPlanet = /@(?<name>[A-Za-z]+)[^@\-!:>]*:(?<population>\d+)[^@\-!:>]*!(?<action>[A|D])![^@\-!:>]*->(?<soldiers>\d+)/;

    let attacked = [];
    let destroyed = [];

    for (let i = 0; i < nOfMessage; i++) {
        let text = input[i];      
        let match = text.match(patternStar);
        
        if (match !== null) {
            let decrypt = '';
            for (let ch of text) {
                decrypt += String.fromCharCode(ch.charCodeAt(0) - match.length);
            }
            text = decrypt;
        }

        let isValid = patternPlanet.test(text);

        if (isValid){
            let final = patternPlanet.exec(text);
            let {name, action} = final.groups;

            if (action === 'A') {
                attacked.push(name);
            } else {
                destroyed.push(name);
            }
        }
        
    }
    
    if (attacked.length > 0) {
        attacked.sort((a, b) => a.localeCompare(b));
    }

    if (destroyed.length > 0) {
        destroyed.sort((a, b) => a.localeCompare(b));
    }


    console.log(`Attacked planets: ${attacked.length}`);
    for (let p of attacked) {
        console.log(`-> ${p}`)
    }

    console.log(`Destroyed planets: ${destroyed.length}`)
    for (let p2 of destroyed) {
        console.log(`-> ${p2}`);
    }

}

// solve(['2',
// 'STCDoghudd4=63333$D$0A53333',
// 'EHfsytsnhf?8555&I&2C9555SR']);

solve(['3',
"tt(''DGsvywgerx>6444444444%H%1B9444",
'GQhrr|A977777(H(TTTT',

'EHfsytsnhf?8555&I&2C9555SR']);