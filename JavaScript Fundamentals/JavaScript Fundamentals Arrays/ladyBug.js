function ladyBugs(input) {
    let workingArray = input.slice()
    let length = workingArray.shift()
    let indexOfBugs = workingArray.shift().split(' ');
    let arr = new Array(length).fill(0);
    
    for (let el of indexOfBugs){
        let currentBug = Number(el);
        if (currentBug < 0 || currentBug >= length){
            continue;
        }
        arr [currentBug] = 1;
    }

    for (let i = 0; i < workingArray.length; i++){
        let [ladybug, direction, moves] = workingArray[i].split(' ');
        let ladyBug = Number(ladybug);

        if (arr[ladyBug] !== 1  || ladyBug >= arr.length || ladyBug < 0){
            continue;
        }

        // || moves === 0
        arr[ladyBug] = 0;
        
        moves = Number(moves);
        
        if (direction === 'left'){
            moves = -moves;
        }
        
        ladyBug += moves;

        while (ladyBug < arr.length && ladyBug >= 0 ){
            if (arr[ladyBug] === 0){
                arr[ladyBug] = 1;
                break;
            } 
            ladyBug += moves;
        }
    }
    console.log(arr.join(' '));
}

ladyBugs([ 3, '0 1',
'0 right 1',
'2 right 1' ]);

ladyBugs([ 5, '3',
'3 left 2',
'1 left -2']);

ladyBugs([ 3, '0 1 2',
'0 right 1',
'1 right 1',
'2 right 1']);