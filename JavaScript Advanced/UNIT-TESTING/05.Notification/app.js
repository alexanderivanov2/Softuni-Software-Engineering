function notify(message) {
    let divElementNotification = document.getElementById('notification');
    divElementNotification.textContent = message;
    divElementNotification.style.display = 'block'

    divElementNotification.addEventListener('click', () => {
        divElementNotification.style.display = 'none';
    })
}


// notify('This is a message');