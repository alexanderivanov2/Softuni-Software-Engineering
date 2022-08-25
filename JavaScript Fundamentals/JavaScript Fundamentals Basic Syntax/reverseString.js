function reverseString(input){
    let reverseWord = '';
    let word = input
    for (let i = word.length - 1; i >= 0; i--){
        reverseWord += word[i];
    }
    console.log(reverseWord);
}

reverseString('Hello');
reverseString('Softuni');
reverseString('1234');