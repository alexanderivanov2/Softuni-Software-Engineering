function convertor(input){
    let radian = Number(input[0]);
    let convertToDegrees = radian * 180 / Math.PI;
    console.log(convertToDegrees);
}
convertor(['3.1416']);