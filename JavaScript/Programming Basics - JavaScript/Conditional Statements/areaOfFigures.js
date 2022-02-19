function getArea(input) {
    let figure = input[0];
    let sideA = Number(input[1]);
    let area = undefined;
    if (figure === 'square') {
        area = sideA * sideA;
    } else if(figure === 'rectangle') {
        let sideB = Number(input[2]);
        area = sideA * sideB;
    } else if (figure === 'circle') {
        area = Math.PI  * Math.pow(sideA, 2);
    } else if (figure === 'triangle') {
        let lenght = Number(input[2]);
        area = (sideA * lenght) / 2;
    }
    console.log(area.toFixed(3));
}

getArea(["square", "5"]);
getArea(["rectangle", "7", "2.5"]);
getArea(["circle", "6"]);
getArea(["triangle", "4.5", "20"]);