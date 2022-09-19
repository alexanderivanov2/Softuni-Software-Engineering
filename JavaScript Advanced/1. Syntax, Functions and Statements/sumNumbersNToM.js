function sumNumbersFromNToM(start, end) {
    start = Number(start);
    end = Number(end);
    let sum = 0;

    for (let i = start; i <= end; i++) {
        sum += i;
    }

    return sum;
}

console.log(sumNumbersFromNToM('1', '5'));
console.log(sumNumbersFromNToM('-8', '20'));