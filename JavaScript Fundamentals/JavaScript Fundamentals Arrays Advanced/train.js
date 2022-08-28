function fillTheTrain(inputArr) {
    let arr = inputArr
    .shift()
    .split(' ')
    .map(Number);
    let maxCapacity = Number(inputArr.shift());
    for (let el of inputArr) {
        if (el.includes('Add')) {
            let [action, num] = el.split(' ');
            num = Number(num);
            arr.push(num);
        } else {
            el = Number(el)
            for (let i = 0; i < arr.length; i++) {
                if (arr[i] + el <= maxCapacity) {
                    arr[i] += el;
                    break;
                }
            }
        }
    }
    console.log(arr.join(' '));
}


fillTheTrain(['32 54 21 12 4 0 23',
'75',
'Add 10',
'Add 0',
'30',
'10',
'75'])