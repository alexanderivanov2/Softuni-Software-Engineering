const { expect } = require('chai');
const { carService } = require('../03. Car service_Resources.js');

// expect(() => ).to.throw();
// expect().to.be.equal();

describe('test Car Service', () => {
    describe('test is it Expensive', () => {
        it('test engine or tansmisiion', () => {
            expect(carService.isItExpensive('Transmission')).to.be.equal(`The issue with the car is more severe and it will cost more money`);
            expect(carService.isItExpensive('Engine')).to.be.equal(`The issue with the car is more severe and it will cost more money`);
            expect(carService.isItExpensive('Other')).to.be.equal(`The overall price will be a bit cheaper`);
        });

    });

    describe('test discount', () => {
        it ('test for invalid input', () => {
            expect(() => carService.discount('', 2)).to.throw("Invalid input");
            expect(() => carService.discount(true, 2)).to.throw("Invalid input");
            expect(() => carService.discount([], 2)).to.throw("Invalid input");
            expect(() => carService.discount({},)).to.throw("Invalid input");
            expect(() => carService.discount('')).to.throw("Invalid input");
            expect(() => carService.discount(1, '')).to.throw("Invalid input");
            expect(() => carService.discount(2, false)).to.throw("Invalid input");
            expect(() => carService.discount(3, [])).to.throw("Invalid input");
            expect(() => carService.discount(3, {})).to.throw("Invalid input");
            expect(() => carService.discount(3)).to.throw("Invalid input");
        });

        it('test you cannot apply discount', () => {
            expect(carService.discount(2, 10)).to.be.equal("You cannot apply a discount");
            expect(carService.discount(1, 10)).to.be.equal("You cannot apply a discount");
            expect(carService.discount(0, 10)).to.be.equal("You cannot apply a discount");
        });

        it('test with discount 30', () => {
            expect(carService.discount(8, 100)).to.be.equal(`Discount applied! You saved 30$`);
            expect(carService.discount(9, 100)).to.be.equal(`Discount applied! You saved 30$`);
            expect(carService.discount(100, 100)).to.be.equal(`Discount applied! You saved 30$`);
        });

        it('test with discount 15', () => {
            expect(carService.discount(7, 100)).to.be.equal(`Discount applied! You saved 15$`);
            expect(carService.discount(3, 100)).to.be.equal(`Discount applied! You saved 15$`);
            expect(carService.discount(5, 100)).to.be.equal(`Discount applied! You saved 15$`);
            
        });

        
    });

    describe('test parts toBuy', () => {
        it ('test invalid input', () => {
            expect(() => carService.partsToBuy('')).to.throw('Invalid input');
            expect(() => carService.partsToBuy('', [])).to.throw('Invalid input');
            expect(() => carService.partsToBuy(1, [])).to.throw('Invalid input');
            expect(() => carService.partsToBuy(true, [])).to.throw('Invalid input');
            expect(() => carService.partsToBuy('test', [])).to.throw('Invalid input');
            expect(() => carService.partsToBuy({}, [])).to.throw('Invalid input');
            expect(() => carService.partsToBuy([], true)).to.throw('Invalid input');
            expect(() => carService.partsToBuy([], '')).to.throw('Invalid input');
            expect(() => carService.partsToBuy([])).to.throw('Invalid input');
            expect(() => carService.partsToBuy([], 'y')).to.throw('Invalid input');
            expect(() => carService.partsToBuy([], {})).to.throw('Invalid input');
            expect(() => carService.partsToBuy([], 1)).to.throw('Invalid input');
        });

        it('test total sum', () => {
            const catalog = [{part: 'a', price: 1 }, {part: 'b', price: 1 }, {part: 'c', price: 1 }];
            const allParts = ['a', 'b', 'c'];
            const noParts = [];
            const allDifferentParts = ['ab', 'bb', 'cc'];
            const someDiffParts = ['a', 'd', 'c'];

            expect(carService.partsToBuy(catalog, allParts)).to.be.equal(3);
            expect(carService.partsToBuy(catalog, noParts)).to.be.equal(0);
            expect(carService.partsToBuy(catalog, allDifferentParts)).to.be.equal(0);
            expect(carService.partsToBuy(catalog, someDiffParts)).to.be.equal(2);
        });
    });
});

// it('', () => {
           
// })