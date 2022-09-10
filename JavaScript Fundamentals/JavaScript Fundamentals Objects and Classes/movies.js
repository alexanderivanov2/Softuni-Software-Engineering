function movies(inputArr) {
    function createObj(name) {
        let obj = {
            name
        };

        return obj;
    }

    let exist = (x) => {
        for (let obj of arr) {
            if (obj.name === x){
                return obj;
            }
        }

        return false;
    }
    
    let arr = [];

    for (let el of inputArr) {
        let tokens = el.split(' ');
        if (tokens.includes('addMovie')) {
            tokens.shift()
            let name = tokens.join(' ');
            arr.push(createObj(name));
        } else {
            let index = 0;
            let propertyName = '';
            if (tokens.includes('directedBy')) {
                index = tokens.indexOf('directedBy');
                propertyName = 'director';
            } else {
                index = tokens.indexOf('onDate');
                propertyName = 'date';
            }
            let name = tokens.slice(0, index).join(' ');
            let secondData = tokens.slice(index + 1).join(' ');
    
            let obj = exist(name);
            if (obj) {
                obj[propertyName] = secondData;
            }
        }
    }

    for (let obj of arr) {
        
        if (obj.name && obj.director && obj.date) {
            console.log(JSON.stringify(obj));
        }
    }
}


movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'])