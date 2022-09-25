function toggle() {
    let spanElement = document.getElementsByClassName('button')[0];
    let spanElementText = spanElement.textContent;
    let divElementExtra = document.getElementById('extra');

    if (spanElementText === 'More') {
        spanElement.textContent = 'Less';
        divElementExtra.style.display = "block";
    } else {
        spanElement.textContent = 'More';
        divElementExtra.style.display = 'none';
    }
}