function towns(inputArr) {
    function createObj(town, latitude, longitude) {
        let obj = {
            town,
            latitude: latitude.toFixed(2),
            longitude: longitude.toFixed(2)
        }
        
        return obj;
    }

    let arr = [];

    for (let el of inputArr) {
        let [town, latitude, longitude] = el.split(' | ');
        latitude = Number(latitude);
        longitude = Number(longitude);

        arr.push(createObj(town, latitude, longitude));
    }

    for (let obj of arr) {
        console.log(obj);
    }

}


towns(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']);