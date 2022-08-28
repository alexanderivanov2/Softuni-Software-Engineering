function arrayManipulator(arr, input) {
    for (let el of input){
        let tokens = el.split(' ');

        if (tokens[0] === 'add') {
            let index = Number(tokens[1]);
            let element = Number(tokens[2]);
            arr.splice(index, 0, element);
        } else if (tokens[0] === "addMany") {
            let index = Number(tokens[1]);
            let nums = tokens.slice(2).map(Number);
            for (let n of nums) {
                arr.splice(index, 0, n);
                index += 1;
                 
            }
        } else if (tokens[0] === 'contains') {
            let element = Number(tokens[1]);
            console.log(arr.indexOf(element));
        } else if (tokens[0] === 'remove') {
            let index = Number(tokens[1]);
            arr.splice(index, 1);
        } else if (tokens[0] === 'shift') {
            let indexPosition = Number(tokens[1]);
            for (let j = 0; j < indexPosition; j++){
                arr.push(arr.shift());
            }
        } else if (tokens[0] === 'sumPairs') {
            let sumArr = [];
            for (let i = 0; i < arr.length; i += 2){
                if (i === arr.length - 1) {
                    sumArr.push(arr[i]);
                } else {
                    sumArr.push(arr[i] + arr[i + 1]);
                }
            }
            arr = sumArr;
        } else if (tokens[0] === 'print') {
            console.log(`[ ${arr.join(', ')} ]`);
            return;
        }
    }
}
// [ 2, 3, 5, 9, 8, 7, 6, 5, 1 ]
arrayManipulator([1, 2, 3, 4, 5], 
    ["addMany 5 9 8 7 6 5", "contains 15", "remove 3", "shift 1", "print"])

arrayManipulator([1, 2, 4, 5, 6, 7],
    ['add 1 8', 'contains 1', 'contains 3', 'print']);

arrayManipulator([1, 2, 3, 4, 5], ['shift 2', 'print']);

arrayManipulator([1, 2, 4, 5, 6, 7, 8], ['sumPairs', 'print'])