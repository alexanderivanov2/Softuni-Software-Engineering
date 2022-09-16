function solve(input) {
    let half = input.length / 2;
    let partOne = input.slice(0, half);
    let partTwo = input.slice(half);
    let reversePartOne = '';
    let reversePartTwo = '';
    for (let i = partOne.length - 1; i >= 0; i-=1){
        reversePartOne += partOne[i];
        reversePartTwo += partTwo[i];
    }
    console.log(reversePartOne);
    console.log(reversePartTwo);
}

solve('tluciffiDsIsihTgnizamAoSsIsihT')