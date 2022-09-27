function encodeAndDecodeMessages() {
    let buttonElements = document.querySelectorAll('button');
    buttonElements = Array.from(buttonElements);
    let textareaElements = document.querySelectorAll('textarea');
    let textareaEncode = textareaElements[0];
    let textareaDecode = textareaElements[1];

    buttonElements.forEach(btn => {

        btn.addEventListener('click', (e) => {
            let btnTextContent = btn.textContent;
            let text = '';

            if (btnTextContent[0] == 'E') {
                for (let char of textareaEncode.value){
                    text += String.fromCharCode(char.charCodeAt(0) + 1);
                }
                textareaDecode.value = text;
                textareaEncode.value = ''
            } else {
                for (let char of textareaDecode.value) {
                    text += String.fromCharCode(char.charCodeAt(0) - 1);
                }
                textareaDecode.value = text;
            }

        });
    });
}