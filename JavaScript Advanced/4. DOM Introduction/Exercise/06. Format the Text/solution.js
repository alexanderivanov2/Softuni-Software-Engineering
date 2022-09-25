function solve() {
  let textareaElement = document.getElementById('input').value;
  let arrayOfSentence = textareaElement
  .split('.')
  .filter(sentence => sentence.length > 1);
  console.log(arrayOfSentence)
  let outputElement = document.getElementById('output');
  let paragraph = '<p>'
  let countSentence = 0;
    
  while (arrayOfSentence.length > 0) {
    paragraph += arrayOfSentence.shift() + '.';
    countSentence += 1;
    if (countSentence == 3 || arrayOfSentence.length == 0) {
      paragraph += '</p>';
      outputElement.innerHTML += paragraph;
      paragraph = '<p>';
      countSentence = 0;
    }
  }
}