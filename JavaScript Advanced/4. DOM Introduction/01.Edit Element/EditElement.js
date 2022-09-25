function editElement(elementReference, matchTxt, replacer) {
    let txt = elementReference.textContent;
    const matcher = new RegExp(matchTxt, 'g');
    elementReference.textContent = txt.replace(matcher, replacer);
}