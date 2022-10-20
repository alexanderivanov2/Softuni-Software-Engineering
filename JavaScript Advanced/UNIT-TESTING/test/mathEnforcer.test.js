const mathEnforcer = require('../mathEnforcer');
const {expect} = require('chai');

describe('mathEnforcer', () => {

    describe('addFive', () => {
        it('Test when argumment is not a Number', () => {
            const addFive = mathEnforcer['addFive'];
            const argString = '1';
            const argObj = {};

            expect(addFive(argString)).to.be.undefined;
            expect(addFive(argObj)).to.be.undefined;
        });

        it('Test result when argumment is correct', () => {
            const addFive = mathEnforcer['addFive'];
            const argPositiveNum = 2;
            const argZero = 0;
            const argNegativeNum = -3;
            const argFloatingNum = 3.33;

            expect(addFive(argPositiveNum)).to.be.equal(7);
            expect(addFive(argZero)).to.be.equal(5);
            expect(addFive(argNegativeNum)).to.be.equal(2);
            expect(addFive(argFloatingNum)).to.be.equal(8.33);
        })
    });

    describe('subtractTen', () => {
        it('Test With argument which is not a Number', () => {
            const subtractTen = mathEnforcer['subtractTen'];
            const argString = '1';
            const argObj = {};

            expect(subtractTen(argString)).to.be.undefined;
            expect(subtractTen(argObj)).to.be.undefined;
        });

        it('Test subtractTen with Correct arguments', () => {
            const subtractTen = mathEnforcer['subtractTen'];
            const argPositiveNum = 12;
            const argZero = 0;
            const argNegativeNum = -3;
            const argFloatingNum = 13.33;

            expect(subtractTen(argPositiveNum)).to.be.equal(2);
            expect(subtractTen(argZero)).to.be.equal(-10);
            expect(subtractTen(argNegativeNum)).to.be.equal(-13);
            expect(subtractTen(argFloatingNum)).to.be.equal(3.33);
        });
    });


    describe('sum', () => {

        it('Test Nevalid num1, num2 or Both', () => {
            const sum2 = mathEnforcer.sum;
            const num1String = '1';
            const num1Number = 1;
            const num2String = '1';
            const num2Number = 71;
            const num1Obj = {}
        
            expect(sum2(num1Number, num2String)).to.be.undefined;
            expect(sum2(num1String, num2Number)).to.be.undefined;
            expect(sum2(num1String, num2String)).to.be.undefined;
            expect(sum2(num1Obj, num2Number)).to.be.undefined;
        });

        it('Test with valid num1 and num2', () => {
            const sum2 = mathEnforcer.sum;
            const positive = [2, 75];
            const negative = [-2, -75];
            const positiveNegative = [78, -1];
            const numAndZero = [0, 77];
            const argFloatingNum = 3.33;

            expect(sum2(positive[0], positive[1])).to.be.equal(77);
            expect(sum2(negative[0], negative[1])).to.be.equal(-77);
            expect(sum2(positiveNegative[0], positiveNegative[1])).to.be.equal(77);
            expect(sum2(numAndZero[0], numAndZero[1])).to.be.equal(77);
            expect(sum2(argFloatingNum, 4.44)).to.be.equal(7.7700000000000005);
        });
    });
});