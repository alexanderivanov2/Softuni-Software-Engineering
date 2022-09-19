function calcStringsLength(strA, strB, strC) {
    let sumOfLengthStrings = strA.length + strB.length + strC.length;
    console.log(sumOfLengthStrings)
    console.log(Math.floor(sumOfLengthStrings / 3));
}

calcStringsLength('chocolate', 'ice cream', 'cake');