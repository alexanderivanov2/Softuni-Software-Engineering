function solution() {
    let inputElement = document.querySelector('.card:nth-child(1) input');
    let listOfGiftsUlElement = document.querySelector('.card:nth-child(2) ul');
    let sentGiftsUlElement = document.querySelector('.card:nth-child(3) ul');
    let discardedGiftsUlElement = document.querySelector('.card:nth-child(4) ul');

    let btnAddGift = document.querySelector('.card:nth-child(1) button');
    
    btnAddGift.addEventListener('click', (e) => {
        // Validate input
        if (inputElement.value.trim()) {
            let liElement = document.createElement('li');
            liElement.classList.add('gift');
            liElement.textContent = inputElement.value;

            let btnSend = document.createElement('button');
            btnSend.id = 'sendButton';
            btnSend.textContent = 'Send';

            let btnDiscard = document.createElement('button');
            btnDiscard.id = 'discardButton';
            btnDiscard.textContent = 'Discard';

            btnSend.addEventListener('click', sendGift);
            btnDiscard.addEventListener('click', discardGift);

            liElement.appendChild(btnSend);
            liElement.appendChild(btnDiscard);
            listOfGiftsUlElement.appendChild(liElement);
            sortLiElements();
        }
        let sections = document.querySelectorAll('section');
        console.log(sections);
        let listOfGifts = sections[1].children[1].children;
        console.log(listOfGifts);
        console.log(listOfGifts.length);
        console.log('txtCont' + listOfGifts[0].textContent);
        // // Clean Input
        
        inputElement.value = '';
    });

    function sendGift(e) {
        let parent = e.currentTarget.parentNode;
        let siblingBtn = e.currentTarget.nextSibling;
        siblingBtn.remove();
        e.currentTarget.remove();
        sentGiftsUlElement.appendChild(parent);
    }

    function discardGift(e) {
        let parent = e.currentTarget.parentNode;
        let siblingBtn = e.currentTarget.previousSibling;
        siblingBtn.remove();
        e.currentTarget.remove();
        discardedGiftsUlElement.appendChild(parent);
    }

    function sortLiElements() {
        Array.from(listOfGiftsUlElement.querySelectorAll('li'))
            .sort((a, b) => a.textContent.localeCompare(b.textContent))
            .forEach(item => listOfGiftsUlElement.appendChild(item));
    }
}