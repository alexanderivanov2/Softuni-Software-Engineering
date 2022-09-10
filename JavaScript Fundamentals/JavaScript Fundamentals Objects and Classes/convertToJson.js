function convertObjectToJson(firstName, lastName, hairColor) {
    let person = {
        name: firstName,
        lastName,
        hairColor
    }
    
    let jsonStr = JSON.stringify(person);
    console.log(jsonStr);
}

convertObjectToJson('George', 'Jones', 'Brown');