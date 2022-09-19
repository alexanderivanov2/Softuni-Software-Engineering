function convertTextToUppercaseWords(txt) {
    let words = txt.match(/\w+/gm);
    words = words.map(word => word.toUpperCase());
    console.log(words.join(', '));
}

convertTextToUppercaseWords('Hi, how are.you?');