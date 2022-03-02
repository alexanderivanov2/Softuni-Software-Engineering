function building(input){
    let floors = Number(input[0]);
    let rooms = Number(input[1]);
    for (let f = floors; f >= 1; f--){
        let allRooms = '';
        for (let r = 0; r < rooms; r++){
            if (f===floors){
                allRooms += `L${f}${r} `;
            } else if (f % 2 === 0){
                allRooms += `O${f}${r} `;
            } else if(f % 2 !== 0){
                allRooms += `A${f}${r} `;
            }
        }
        console.log(allRooms);
    }
}

building(["6", "4"]);