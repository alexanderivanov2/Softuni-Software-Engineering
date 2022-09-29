function printDeckOfCards(cards) {
    let arrOfCards = cards;
    function createCard() {
        let createdCards = [] 

        for (let c of arrOfCards) {
            let currentCard = c.split('');
            let suite = currentCard.pop();
            let face = currentCard.join('');

            let validFaces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
    
            let suits = {
            S: '\u2660',
            H: '\u2665',
            D: '\u2666',
            C: '\u2663'
            };
    
            if (!validFaces.includes(face) || !suits[suite]) {
                return `Invalid card: ${c}`
            }
    
            createdCards.push(`${face}${suits[suite]}`);   
        }
        return createdCards.join(' ');
    }

    let createdCards = createCard()

    console.log(createdCards);
}

printDeckOfCards(['AS', '10D', 'KH', '2C']);
printDeckOfCards(['5S', '3D', 'QD', '1C']);