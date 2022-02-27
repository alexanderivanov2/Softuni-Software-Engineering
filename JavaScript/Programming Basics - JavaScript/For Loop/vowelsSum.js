function calculateSumOfVowels (input) {
    let word = input[0];
    let sum = 0;
    for (i = 0; i < word.length; i++) {
        switch(word[i]){
            case 'a': sum += 1; break;
            case 'e': sum += 2; break;
            case 'i': sum += 3; break;
            case 'o': sum += 4; break;
            case 'u': sum += 5; break;
            default: sum += 0; break;
        }
    }
    console.log(sum);
}

calculateSumOfVowels(['hello']);