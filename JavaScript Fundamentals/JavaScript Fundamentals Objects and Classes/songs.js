function songs(input) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList,
            this.name = name,
            this.time = time
        }
    }
    let n = Number(input.shift());
    let arr = [];

    for (let i = 0; i < n; i++) {
        let [typeList, name, time] = input[i].split('_');
        arr.push(new Song(typeList, name, time));
    }
    
    let checkTypeList = input.pop();

    for (let obj of arr) {
        if (obj.typeList === checkTypeList || checkTypeList === "all") {
            console.log(obj.name);
        }
    }
}


songs([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite'])