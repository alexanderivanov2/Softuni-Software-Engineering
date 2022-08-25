function intOrFloat(n1, n2, n3) {
    let result = n1 + n2 + n3;
    let result2 = result % 1 === 0? 'Integer': 'Float';
    console.log(`${result} - ${result2}`)
}


intOrFloat(9, 100, 1.1);
intOrFloat(100, 200, 303);