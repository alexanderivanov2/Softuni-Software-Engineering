function getRounding(num1, num2) {
    let num = num1;
    let signsRounded = num2 > 15 ? 15: num2;
    console.log(parseFloat(num1.toFixed(signsRounded)));
}


getRounding(3.1415926535897932384626433832795,2);
getRounding(10.5,3);