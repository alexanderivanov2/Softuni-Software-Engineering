function solve(input) {
    let arr = input.split(/[,\s]+/g);
    let patternHP = /[^0-9+\-\*\/\.]/g;
    let patternDMG = /(-?\d+(?:\.\d+)?)/g;
    let patternOperators = /[\*\/]/g;
    let obj = {};

    for (let el of arr) {
        let health = 0;
        let damage = 0;
        let hp = el.match(patternHP);
        let dmg = el.match(patternDMG);
        let operators = el.match(patternOperators);

        if (hp !== null) {
            for (let h of hp) {
                health += h.charCodeAt(0);
            }
        }

        if (dmg !== null) {
            for (let d of dmg) {    
                d = Number(d);
                damage += d;
            }
            if (operators !== null) {
                for (let o of operators) {
                    if (o == '*') {
                        damage *= 2;
                    } else {
                        damage /= 2;
                    }
                }
            }
        }
    
        obj[el] = `${el} - ${health} health, ${damage.toFixed(2)} damage`;
    
    }

    sortObj = Object.entries(obj).sort((a, b) => a[0].localeCompare(b[0]));

    for (el of sortObj) {
        console.log(el[1]);
    }
}

solve('M3ph-0.5s-0.5t0.0**')
solve('M3ph1st0**, Azazel');
solve('Gos/ho')