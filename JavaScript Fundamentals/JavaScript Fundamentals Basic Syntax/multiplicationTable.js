function multiplicationTable(inputN) {
    let num = inputN;
    for (let i=1; i <= 10; i++) {
        console.log(`${num} X ${i} = ${num * i}`);
    }
}

multiplicationTable(5);