function addAndRemoveElements(arr) {
    let numArr = [];
    let n = 1;
    for (let el of arr) {
        if (el === 'add') {
            numArr.push(n);
        } else {
            numArr.pop();
        }
        n += 1;
    }
    
    let result = numArr.length > 0 ? numArr.join('\n') : 'Empty';
    console.log(result);
}


addAndRemoveElements(['add', 
'add', 
'add', 
'add']);
addAndRemoveElements(['add', 
'add', 
'remove', 
'add', 
'add']);
addAndRemoveElements(['remove', 
'remove', 
'remove']);