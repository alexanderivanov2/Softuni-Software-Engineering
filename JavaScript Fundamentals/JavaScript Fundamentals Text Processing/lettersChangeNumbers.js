function solve(arr) {
    arr = arr.split(' ');
    let curArr = arr.filter(x => x !== ''); 
    let chPosition = x => x.toUpperCase().charCodeAt(0) - 64;
    let totalSum = 0;

    for (let strEl of curArr) {
        let result = 0;
        let str = strEl.trim().split('');
        let firstCh = str.shift();
        let lastCh = str.pop();
        let n = Number(str.join(''));
        let chOnePostion = chPosition(firstCh);
        let chTwoPostion = chPosition(lastCh);
        
        if (firstCh === firstCh.toUpperCase()) {
            result += n / chOnePostion;
        } else {
            result += n * chOnePostion;
        }

        if (lastCh === lastCh.toUpperCase()) {
            result -= chTwoPostion;
        } else {
            result += chTwoPostion;
        }

        totalSum += result;
    }

    console.log(totalSum.toFixed(2));

}

// solve('A12b s17G');
solve('P34562Z q2576f    H456z');