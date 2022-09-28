function solution(n) {
    
    let add = function (a, b) {
        return a + b;
    } ;

    return add.bind(this, n);

}


let add5 = solution(5);
console.log(add5(2));
console.log(add5(3));