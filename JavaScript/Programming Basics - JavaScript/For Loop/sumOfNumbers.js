function sumDigitsOfString (input) {
    let txt = input[0];
    let sum = 0;
    for (let i = 0; i < txt.length; i++){
        sum += Number(txt[i]);
    }
    console.log(`The sum of the digits is:${sum}`)
}

sumDigitsOfString(['1234567897777'])