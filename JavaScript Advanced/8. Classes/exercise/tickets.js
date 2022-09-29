function solve(input, sortParameter) {
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }
    }
    
    let ticketsArray = [];

    for (let el of input) {
        const [destination, price, status] = el.split('|');
        const ticket = new Ticket(destination, Number(price), status);

        ticketsArray.push(ticket);
    }

    const sortedFunctions = {
        'price': (a, b) => a.price - b.price,
        'destination': (a, b) => a.destination.localeCompare(b.destination),
        'status': (a, b) => a.status.localeCompare(b.status)
    }

    const sortTicketsArray = ticketsArray.sort(sortedFunctions[sortParameter]);
    return sortTicketsArray;
}


console.log(solve(['Philadelphia|94.20|available',
'New York City|95.99|available',
'New York City|95.99|sold',
'Boston|126.20|departed'],
'destination'));

