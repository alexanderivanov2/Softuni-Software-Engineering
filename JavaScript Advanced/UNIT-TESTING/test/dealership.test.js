const {expect} = require('chai');
const dealership = require('../dealership');

console.log(dealership);

describe('Dealership', () => {
    describe('new Carc Cost', () => {
        it ('price without discount', () => {
            expect(dealership.newCarCost('A', 1500)).to.be.equal(1500);
        });
        
        it ('price with discount', () => {
            expect(dealership.newCarCost('Audi A4 B8', 30000)).to.be.equal(15000);
            expect(dealership.newCarCost('Audi A6 4K' ,30000)).to.be.equal(10000);
            expect(dealership.newCarCost('Audi A8 D5', 30000)).to.be.equal(5000);
            expect(dealership.newCarCost('Audi TT 8J', 30000)).to.be.equal(16000);
        });
    });

    describe('carEquipment', () => {
        it('test selected extras', () => {
            expect(dealership.carEquipment(['a', 'b', 'c'], [0, 2])).to.be.deep.equal(['a', 'c']);
        });
    });

    describe('euroCategory', () => {
        it('test low energy level', () => {
            const result = 'Your euro category is low, so there is no discount from the final price!';

            expect(dealership.euroCategory(2)).to.be.equal(result);
        });

        it('test high euro category', () => {
            expect(dealership.euroCategory(4)).to.be.equal(`We have added 5% discount to the final price: ${14250}.`);
        });
    });
});