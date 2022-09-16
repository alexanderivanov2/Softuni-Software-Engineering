function solve(arr) {
    let password = arr[0].concat(arr[1]).toLowerCase();
    let third = arr[2]
    let vowels = ['a', 'e', 'o', 'u', 'i']
    let indexLenght = third.length;
    let index = 0;
    let reverseArr = [];

    for (let i = 0; i < password.length; i+=1) {
        if (vowels.includes(password[i].toLowerCase())){
            let letter = third[index].toUpperCase();
            index = index + 1 === indexLenght ? 0 : index + 1;
            reverseArr.unshift(letter);
        } else {
            reverseArr.unshift(password[i]);
        }
    }
    console.log(`Your generated password is ${reverseArr.join('')}`);
}

solve([
    'ilovepizza', 'ihatevegetables',
    'orange'
    ]);