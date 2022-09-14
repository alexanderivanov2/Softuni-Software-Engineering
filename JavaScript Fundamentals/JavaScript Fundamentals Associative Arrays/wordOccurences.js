function wordOccurences(arr) {
    let words = {};

    for (let word of arr) {
        if (words.hasOwnProperty(word)) {
            words[word] += 1;
        } else {
            words[word] = 1;
        }
    }

    let sorted = Object.entries(words).sort((a, b) => b[1] - a[1]);

    for (let key of sorted) {
        console.log(`${key[0]} -> ${key[1]} times`);
    }
}

wordOccurences(["Here", "is", "the", "first", "sentence", "Here", "is", "another", "sentence", "And", "finally", "the", "third", "sentence"]);