function goingToHouseParty(inputArr) {
    let goingToParty = [];
    for (let el of inputArr) {
        let [name, secPart, thirdPart] = el.split(' ');
        if (thirdPart === 'going!') {
            if (goingToParty.includes(name)) {
                console.log(`${name} is already in the list!`);
            } else {
                goingToParty.push(name);
            }
        } else {
            if (goingToParty.includes(name)) {
                goingToParty.splice(goingToParty.indexOf(name), 1);
            } else {
                console.log(`${name} is not in the list!`);
            }
        }
    }
    console.log(goingToParty.join('\n'));
}

goingToHouseParty(['Allie is going!',
'George is going!',
'John is not going!',
'George is not going!']);