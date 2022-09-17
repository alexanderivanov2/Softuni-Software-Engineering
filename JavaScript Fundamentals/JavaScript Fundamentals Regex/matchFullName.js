function solve(text) {
    let pattern = /\b[A-Z][a-z]+\s{1}[A-Z][a-z]+\b/g;
    let validNames = text.match(pattern);
    let arrNames = [];
    let match = pattern.exec(text);
    while (match!= null) {
        arrNames.push(match[0]);
        match = pattern.exec(text);
    }

    console.log(arrNames.join(' '));
    
}

solve("Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan	Ivanov");