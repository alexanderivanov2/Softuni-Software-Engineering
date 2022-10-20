const {expect} = require('chai');
const sum = require('../sumOfNumbers');

describe('sum of numbers in array', () => {
    let arr = [10, 20, 30];
    let arrWithNegativeNumbers = [-10, 10, 70]; 
    let arrWithOneNumber = [27];
    let emptyArr = [];
    let expectedSumArr = 60;
    let expectSumArrWithNegativeNumbers = 70;
    let expectSumArrWithOneNumber = 27;
    let expectSumOfAnEmptyArray = 0;

    it('is sum Equal', () =>{
        expect(sum(arr)).to.equal(expectedSumArr);
    });

    it('is sum Equal with Negative numbers', () => {
        expect(sum(arrWithNegativeNumbers)).to.equal(expectSumArrWithNegativeNumbers);
    });

    it('is sum Equal for array with One number', () => {
        expect(sum(arrWithOneNumber)).to.equal(expectSumArrWithOneNumber);
    });

    it('is sum Equal to empty array ', () => {
        expect(sum(emptyArr)).to.equal(expectSumOfAnEmptyArray);
    });
});