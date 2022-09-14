function oddOccurrences(input) {
    let obj = {};
    let [...arr] = input.split(' ');

    for (let el of arr) {
        el = el.toLowerCase(); 
        if (obj.hasOwnProperty(el)) {
            obj[el] += 1;
        } else {
            obj[el] = 1;
        }
    }
    
    let result = ''
    for (let key in obj) {
        if (obj[key] % 2 != 0){
            result += key + ' ';
        }
    }
    console.log(result);
}


oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');