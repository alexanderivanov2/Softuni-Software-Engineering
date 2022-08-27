function signCheck(a, b, c ){
    let isPositive = x => x < 0 ? 0 : 1;
    let isNegative = x => x < 0 ? 1 : 0;
    let positive = isPositive(a) + isPositive(b) + isPositive(c);
    let negative = isNegative(a) + isNegative(b) + isNegative(c);
    let result;

    if (positive === 2 || negative === 3 || negative === 1) {
        result = 'Negative'
    } else if (negative === 2 || positive === 3) {
        result = 'Positive';
    } 
    console.log(result);
}


signCheck(5,
    12,
   -15);

signCheck(-6,
    -12,
     14);

signCheck(-1,
    -2,
    -3);

signCheck(-5,
    1,
    1);