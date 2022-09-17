function solve(numbers) {
    let pattern = /\+359( 2 [0-9]{3} [0-9]{4}|-2-[0-9]{3}-[0-9]{4})\b/g;
    let phones = [];
    let match = pattern.exec(numbers);
    
    while(match != null) {
        phones.push(match[0]);
        match = pattern.exec(numbers);
    }
    console.log(phones.join(', '));
}

solve("+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222");