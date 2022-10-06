class LibraryCollection{
    constructor(capacity) {
        this.capacity = capacity;
        this.books = [];
    }

    addBook(bookName, bookAuthor) {
        if (this.capacity == this.books.length) {
            throw new Error('Not enough space in the collection.');
        }

        const book = {
            bookName,
            bookAuthor,
            payed: false
        };

        this.books.push(book);

        return `The ${bookName}, with an author ${bookAuthor}, collect.`
    }

    payBook(bookName) {
        const book = this.books.find(book => book.bookName == bookName);

        if (!book) {
            throw new Error(`${bookName} is not in the collection.`);
        }

        if (book.payed) {
            throw new Error(`${bookName} has already been paid.`);
        }

        book.payed = true;

        return `${bookName} has been successfully paid.`
    }

    removeBook(bookName) {
        const book = this.books.find(book => book.bookName == bookName);

        if (!book) {
            throw new Error(`The book, you're looking for, is not found.`);
        }

        if (!book.payed) {
            throw new Error(`${bookName} need to be paid before removing from the collection.`);
        }

        const index = this.books.indexOf(book);
        this.books.splice(index, 1);

        return `${bookName} remove from the collection.`
    }

    getStatistics(bookAuthor) {
        const result = [];
        if (bookAuthor) {
            const book = this.books.find(el => el.bookAuthor == bookAuthor);
            if (book) {
                result.push(`${book.bookName} == ${book.bookAuthor} - ${book.payed?'Has Paid':'Not Paid'}.`);
            } else {
                throw new Error(`${bookAuthor} is not in the collection.`);
            }
        } else {
            result.push(`The book collection has ${this.capacity - this.books.length} empty spots left.`);

            const sortedBooks = this.books.sort((a, b) => a.bookName.localeCompare(b.bookName));

            for (let book of sortedBooks) {
                result.push(`${book.bookName} == ${book.bookAuthor} - ${book.payed?'Has Paid':'Not Paid'}.`);
            }
        }

        return result.join('\n');
    }
}


const library = new LibraryCollection(2)
library.addBook('In Search of Lost Time', 'Marcel Proust');
library.addBook('Don Quixote', 'Miguel de Cervantes');
library.payBook('Don Quixote');
console.log(library.removeBook('Don Quixote'));
console.log(library.removeBook('In Search of Lost Time'));