function petShop(input){
    let numOfDogFood = Number(input[0]);
    let numOfCatFood = Number(input[1]);
    let totalSum = (numOfDogFood * 2.50) + (numOfCatFood * 4);
    console.log(`${totalSum} lv.`);
}
petShop(['5', '4'])