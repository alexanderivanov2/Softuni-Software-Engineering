function sortNegativeAndPositiveNumbers(arr) {
    let negativePositiveSortArr = [];
    for (let el of arr) {
        el = Number(el);
        if (el < 0) {
            negativePositiveSortArr.unshift(el);
        } else {
            negativePositiveSortArr.push(el);
        }
    }
    console.log(negativePositiveSortArr.join('\n'));
}


sortNegativeAndPositiveNumbers(['7', '-2', '8', '9']);