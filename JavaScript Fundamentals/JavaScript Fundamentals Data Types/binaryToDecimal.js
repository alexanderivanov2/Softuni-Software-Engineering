function binaryToDecimal(binaryN){
    let binary = String(binaryN);
    let decimal = parseInt(binary, 2);
    console.log(decimal);
}


binaryToDecimal("00001001");
binaryToDecimal(11110000);