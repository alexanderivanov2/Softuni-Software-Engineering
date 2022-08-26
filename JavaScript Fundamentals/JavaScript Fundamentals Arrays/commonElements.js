function commonElements(arrOne, arrTwo){
    for (let el of arrOne){
        if (arrTwo.includes(el)){
            console.log(el);
        }
    }
}

commonElements(['Hey', 'hello', 2, 4, 'Peter', 'e'],
['Petar', 10, 'hey', 4, 'hello', '2']);