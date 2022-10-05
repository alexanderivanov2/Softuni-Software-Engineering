function solution() {
    const inputGiftName = document.querySelector('input');
    const ulListOfGifts = document.querySelector('section.card:nth-child(2) ul');
    const ulSentGifts = document.querySelector('.card:nth-child(3) ul');
    const ulDiscardedGifts = document.querySelector('.card:nth-child(4) ul');
    const buttonAddGift = document.querySelector('button');

    buttonAddGift.addEventListener('click', addGift);

    function addGift(e) {
    
    
        if (inputGiftName.value) {
            const liElement = createElement('li', ulListOfGifts, inputGiftName.value, ['class', 'gift']);
            const buttonSend = createElement('button', liElement, 'Send', ['id', 'sendButton']);
            const buttonDiscard = createElement('button', liElement, 'Discard', ['id', 'discardButton']);
            buttonSend.addEventListener('click', sendGift);
            buttonDiscard.addEventListener('click', discardGift);

            inputGiftName.value = '';

            Array.from(ulListOfGifts.querySelectorAll('.gift')).sort((a, b) => a.textContent.localeCompare(b.textContent))
            .forEach(liElement => ulListOfGifts.appendChild(liElement));
        }
    }
    
    function sendGift(e) {
        const parent = e.currentTarget.parentNode;
        const sibblingButton = e.currentTarget.nextSibling;
        sibblingButton.remove();
        e.currentTarget.remove();
        ulSentGifts.appendChild(parent);
    }
    
    function discardGift(e) {
        const parent = e.currentTarget.parentNode;
        const sibblingButton = e.currentTarget.previousSibling;
        sibblingButton.remove();
        e.currentTarget.remove();
        ulDiscardedGifts.appendChild(parent);
    }
    
    function createElement(type, parent, content='', attributes=[]) {
        const element = document.createElement(type);
        element.textContent = content;
        parent.appendChild(element);
    
        for (let i = 0; i < attributes.length; i += 2) {
            element.setAttribute(attributes[i], attributes[i + 1]);
        }
    
        return element;
    }
}