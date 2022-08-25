function triplesLetters(num) {
    let a = '';
    let b = '';
    let c = '';
    let n = Number(num);
    for (let i = 0; i < n; i++){
        a += String.fromCharCode(97 + i);
        for (let j = 0; j < n; j++){
            b += String.fromCharCode(97 + j);
            for (let k = 0; k < n; k++){
                c += String.fromCharCode(97 + k);
                console.log(`${a}${b}${c}`);
                c = '';
            }
            b = '';
        }
        a = '';
    }
}

triplesLetters('2')