function getCharactersInRange(charOne, charTwo) {
    let getAsciiCode = x => x.charCodeAt(0);
    let startAscii = getAsciiCode(charOne) < getAsciiCode(charTwo)? getAsciiCode(charOne) : getAsciiCode(charTwo);
    let endAscii = String.fromCharCode(startAscii) === charOne ? getAsciiCode(charTwo) : getAsciiCode(charOne);
    let arr = [];

    for (let i = startAscii + 1; i < endAscii; i++) {
        arr.push(String.fromCharCode(i));
    }

    console.log(arr.join(' '))
}

getCharactersInRange("C",
    '#');