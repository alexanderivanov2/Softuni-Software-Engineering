function echoType(input){
    typeInput = typeof input;
    console.log(typeInput);
    if (typeInput === 'string' || typeInput === 'number'){
        console.log(input);
    } else {
        console.log('Parameter is not suitable for printing');
    }
}

echoType('AAA');
echoType(18);
echoType(null);