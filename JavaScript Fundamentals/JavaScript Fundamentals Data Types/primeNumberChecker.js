function isPrime(num) {
    if (num === 1){
        console.log(false);
    } else {
        let end = Math.trunc(Math.sqrt(num));
        for (let i = 2; i <= end; i++){
            if (num % i === 0) {
                console.log(false);
                return
            }
        }    
    }
    console.log(true);
}

isPrime(7);
isPrime(8);
isPrime(81);