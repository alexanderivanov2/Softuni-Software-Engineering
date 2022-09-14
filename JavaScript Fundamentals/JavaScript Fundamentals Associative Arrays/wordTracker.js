function wordTracker(input){
    let [...objParts] = input.shift().split(' ');
    let obj = {};

    for (let el of objParts) {
        obj[el] = 0;
    }

    for (let el of input) {
        if (obj.hasOwnProperty(el)){
            obj[el] += 1;
        }
    }

    let sortObj = Object.entries(obj).sort((a, b) => b[1] - a[1]);
    
    for (let [key, value] of sortObj) {
        console.log(`${key} - ${value}`);
    }
}


wordTracker([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurances', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]);