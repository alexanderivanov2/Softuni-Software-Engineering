function partyTime(arr) {
    let guests = [];
    let vip = [];
    let el = arr.shift();
    while (el !== 'PARTY') {
        if (isNaN(el.charAt(0))) {
            guests.push(el);
        } else {
            vip.push(el);
        }
        el = arr.shift();
    }

    while (arr.length > 0) {
        el = arr.shift();
        if (isNaN(el.charAt(0))) {
            guests.splice(guests.indexOf(el), 1);
        } else {
            vip.splice(vip.indexOf(el), 1);
        }
    }
    console.log(guests.length + vip.length);
    console.log(vip.join('\n'));
    console.log(guests.join('\n'));
}

partyTime(['7IK9Yo0h',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc',
'tSzE5t0p',
'PARTY',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc'
]);