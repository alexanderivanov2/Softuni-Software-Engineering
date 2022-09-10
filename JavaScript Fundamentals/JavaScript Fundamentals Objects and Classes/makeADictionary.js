function makeDictionary(inputArr) {
    let dictionary = {};

    for (el of inputArr) {
        let elObj = JSON.parse(el);
        for (let key of Object.keys(elObj)){
            dictionary[key] = elObj[key];
        }
    }

    dictionaryKeys = Object.keys(dictionary);
    dictionaryKeys.sort((a, b) => a.localeCompare(b));
    for (let key of dictionaryKeys) {
        console.log(`Term: ${key} => Definition: ${dictionary[key]}`);
    }
}


makeDictionary([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]);