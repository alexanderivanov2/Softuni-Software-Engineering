function extract(content) {
    let regEx = /\(([^)]+)\)/gm;
    let regEx2 = /[^\(\)]+/gm;
    let pElement = document.getElementById(content);
    console.log(pElement.textContent);
   
    let matches = pElement.textContent.match(regEx);
    console.log(matches);
    matchesResult = matches.map(x => x.match(regEx2))
    return matchesResult.join('; ') 
}