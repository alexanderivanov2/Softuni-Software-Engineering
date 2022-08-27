function isPalindrome(arrNums) {
    let readNumBackwards = x => {
        let result = '';

        for (let i = x.length - 1; i >= 0; i--) {
            result += x[i];
        }

        return Number(result);
    }

    for (let num of arrNums) {
        let backwardNum = readNumBackwards(String(num));
        console.log(num === backwardNum)
    }
}

isPalindrome([123,323,421,121]);