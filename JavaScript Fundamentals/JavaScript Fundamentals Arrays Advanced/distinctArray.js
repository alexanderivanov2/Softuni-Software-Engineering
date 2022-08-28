function filterDouplicateInArr(arr) {
    let filtredArr = [];
    filtredArr = arr.filter((num, i) => {
        return arr.indexOf(num) === i;
    });
    console.log(filtredArr.join(' '));
}

filterDouplicateInArr([7, 8, 9, 7, 2, 3, 4, 1, 2]);
