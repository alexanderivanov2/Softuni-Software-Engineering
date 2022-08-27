function power(n, x){
    let result = 1;
    
    for (let i = 1; i <= x; i++){
        result *= n;
    }

    console.log(result);
}

power(2, 8);
power(3, 4);
power(12, 2);