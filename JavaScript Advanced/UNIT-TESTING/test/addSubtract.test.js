const {expect} = require('chai');
const createCalculator = require('../addSubtract');

describe('Test functionality of calculator', () => {
    let calculator = {};
    beforeEach(() => { calculator = createCalculator();});
    
    it('Test has all methods', () => {
        expect(calculator).to.has.ownProperty('add');
        expect(calculator).to.has.ownProperty('subtract');
        expect(calculator).to.has.ownProperty('get');
    });

    it('Test Create Calculator', () => {
        expect(typeof calculator).to.equal('object');
    });

    it('Test get function', () => {
        expect(calculator.get()).to.equal(0);
    });

    it('Test add function', () => {
        calculator.add(1);
        calculator.add(2);
        expect(calculator.get()).to.equal(3);
    });

    it('Test subtract function', () => {
        calculator.subtract(5);
        expect(calculator.get()).to.equal(-5);
    });

    it('Test add and subtract with Zero', () => {
        calculator.add(0);
        expect(calculator.get()).to.equal(0);
        calculator.subtract(0);
        expect(calculator.get()).to.equal(0);
    });

    it('Test numbers as string', () => {
        calculator.add('7');
        expect(calculator.get()).to.equal(7);
        calculator.subtract('3');
        expect(calculator.get()).to.equal(4);
    });
});