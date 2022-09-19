function solve(num, a, b, c, d, e) {
    let result = num;
    let arr = [a, b, c, d, e];

    for (let el of arr) {
        if (el === 'chop') {
            result /= 2;
        } else if (el === 'dice') {
            result = Math.sqrt(result);
        } else if (el === 'spice'){
            result += 1;
        } else if (el === 'bake') {
            result *= 3;
        } else if (el === 'fillet') {
            result *= 0.80;
        }
        console.log(result);
    }
}


solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');