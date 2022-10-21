const {expect} = require('chai');
const isSymmetric = require('../checkForSymmetry');

describe('check isSymetric Function', () => {
    // Arrange
    const symmetricArr = [2, 7, 2];
    const charSymmetric = ['a', 'a', 'a'];
    const unsymmetricArr = [1, 2, 3];
    const symetricOneElementArray = [2];
    const emptyArray = [];
    const arrgumentAsObj = {a: 'abc'};

    it('Test result if given argument is Object', () => {
        let result = isSymmetric(arrgumentAsObj);
        expect(result).to.equal(false);
    });

    it('return false for non-array number', () => {
        expect(isSymmetric(5)).to.be.false;
    });

    it('return false for string parameter', () => {
        expect(isSymmetric('abba')).to.be.false;
    })

    it('return true number array', () => {
        let symetricResult = isSymmetric(symmetricArr);
        expect(symetricResult).to.be.true;
    });

    it('return true string array', () => {
        let symetricResult2 = isSymmetric(charSymmetric);
        expect(symetricResult2).to.be.true;
    })

    it('return false unSymmetric number array', () => {
        let unsymmetricResut = isSymmetric(unsymmetricArr);
        expect(unsymmetricResut).to.be.false;
    });

    it('return true for one element Array', () => {
        let result = isSymmetric(symetricOneElementArray);
        expect(result).to.be.true;
    });

    it('return empty array for symmetry', () => {
        let result = isSymmetric(emptyArray);
        expect(result).to.be.true;
    });

    it('return false for array with different types', () => {
        expect(isSymmetric([1, 2, '1'])).to.be.false;
    });
});