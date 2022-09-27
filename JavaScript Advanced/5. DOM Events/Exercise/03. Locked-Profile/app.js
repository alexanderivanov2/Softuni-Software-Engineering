function lockedProfile() {
    let buttonElements = document.querySelectorAll('button');
    buttonElements = Array.from(buttonElements);

    buttonElements.forEach(btn => {
        btn.addEventListener('click', (e) => {
            let parent = btn.parentNode;
            let parentInputElement = parent.querySelector('input[type="radio"]:checked');
            let divPreviousSiblingElement = btn.previousElementSibling;

            // Logic For Unlock
            if (parentInputElement.value == 'unlock') {
                if (btn.textContent == 'Show more') {
                    divPreviousSiblingElement.style.display = 'block';
                    btn.textContent = 'Hide it';
                } else {
                    divPreviousSiblingElement.style.display = 'none';
                    btn.textContent = 'Show more';
                }
            }
        });
    });
}