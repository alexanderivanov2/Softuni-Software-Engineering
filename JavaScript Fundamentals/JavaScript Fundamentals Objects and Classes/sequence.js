function sequence(input) {
    input = input.map(el => JSON.parse(el));
    input.forEach(el => el.sort((a, b) => b - a));
    let unique = [];

    for (let i = 0; i < input.length; i++) {
        let currentArray = input[i];
        let isUnique = true;
        for (let j = 0; j < unique.length; j++) {
            let uniqueArr = unique[j];
            if (currentArray.toString() === uniqueArr.toString()) {
                isUnique = false;
                break;
            } 
        }

        if (isUnique) {
            unique.push(currentArray);
        }
    }
        
    unique.sort((a, b) => a.length - b.length);
    unique.forEach(el => console.log(`[${el.join(', ')}]`));
}


sequence(["[-3, -2, -1, 0, 1, 2, 3, 4]",
"[10, 1, -17, 0, 2, 13]",
"[4, -3, 3, -2, 2, -1, 1, 0]"]);