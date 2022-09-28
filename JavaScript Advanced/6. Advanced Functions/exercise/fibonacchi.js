function getFibonator() {
    let fibonachiN1 = 0
    let fibonachiN2 = 1;

    function addFib() {
        let previousFibonachi = fibonachiN2;
        fibonachiN2 += fibonachiN1;
        fibonachiN1 = previousFibonachi;
        return fibonachiN1;
    }

    return addFib
}


let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); 