let {expect} = require('chai');
let testNumbers = require('../testNumbers');

describe('testNumbers', () => {
    describe('sumNumber Tests', () =>{
        it('test sumNumbers function', () => {
            expect(testNumbers.sumNumbers(1, 1)).to.be.equal('2.00');
            expect(testNumbers.sumNumbers(1, -1)).to.be.equal('0.00');
            expect(testNumbers.sumNumbers(-1, 1)).to.be.equal('0.00');
            expect(testNumbers.sumNumbers(1, 0)).to.be.equal('1.00');
            expect(testNumbers.sumNumbers(0, 1)).to.be.equal('1.00');
            expect(testNumbers.sumNumbers(0, 0)).to.be.equal('0.00');
            expect(testNumbers.sumNumbers(-1, -1)).to.be.equal('-2.00');
            expect(testNumbers.sumNumbers(3.33, 4.44)).to.be.equal('7.77');
            expect(testNumbers.sumNumbers(-7.50, -2.50)).to.be.equal('-10.00');
        })

        it('test num1 not a number', () => {
            expect(testNumbers.sumNumbers(1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers()).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(undefined, 1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers('as',1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers([], 1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers({}, 1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(true, 1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(null, 1)).to.be.equal(undefined);
        });

        it('test num2 not a number', () => {
            expect(testNumbers.sumNumbers(1)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers()).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(1, undefined)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(1,'as')).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(1, [])).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(1, {})).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(1, true)).to.be.equal(undefined);
            expect(testNumbers.sumNumbers(1, null)).to.be.equal(undefined);
        });
    });

    describe('numberChecker', () => {
        it(' test functionality', () => {
            expect(testNumbers.numberChecker(2)).to.be.equal('The number is even!');
            expect(testNumbers.numberChecker(2.22)).to.be.equal('The number is odd!');
            expect(testNumbers.numberChecker(0)).to.be.equal('The number is even!');
            expect(testNumbers.numberChecker(-2)).to.be.equal('The number is even!');
            expect(testNumbers.numberChecker(1)).to.be.equal('The number is odd!');
            expect(testNumbers.numberChecker(3.33)).to.be.equal('The number is odd!');
            expect(testNumbers.numberChecker(-11)).to.be.equal('The number is odd!');
            expect(testNumbers.numberChecker(2.00)).to.be.equal('The number is even!');
            expect(testNumbers.numberChecker('2')).to.be.equal('The number is even!');
            expect(testNumbers.numberChecker('2.22')).to.be.equal('The number is odd!');
            expect(testNumbers.numberChecker('0')).to.be.equal('The number is even!');
            expect(testNumbers.numberChecker('-2')).to.be.equal('The number is even!');
        });

        it('test with NaN inputs', () => {
            expect(() => testNumbers.numberChecker()).to.throw('The input is not a number!');
            // expect(() => testNumbers.numberChecker(null)).to.throw('The input is not a number!');
            expect(() => testNumbers.numberChecker(undefined)).to.throw('The input is not a number!');
            // expect(() => testNumbers.numberChecker(false)).to.throw('The input is not a number!');
            // expect(() => testNumbers.numberChecker([])).to.throw('The input is not a number!');
            expect(() => testNumbers.numberChecker({})).to.throw('The input is not a number!');
        });
    });

    describe('averageSumArray', () => {
        it('averageSumArray functionality', () => {
            expect(testNumbers.averageSumArray([1])).to.be.equal(1);
            expect(testNumbers.averageSumArray([1, 2])).to.be.equal(1.5);
            expect(testNumbers.averageSumArray([1, 2, 3])).to.be.equal(2);
            expect(testNumbers.averageSumArray([3.33, 3.33])).to.be.equal(3.33);
        });
    });
});