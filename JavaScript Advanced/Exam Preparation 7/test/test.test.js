const { assert, expect } = require('chai');
const { numberOperations } = require('../03. Number Operations_Resources.js');

console.log(numberOperations);

describe('Testing Number Operations', () => {
    describe('Test powNumber', () => {
        it('test power', () => {
            expect(numberOperations.powNumber(2)).to.be.equal(4);
            expect(numberOperations.powNumber(7)).to.be.equal(49);
            expect(numberOperations.powNumber(3)).to.be.equal(9);
            expect(numberOperations.powNumber(1)).to.be.equal(1);
        });
    })

    describe('Test numberChecker', () => {
        it('isNaN', () => {
            expect(() => numberOperations.numberChecker('a')).to.throw('The input is not a number!');
            expect(() => numberOperations.numberChecker({})).to.throw('The input is not a number!');
        });

        it('Test with number lower than 100', () => {
            expect(numberOperations.numberChecker('99')).to.be.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker(99)).to.be.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker(99.9)).to.be.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker(-100)).to.be.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker('')).to.be.equal('The number is lower than 100!');
        });

        it('Test with numbers greater or equal to 100!', () => {
            expect(numberOperations.numberChecker('100')).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker(100)).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker(100.1)).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker(101)).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker('1000')).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker('100.1')).to.be.equal('The number is greater or equal to 100!');
        });
    });

    describe('Test sumArrays', () => {
        it('Test sumArrays with first larger', () => {
            const arrayOne = [1, 2, 3, 4];
            const arrayTwo = [1, 2, 3];
            const result = [2, 4, 6, 4];
            const resultFunction = numberOperations.sumArrays(arrayOne, arrayTwo);
            assert.deepEqual(resultFunction, result);
            expect(numberOperations.sumArrays(arrayOne, arrayTwo)).to.deep.equal(result);
        });
        
        it('Test sumArrays with second larger', () => {
            const arrayOne = [1, 2, 3];
            const arrayTwo = [1, 2, 3, 4];
            const result = [2, 4, 6, 4];
            const resultFunction = numberOperations.sumArrays(arrayOne, arrayTwo);
            assert.deepEqual(resultFunction, result);
            expect(numberOperations.sumArrays(arrayOne, arrayTwo)).to.deep.equal(result);
        });
    });
});