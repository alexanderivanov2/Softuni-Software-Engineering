const {expect} = require('chai');
const lookupChar = require('../charLookup');

describe('Test LookupChar Function', () => {
    it('Test with not a string', () => {
        const argNum = 123;
        const argObj = {a:'aaa'};
        const argNaN = NaN;
        
        expect(lookupChar(argNum, 0)).to.be.undefined;
        expect(lookupChar(argObj, 0)).to.be.undefined;
        expect(lookupChar(argNaN, 0)).to.be.undefined;
    });

    it('Test with not a number Index', () => {
        const argString = 'AaBbCc';
        const argSecondString = '1';
        const argObj = {a:'aaa'};
        const argNaN = NaN;

        expect(lookupChar(argString, argSecondString)).to.be.undefined;
        expect(lookupChar(argString, argObj)).to.be.undefined;
        expect(lookupChar(argString, argNaN)).to.be.undefined;
    });

    it('Test with incorrect index', () => {
        const argString = 'AaBbCc';
        const argIndexUnderZero = -1;
        const argIndexOverLength = 6;
        const expectedResult = 'Incorrect index';

        expect(lookupChar(argString, argIndexUnderZero)).to.be.equal(expectedResult);
        expect(lookupChar(argString, argIndexOverLength)).to.be.equal(expectedResult);
    });

    it('Test Return result charAt', () => {
        const argString = 'AaBbCc';
        let resulCharAtFirstIndex = lookupChar(argString, 0);
        let resultCharAtLastIndex = lookupChar(argString, 5);
        let resultCharAtMiddleIndex = lookupChar(argString, 2);

        expect(resulCharAtFirstIndex).to.be.equal('A');
        expect(resultCharAtLastIndex).to.be.equal('c');
        expect(resultCharAtMiddleIndex).to.be.equal('B');
    });
});