function evenOddSubtraction(arrNumbers){
    let even = 0;
    let odd = 0;
    for (let num of arrNumbers){
        if (num % 2 === 0){
            even += num;
        } else {
            odd += num;
        }
    }
    console.log(even - odd);
}

evenOddSubtraction([1,2,3,4,5,6]);