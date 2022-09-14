function companyUsers(arr) {
    let obj = {};

    for (let el of arr) {
        let [company, user] = el.split(' -> ');
        if (obj.hasOwnProperty(company)) {
            if (obj[company].includes(user) === false) {
                obj[company].push(user)
            }
        } else  {
            obj[company] = [user];
        }
    }

    let sortObj = Object.keys(obj).sort((a, b) => a.localeCompare(b));

    for (let key of sortObj) {
        console.log(key);
        for (let el of obj[key]) {
            console.log(`-- ${el}`);
        }
    }

}

companyUsers([
    'SoftUni -> AA12345',
    'SoftUni -> BB12345',
    'Microsoft -> CC12345',
    'HP -> BB12345',
    'SoftUni -> AA12345',
    'SoftUni -> BB12345',
    'Microsoft -> CC12345',
    'HP -> BB12345'
    ]);