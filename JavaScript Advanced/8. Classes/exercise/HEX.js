class Hex {
    constructor(value) {
        this.value = value;
    }

    valueOf() {
        return this.value;
    }

    toString() {
        let result = '0x';
        result += this.value.toString(16).toUpperCase();
        return result;
    }

    plus(number) {
        let value = this.value;
        if (number instanceof Hex) {
            value += number.valueOf();
        } else {
            value += number;
        }

        return new Hex(value);
    }

    minus(number) {
        let value = this.value;
        if (number instanceof Hex) {
            value -= number.valueOf();
        } else {
            value -= number;
        }

        return new Hex(value);
    }

    parse(string) {
        return parseInt(string, 16);
    }
}



let FF = new Hex(255);
console.log(FF.toString());
console.log(FF.valueOf() + 1 == 256);
let a = new Hex(10);
let b = new Hex(5);
console.log(a.plus(b).toString());
console.log(a.plus(b).toString()==='0xF');
console.log(FF.parse('AAA'));