const cinema = require('../03. Cinema/cinema');
const {expect} = require('chai');
// console.log(cinema);

describe('cinema', () => {
    describe('showMovies', () => {
        let movieArr = ['a', 'b', 'c'];
        it('showMovies functionality', () => {
            expect(cinema.showMovies(movieArr)).to.be.equal('a, b, c');
            expect(cinema.showMovies(['a'])).to.be.equal('a');
            expect(cinema.showMovies(['a', 2])).to.be.equal('a, 2');
        });

        it('show movies empty array', () => {
            expect(cinema.showMovies([])).to.be.equal('There are currently no movies to show.');
            
        })
    });

    describe('ticketPrice', () => {
        it('result with correct input', () => {
            expect(cinema.ticketPrice('Premiere')).to.be.equal(12.00);
            expect(cinema.ticketPrice('Normal')).to.be.equal(7.50);
            expect(cinema.ticketPrice('Discount')).to.be.equal(5.50);
        });

        it('test with invalid input', () => {
            expect(() => cinema.ticketPrice(1)).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice('Test')).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice()).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice(true)).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice([])).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice({})).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice('asd')).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice(undefined)).to.throw('Invalid projection type.');
            expect(() => cinema.ticketPrice(null)).to.throw('Invalid projection type.');
            // expect(() => cinema.ticketPrice(NaN)).to.throw('Invalid projection type.');
        })
    });

    describe('swapSeatsInHall', () => {
        it('test invalid inputs', () =>{
            expect(cinema.swapSeatsInHall()).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall('1', 2)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall('1')).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall('1', '1')).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(2)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(2, '1')).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(true, 1)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, false)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(true, false)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(undefined, 2)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(undefined, undefined)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, undefined)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(null, 3)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(null, null)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, null)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(NaN, NaN)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, NaN)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall([], 3)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall([], [])).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(2, [])).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall({}, 2)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall({}, {})).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(3, {})).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(-1, 2)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(-1, -2)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(2, -1)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(0, 1)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, 0)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(21, 1)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, 21)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(21, 22)).to.be.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(2, 2)).to.be.equal('Unsuccessful change of seats in the hall.');
        }); 

        it('successfully change', () => {
            expect(cinema.swapSeatsInHall(1, 2)).to.be.equal('Successful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(20, 4)).to.be.equal('Successful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(19, 20)).to.be.equal('Successful change of seats in the hall.');
        })

        // it("Should return a specific message if the parameters are NaN", function () {
        //     assert.equal(cinema.swapSeatsInHall('test', 2), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(2, 'test'), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall('test', 'test'), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(['test'], 2), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(2, ['test']), "Unsuccessful change of seats in the hall.");
        // });

        // it("Should return a specific message if the parameters are less or equal to Zero", function () {
        //     assert.equal(cinema.swapSeatsInHall(-2, 2), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(2, -2), "Unsuccessful change of seats in the hall.");

        //     assert.equal(cinema.swapSeatsInHall(2, 0), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(0, 2), "Unsuccessful change of seats in the hall.");
        // });

        // it("Should return a specific message if the parameters are larger than 20", function () {
        //     assert.equal(cinema.swapSeatsInHall(22, 2), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(2, 22), "Unsuccessful change of seats in the hall.");
        // });

        // it("Should return a specific message if the parameters are equal", function () {
        //     assert.equal(cinema.swapSeatsInHall(2, 2), "Unsuccessful change of seats in the hall.");
        // });

        // it("Should return a specific message if we try to execute the function with less parameters", function () {
        //     assert.equal(cinema.swapSeatsInHall(2), "Unsuccessful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(), "Unsuccessful change of seats in the hall.");
        // });

        // it("Should work correctly", function () {
        //     assert.equal(cinema.swapSeatsInHall(5, 10), "Successful change of seats in the hall.");
        //     assert.equal(cinema.swapSeatsInHall(20, 10), "Successful change of seats in the hall."); // Border case
        //     assert.equal(cinema.swapSeatsInHall(5, 20), "Successful change of seats in the hall."); // Border case
        // });
    });       
});