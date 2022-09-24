function jansNotation(input) {
    let operations = {
        '+'(a, b)  {
            return a + b;
        },
        '-'(a, b) {
            return a - b;
        },
        '*'(a, b) {
            return a * b;
        },
        '/'(a, b) {
            return a / b;
        }
    }
    let nums = [];
    for (let el of input) {
        if (isNaN(el)) {
            if (nums.length < 2) {
                console.log( "Error: not enough operands!");
                return
            } 
            let num2 = nums.pop();
            let num1 = nums.pop();
            nums.push(operations[el](num1, num2));
        } else {
            nums.push(el);
        }
    }
    if (nums.length > 1) {
        console.log('Error: too many operands!')
    } else {
        console.log(nums[0]);
    }
}

jansNotation([5,
    3,
    4,
    '*',
    '-']);