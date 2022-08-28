function manipulateArray(arr){
    let resultArr = arr.shift().split(' ').map(Number);
    for (let i = 0; i < arr.length; i++) {
        let [action, num, num2] = arr[i].split(' ');
        num = Number(num);
        
        if (action === 'Add') {
            resultArr.push(num);
        } else if (action === 'Remove') {
            while (resultArr.includes(num)) {
                let index = resultArr.indexOf(num);
                resultArr.splice(index, 1);
            }
        } else if (action === 'RemoveAt') {
            resultArr.splice(num, 1);
        } else if (action === 'Insert') {
            num2 = Number(num2)
            resultArr.splice(Number(num2), 0, num);
        }
    }
    console.log(resultArr.join(' '));
}


manipulateArray(['4 19 2 53 6 43',
'Add 3',
'Remove 2',
'RemoveAt 1',
'Insert 8 3'])
//result 4 53 6 8 43 3