function cardFactory(face, suite) {
    let validFaces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
    
    let suits = {
        S: '\u2660',
        H: '\u2665',
        D: '\u2666',
        C: '\u2663'
    };

    if (!validFaces.includes(face)) {
        throw new Error('Error');
    }

    let card = {};
    card['face'] = face;
    card['suite'] = suits[suite];
    card.toString = () => `${card.face}${card['suite']}`;
    
    return card.toString();
}

console.log(cardFactory('A', 'S'));
console.log(cardFactory('10', 'H'));
console.log(cardFactory('1', 'C'));