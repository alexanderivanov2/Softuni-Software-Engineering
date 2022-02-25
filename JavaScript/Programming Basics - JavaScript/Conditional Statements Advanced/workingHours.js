function openOrClosed (input) {
    let hour = Number(input[0]);
    let day = input[1];
    if (day != 'Sunday' && 18 >= hour && hour >= 10){
        console.log('open');
    } else {
        console.log('closed');
    }
}