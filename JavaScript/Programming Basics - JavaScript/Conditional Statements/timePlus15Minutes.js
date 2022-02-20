function add15Minutes (input) {
    let hour = Number(input[0]);
    let minutes = Number(input[1]);
    let allInMinutes = hour * 60 + minutes + 15;
    hour = Math.floor(allInMinutes / 60);
    if (hour === 24) {
        hour = 0;
    } 
    minutes = allInMinutes % 60;
    if (minutes < 10) {
        console.log(`${hour}:0${minutes}`);
    } else {
        console.log(`${hour}:${minutes}`);
    }
}

add15Minutes(["1", "46"]);
add15Minutes(["0", "01"]);
add15Minutes(["23", "59"]);
add15Minutes(["11", "08"]);
add15Minutes(["12", "49"]);