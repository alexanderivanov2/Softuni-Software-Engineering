function searchForANumber(arr, arrSettings) {
    let arrLength = arrSettings.shift();
    let arrDelete = arrSettings.shift();
    let arrSearchEl = arrSettings.shift();
    let resultArr = arr.slice(0, arrLength);
    resultArr.splice(0, arrDelete);
    resultArr = resultArr.filter(x => x === arrSearchEl);
    console.log(`Number ${arrSearchEl} occurs ${resultArr.length} times.`);
}

searchForANumber([7, 1, 5, 8, 2, 7],
    [3, 1, 5]);