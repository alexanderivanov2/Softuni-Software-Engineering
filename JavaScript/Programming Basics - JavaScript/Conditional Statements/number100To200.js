function getPlaceOfTheNumber(input) {
    let num = input[0];
    if (num < 100) {
        console.log("Less than 100");
    } else if (num > 200) {
        console.log("Greater than 200");
    } else {
        console.log("Between 100 and 200");
    }
}

getPlaceOfTheNumber(["95"]);
getPlaceOfTheNumber(["120"]);
getPlaceOfTheNumber(["210"]);