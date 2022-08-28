function sortingBy2Criteria(arr) {
    arr.sort((a, b) => {
        let result = a.length - b.length;
        if (result === 0 ){
            result = a.localeCompare(b);
        }
        return result;
    });
    console.log(arr.join('\n'));
}

// sortingBy2Criteria(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George'])
sortingBy2Criteria(['Deny', 'omen', 'test', 'Default']);