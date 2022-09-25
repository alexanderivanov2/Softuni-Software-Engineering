function extractText() {
    let liItems = document.querySelectorAll('li');
    let textareaElement = document.getElementById('result')
    for (let liItem of liItems) {
        textareaElement.textContent += liItem.textContent + '\n';
    }
}