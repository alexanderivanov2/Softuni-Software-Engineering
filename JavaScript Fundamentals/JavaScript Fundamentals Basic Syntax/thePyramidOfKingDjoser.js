function calculateResourcesForPyramid(input1, input2) {
    let base = input1;
    let increment = input2;
    let stone = 0;
    let marble = 0;
    let lapisLazuli = 0;
    let gold = 0;
    let height = 0;
    for (let i = base; i >= 1; i -= 2) {
        height += 1;
        fullArea = i * i;
        if (i - 2 < 1){
            gold += fullArea * increment;
            break;
        }
        curStone = Math.pow(i - 2, 2);
        stone += curStone * increment;   
        if (height % 5 === 0){
            lapisLazuli += (fullArea - curStone) * increment;
        } else {
            marble += (fullArea - curStone) * increment;
        }   
    }
    height *= increment;
    console.log(`Stone required: ${Math.ceil(stone)}\nMarble required: ${Math.ceil(marble)}\nLapis Lazuli required: ${Math.ceil(lapisLazuli)}\nGold required: ${Math.ceil(gold)}\nFinal pyramid height: ${Math.floor(height)}`);    
}


calculateResourcesForPyramid(11, 0.75);
calculateResourcesForPyramid(12,1);
calculateResourcesForPyramid(23, 0.5);


