function rightPlace(wordOne, char, wordTwo){
    let wordOneReplace = '';
    for (let i = 0; i < wordOne.length; i++){
        if (wordOne[i] === '_'){
            wordOneReplace += char;
        } else {
            wordOneReplace += wordOne[i];
        }
    }
    if (wordOneReplace === wordTwo){
        console.log('Matched');
    } else {
        console.log('Not Matched');
    }
}


rightPlace('Str_ng', 'I', 'Strong');