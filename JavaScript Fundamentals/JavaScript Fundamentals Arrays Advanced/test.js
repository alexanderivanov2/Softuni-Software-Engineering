let arr = [1, 2, 3, 4, 5];
let resArr = [];
for (let i = 0; i < arr.length - 1; i+= 2){
    resArr.push(arr[i] + arr[i + 1]);
}

console.log(resArr);