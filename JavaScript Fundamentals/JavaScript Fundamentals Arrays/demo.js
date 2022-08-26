function ladyBugs(input) {

    let length = input[0];
    let indexOfBugs = input[1].split(' ');
    let arr = [];
    
    for (let i = 0; i < length; i++){
        
        if (indexOfBugs.includes(String(i))){
            arr.push(1);
        } else {
            arr.push(0)
        }
    }

    for (let i = 2; i < input.length; i++){
        
        let splitStr = input[i].split(' ');
        let ladyBug = Number(splitStr[0]);
        let direction = splitStr[1];
        let moves = Number(splitStr[2]);
        let done = false
        let nextIndex = ladyBug;
        
        if (arr[ladyBug] !== 1 || moves === 0 || ladyBug >= arr.length || ladyBug < 0){
            continue;
        } else {
            if (moves < 0){
                direction = direction === 'left' ? 'right' : 'left';
                moves *= -1; 
            }
            if (direction === 'left'){
                nextIndex -= moves;
            } else {
                nextIndex += moves;
            }
        }

        arr[ladyBug] = 0;

        while (nextIndex < length && nextIndex >= 0 ){

            if (arr[nextIndex] === 0){
                arr[nextIndex] = 1;
                break;
            } 

            if (direction === 'left'){
                nextIndex -= moves;
            } else {
                nextIndex += moves;
            }
        }
    }
    console.log(arr.join(' '));
}


  ladyBugs([ 3, '0 1 2',
  '0 right 1',
  '1 right 1',
  '2 right 1']);