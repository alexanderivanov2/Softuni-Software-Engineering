function solution() {
    let result = '';

    let append = (txt)  => result += txt;
    let removeStart = (n) => result = result.slice(n);
    let removeEnd = (n) => {
        let index = result.length - n;
        result = result.slice(0, index);
    }
    let print = () => console.log(result);

    return {append:append, removeStart:removeStart, removeEnd:removeEnd, print:print}
}

let firstZeroTest = solution();
firstZeroTest.append('hello');
firstZeroTest.append('again');
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();


let secondZeroTest = solution();

secondZeroTest.append('123');
secondZeroTest.append('45');
secondZeroTest.removeStart(2);
secondZeroTest.removeEnd(1);
secondZeroTest.print();