const { expect } = require('chai');
const { flowerShop } = require('../flowerShop.js');


describe('Testing FlowerShop', () => {
    describe('Test calcPriceOfFlowers', () => {
        it('test invalid input!', () => {
            expect(() => flowerShop.calcPriceOfFlowers(2, 2, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(true, 2, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers([], 2, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers({})).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, '2', 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, true, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, [], 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, {}, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, 2, '2')).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, 2, true)).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, 2, [])).to.throw('Invalid input!');
            expect(() => flowerShop.calcPriceOfFlowers(2, 2, {})).to.throw('Invalid input!');
        });

        it('Test calcPrice Of Flowers', () => {
            expect(flowerShop.calcPriceOfFlowers('A', 2, 2)).to.be.equal('You need $4.00 to buy A!');
            expect(flowerShop.calcPriceOfFlowers('A', 2, 39)).to.be.equal('You need $78.00 to buy A!');
        })
    });

    describe('Test checkFlowersAvailable', () => {
        it ('test when flower is available', () => {
            const garderArr = ['a', 'b', 'c'];
            expect(flowerShop.checkFlowersAvailable('a', garderArr)).to.be.equal(`The a are available!`);
            expect(flowerShop.checkFlowersAvailable('b', garderArr)).to.be.equal(`The b are available!`);
            expect(flowerShop.checkFlowersAvailable('c', garderArr)).to.be.equal(`The c are available!`);
        });

        it('test when flower is not available', () => {
            const garderArr = ['a', 'b', 'c'];
            expect(flowerShop.checkFlowersAvailable('aaa', garderArr)).to.be.equal(`The aaa are sold! You need to purchase more!`);
            expect(flowerShop.checkFlowersAvailable('bbb', garderArr)).to.be.equal(`The bbb are sold! You need to purchase more!`);
        });
    });

    describe('test sellFlowers', () => {
        it ('Test with invalid Input', () => {
            expect(() => flowerShop.sellFlowers('', 2)).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers({}, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers(true, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers(1, 2)).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers([], '')).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers([], [])).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers([], {})).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers([], true)).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers([], -1)).to.throw('Invalid input!');
            expect(() => flowerShop.sellFlowers([], 1)).to.throw('Invalid input!');
        });

        it('Test sellFlowers', () => {
            const gardenArr = ['a', 'b', 'c'];
            expect(flowerShop.sellFlowers(gardenArr, 2)).to.be.equal('a / b');
            expect(flowerShop.sellFlowers(gardenArr, 1)).to.be.equal('a / c');
            expect(flowerShop.sellFlowers(gardenArr, 0)).to.be.equal('b / c');
        });
    });
});