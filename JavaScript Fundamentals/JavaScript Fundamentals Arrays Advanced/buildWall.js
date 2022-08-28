function buildWall(input) {
    let cubicMeters = 0;
    let arrCubicMeters = [];
    let sections = input.map(Number);

    while (true) {
        let blocks = 0;
        for (let i = 0; i < sections.length; i++) {
            if (sections[i] < 30) {
                sections[i] += 1;
                blocks += 1;
            }
        }

        if (blocks === 0){
            break;
        }
        cubicMeters += blocks * 195;
        arrCubicMeters.push(blocks * 195);
    }
    console.log(arrCubicMeters.join(', '));
    console.log(`${cubicMeters * 1900} pesos`)
}

buildWall([21, 25, 28]);