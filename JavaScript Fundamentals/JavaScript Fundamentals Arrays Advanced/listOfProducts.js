function getOrderedListOfProducts(arr) {
    console.log(arr
        .sort()
        .map((el, i) => `${i + 1}.${el}`)
        .join('\n')
        );
}

getOrderedListOfProducts(['Potatoes', 'Tomatoes', 'Onions', 'Apples']);