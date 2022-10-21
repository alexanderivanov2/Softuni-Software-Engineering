const {expect} = require('chai');
const isOddOrEven = require('../isOddOrEven');

describe('Test Functionality of a Function', () => {
    it('Test with Number to return undefined', () => {
        const arg = 1;
        const result = isOddOrEven(arg);

        expect(result).to.be.undefined;
    });

    it('Test with object to return undefined', () => {
        const arg = {};
        const result = isOddOrEven(arg);

        expect(result).to.be.undefined;
    });
    
    it('Test String with Even length', () => {
        const string = 'AA';
        const result = isOddOrEven(string);
        const expectResult = 'even';

        expect(result).to.be.equal(expectResult);
    })

    it('Test Empty String to be equal as Even', () => {
        const string = '';
        const result = isOddOrEven(string);
        const expectResult = 'even';

        expect(result).to.be.equal(expectResult);
    })

    it('Test Empty String with Odd length', () => {
        const string = 'AAA';
        const result = isOddOrEven(string);
        const expectResult = 'odd';

        expect(result).to.be.equal(expectResult);
    })
});