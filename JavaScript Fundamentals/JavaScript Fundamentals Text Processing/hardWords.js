function solve(arr) {
    let text = arr[0];
    let textArr = text.split(' ');
    let words = arr[1];

    for  (let i = 0; i < textArr.length; i+= 1) {
        if (textArr[i][0] === '_') {
            let currentLength = textArr[i].length;
            let finalLength = textArr[i][currentLength - 1] !== '_' ? textArr[i].length - 1 : textArr[i].length;
            let addSign = finalLength < currentLength ? textArr[i][currentLength - 1] : '';
            textArr[i] = words.filter(x => x.length === finalLength)[0] + addSign;
        }
    }

    console.log(textArr.join(' '));
    
}

solve(['Hi, grandma! I\'m so ____ to write to you. ______ the winter vacation, so _______ things happened. My dad bought me a sled. Mom started a new job as a __________. My brother\'s ankle is ________, and now it bothers me even more. Every night Mom cooks ___ on your recipe because it is the most delicious. I hope this year Santa will _____ me a robot.',
['pie', 'bring', 'glad', 'During', 'amazing', 'pharmacist', 'sprained']]);