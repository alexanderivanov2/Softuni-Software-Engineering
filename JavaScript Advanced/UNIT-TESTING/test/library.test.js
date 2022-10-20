const {expect} = require('chai');
let library = require('../Resource/library');

describe('library', () => {
    describe('Test CaclPriceOfBook', () => {
        // console.log(library);
        it('test invalid input', () => {
            expect(() => library.calcPriceOfBook()).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook(123, 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook([], 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook({}, 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook(undefined, 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook(null, 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook(NaN, 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook(false, 123)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook('aa')).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook('aa', [])).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook('aa', {})).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook('aa', undefined)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook('aa', null)).to.throw('Invalid input');
            expect(() => library.calcPriceOfBook('aa', true)).to.throw('Invalid input');
        });
    
        it('test price of year before 1980', () => {
            let result = `Price of a is 10.00`
            expect(library.calcPriceOfBook('a', 1980)).to.be.equal(result);
            expect(library.calcPriceOfBook('a', 1979)).to.be.equal(result);
            expect(library.calcPriceOfBook('a', 0)).to.be.equal(result);
            expect(library.calcPriceOfBook('a', 2)).to.be.equal(result);
            expect(library.calcPriceOfBook('a', 1981)).to.not.be.equal(result);
        });
    
        it('test price of year after 1980', () => {
            let result = `Price of a is 20.00`
            expect(library.calcPriceOfBook('a', 1980)).to.not.be.equal(result);
            expect(library.calcPriceOfBook('a', 1979)).to.not.be.equal(result);
            expect(library.calcPriceOfBook('a', 0)).to.not.be.equal(result);
            expect(library.calcPriceOfBook('a', 2)).to.not.be.equal(result);
            expect(library.calcPriceOfBook('a', 1981)).to.be.equal(result);
            expect(library.calcPriceOfBook('a', 1981)).to.be.equal(result);
        });
    });

    describe('test findBook function', ()=>{
        it('test emptyArr', () => {
            expect(() => library.findBook([], 'a')).to.throw("No books currently available");
        });

        it('test availabel book', () => {
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], 'a')).to.be.equal("We found the book you want.");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], 'b')).to.be.equal("We found the book you want.");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], 1)).to.be.equal("We found the book you want.");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], true)).to.be.equal("We found the book you want.");
        });

        it('test unavailable book', () => {
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], 'c')).to.be.equal("The book you are looking for is not here!");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], 'd')).to.be.equal("The book you are looking for is not here!");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], 2)).to.be.equal("The book you are looking for is not here!");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], {})).to.be.equal("The book you are looking for is not here!");
            expect(library.findBook(['a', 'b', 1, true, undefined, null, {}, []], [])).to.be.equal("The book you are looking for is not here!");
        });
    });

    describe('Test arrangeTheBooks function', () => {
        it('test countBooks not a number', () => {
            expect(() => library.arrangeTheBooks('a')).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks([])).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks({})).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(undefined)).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(null)).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(NaN)).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(true)).to.throw("Invalid input");
        });

        it('test countBooks not a number', () => {
            expect(() => library.arrangeTheBooks(-2)).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(-100)).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(0)).to.not.throw("Invalid input")
            expect(() => library.arrangeTheBooks(100)).to.not.throw("Invalid input");;    
        });

        it('test available space', () => {
            expect(library.arrangeTheBooks(2)).to.be.equal("Great job, the books are arranged.");
            expect(library.arrangeTheBooks(5)).to.be.equal("Great job, the books are arranged.");
            expect(library.arrangeTheBooks(40)).to.be.equal("Great job, the books are arranged.");
            expect(library.arrangeTheBooks(39)).to.be.equal("Great job, the books are arranged.");
            expect(library.arrangeTheBooks(0)).to.be.equal("Great job, the books are arranged.");
        })

        it('test not enough space', () => {
            expect(library.arrangeTheBooks(41)).to.be.equal("Insufficient space, more shelves need to be purchased.");
            expect(library.arrangeTheBooks(141)).to.be.equal("Insufficient space, more shelves need to be purchased.");
            expect(library.arrangeTheBooks(45)).to.be.equal("Insufficient space, more shelves need to be purchased.");
            expect(library.arrangeTheBooks(40)).to.not.be.equal("Insufficient space, more shelves need to be purchased.");
        });
    });
});

