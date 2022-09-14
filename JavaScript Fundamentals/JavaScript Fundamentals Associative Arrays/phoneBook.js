function phoneBook(arrNumbers) {
    let phoneBook = {};

    for (let el of arrNumbers) {
        [firstName, number] = el.split(' ');
        phoneBook[firstName] = number;
    }

    for (let key in phoneBook) {
        console.log(`${key} -> ${phoneBook[key]}`);
    }

}


phoneBook(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344']);