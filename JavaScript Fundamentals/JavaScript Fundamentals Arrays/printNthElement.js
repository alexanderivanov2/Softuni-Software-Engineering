function printNthElemnet(arr) {
    let newArr = arr.slice(0, arr.length - 1);
    let step = Number(arr[arr.length - 1]);
    let stepArr = [];
    for (let i = 0; i < newArr.length; i += step){
        stepArr.push(newArr[i]);
    }
    console.log(stepArr.join(' '));
}

printNthElemnet(['5', '20', '31', '4', '20', '2']);