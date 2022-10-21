const {expect} = require('chai');
const ChristmasMovies = require('../02. Christmas Movies_Resources');

describe('tests at ChristamsMovie class', function() {
	let cm;
	this.beforeEach(function() {
		cm = new ChristmasMovies();
	})
	describe('tests all initial properties', function() {
		//test 1
		it('Instantiation with no parameters', function() {
			expect(cm.movieCollection).to.eql([]);
			expect(cm.movieCollection.length).to.deep.equal(0);
			expect(cm.watched).to.eql({});
			expect(cm.actors).to.deep.equal([]);
			expect(cm.actors.length).to.deep.equal(0);
		});
	});
 
	describe('tests function buyMovie', function() {
		// test 2
		it('should return added corectly a movie', function() {
			expect(cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']))
			.to.equal('You just got Last Christmas to your collection in which Madison Ingoldsby, Emma Thompson, Boris Isakovic are taking part!');
		});
 
		it('should thrown error that exist a movie name', function() {
			cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']);
			expect(() => cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']))
			.to.throw(Error, 'You already own Last Christmas in your collection!');
		});
	});
 
	describe('tests function discardMovie', function() {
		it('should throw error that no exist movie name', function() {
			expect(() => cm.discardMovie('The Grunch')).to.throw(Error, 'The Grunch is not at your collection!');
		});
 
		it('should throw error that no exist movie watch', function() {
			cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']);
			expect(() => cm.discardMovie('Last Christmas')).to.throw(Error, 'Last Christmas is not watched!');
		});
 
		it('should return message that correctly remove a movie', function() {
			cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']);
			cm.watchMovie('Last Christmas');
			expect(cm.discardMovie('Last Christmas')).to.equal('You just threw away Last Christmas!');
		});
	});
 
	describe('tests function watchMovie', function() {
		it('should throw error that no exist in collection list this a movie name', function() {
			expect(()=> cm.watchMovie('The Grunch')).to.throw(Error, 'No such movie in your collection!');
		});
 
		it('should return three watched a movie', function() {
			cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']);
			cm.watchMovie('Last Christmas');
			cm.watchMovie('Last Christmas');
			cm.watchMovie('Last Christmas');
			expect(cm.watched['Last Christmas']).to.deep.equal(3);
		});
	});
 
	describe('tests function favouriteMovie', function() {
		it('should thtow error that empty watched collection', function() {
			expect(() => cm.favouriteMovie()).to.throw(Error, 'You have not watched a movie yet this year!');
		});
 
		it('should return a movie with the most watched', function() {
			cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']);
			cm.buyMovie('Home Alone', ['Macaulay Culkin', 'Joe Pesci', 'Daniel Stern']);
			cm.watchMovie('Last Christmas');
			cm.watchMovie('Last Christmas');
			cm.watchMovie('Last Christmas');
			cm.watchMovie('Home Alone');
			expect(cm.favouriteMovie()).to.equal('Your favourite movie is Last Christmas and you have watched it 3 times!');
		});
	});
 
	describe('tests function mostStarredActors', function() {
		//test 11
		it('should throw error that empty movieCollection', function() {
			expect(() => cm.mostStarredActor()).to.throw(Error, 'You have not watched a movie yet this year!');
		});
		//test 10
		it('should return the most played actor  in the movies', function() {
			cm.buyMovie('Home Alone', ['Macaulay Culkin', 'Joe Pesci', 'Daniel Stern']);
			cm.buyMovie('Last Christmas', ['Madison Ingoldsby', 'Emma Thompson', 'Boris Isakovic', 'Madison Ingoldsby']);
			cm.buyMovie('Home Alone 2', ['Macaulay Culkin']);
			cm.buyMovie('Home Alone 3', ['Macaulay Culkin', 'Emma Thompson']);
			cm.watchMovie('Home Alone');
			expect(cm.mostStarredActor()).to.equal('The most starred actor is Macaulay Culkin and starred in 3 movies!');
 
		});
	});
});

// describe('Christmas Movies', () => {
//     describe('Test Constructor', () => {
//         let movies = new ChristmasMovies();
//         movies.buyMovie('a', ['a', 'b', 'c']);
//         it('test movie collection', () => {
//             expect(typeof movies.movieCollection).to.be.equal('object');
//         });

//         it('test watched', () => {
//             expect(typeof movies.watched).to.be.equal('object');
//         });

//         it('test movie collection', () => {
//             expect(typeof movies.actors).to.be.equal('object');
//         });
//     });

//     describe('buyMovie', () => {
//         let movies = new ChristmasMovies();
//         movies.buyMovie('a', ['a', 'b', 'c']);
//        it('test  to add own movie again', () => {
//         expect(() => movies.buyMovie('a', [])).to.throw('You already own a in your collection!');
//         // expect(() => movies.buyMovie('a')).to.throw('You already own a in your collection!');
//         expect(() => movies.buyMovie('a', ['b'])).to.throw('You already own a in your collection!');
//        });

//        it('test buy movie', () => {
//            expect(movies.buyMovie('b', ['a', 'b'])).to.be.equal(`You just got b to your collection in which a, b are taking part!`);
//         //    expect(movies.buyMovie('c')).to.be.equal(`You just got c to your collection in which  are taking part!`);
//            expect(movies.buyMovie('d', [])).to.be.equal(`You just got d to your collection in which  are taking part!`);
//        });
//     });

//     describe('discardMovie', () => {
//         let movies = new ChristmasMovies();
//         movies.buyMovie('a', ['a', 'b', 'c']);
//         it('filter with movie that not exost', () => {
//             expect(() => movies.discardMovie('e')).to.throw(`e is not at your collection!`);
//             expect(() => movies.discardMovie()).to.throw(` is not at your collection!`)
//             expect(() => movies.discardMovie({})).to.throw(`[object Object] is not at your collection!`);
//             expect(() => movies.discardMovie([])).to.throw(` is not at your collection!`);
//             expect(() => movies.discardMovie(undefined)).to.throw(`undefined is not at your collection!`);
//             expect(() => movies.discardMovie(true)).to.throw(`true is not at your collection!`);
//         });

//         it('discard valid input', () => {
//             movies.watchMovie('a');
//             expect(movies.discardMovie('a')).to.be.equal('You just threw away a!')
//         });

//         it('try to discard not wathced movie', () => {
//             movies.buyMovie('b', ['e']);
//             expect(() => movies.discardMovie('b')).to.throw('b is not watched!');
//         });
//     });

//     describe('watchMovie', () => {
//         it('Test with movie you don\'t have', () => {
//             expect(() => movies.watchMovie('j')).to.throw('No such movie in your collection!');
//         });

//         it('Test watch function', () => {
//             movies.watchMovie('a');
//             expect(movies.watched['a']).to.be.equal(1);
//             movies.watchMovie('a');
//             expect(movies.watched['a']).to.be.equal(2);
//         });
//     });

//     describe('favouriteMovie', () => {
//         it('test throw error no movies Wathced', () => {
//             let movies2 = new ChristmasMovies();
//             expect(() => movies2.favouriteMovie()).to.throw('You have not watched a movie yet this year!');
//         });

//         it('test favourite Movie', () => {
//             expect(movies.favouriteMovie()).to.be.equal('Your favourite movie is a and you have watched it 2 times!');
//         });
//     });

//     describe('mostStarredActor', () => {
//         let movies2 = new ChristmasMovies();
//         it('test movie collections Error', () => {
//             expect(() => movies2.mostStarredActor()).to.throw('You have not watched a movie yet this year!');
//         });

//         it('test result', () => {
//             movies2.buyMovie('a', ['a']);
//             movies2.buyMovie('b', ['a']);
//             movies2.buyMovie('c', ['b']);
//             expect(movies2.mostStarredActor()).to.be.equal('The most starred actor is a and starred in 2 movies!')
//         });

//     });
// });