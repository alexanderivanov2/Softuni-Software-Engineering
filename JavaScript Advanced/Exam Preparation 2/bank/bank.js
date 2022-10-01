class Bank {
    constructor(bankName) {
        this._bankName = bankName;
        this.allCustomers = [];
    }

    newCustomer(customer) {
        let result = {...customer};
        let findCustomer = this.allCustomers.find(c => c.personalId == customer.personalId);
        if (findCustomer) {
            throw new Error(`${customer.firstName} ${customer.lastName} is already our customer!`);
        }

        // May have a error! CHECK!!!
        customer.totalMoney = 0;
        customer.transactions = [];
        this.allCustomers.push(customer);
        return result;
    }

    depositMoney(personalId, amount) {
        let findCustomer = this.allCustomers.find(c => c.personalId == personalId);

        if (!findCustomer) {
            throw new Error('We have no customer with this ID!');
        }

        findCustomer.transactions.push(`${findCustomer.firstName} ${findCustomer.lastName} made deposit of ${amount}$!`);
        findCustomer['totalMoney'] += amount;

        return `${findCustomer.totalMoney}$`;
    }

    withdrawMoney(personalId, amount) {
        let findCustomer = this.allCustomers.find(c => c.personalId == personalId);
        if (!findCustomer) {
            throw new Error('We have no customer with this ID!');
        } else if (amount > findCustomer.totalMoney) {
            throw new Error(`${findCustomer.firstName} ${findCustomer.lastName} does not have enough money to withdraw that amount!`);
        }

        findCustomer.transactions.push(`${findCustomer.firstName} ${findCustomer.lastName} withdrew ${amount}$!`);
        findCustomer.totalMoney -= amount;
        return `${findCustomer.totalMoney}$`;
    }

    customerInfo(personalId) {
        let findCustomer = this.allCustomers.find(c => c.personalId == personalId);
        if (!findCustomer) {
            throw new Error('We have no customer with this ID!');
        }

        let result = [
            `Bank name: ${this._bankName}\nCustomer name: ${findCustomer.firstName} ${findCustomer.lastName}\nCustomer ID: ${personalId}\nTotal Money: ${findCustomer.totalMoney}$\nTransactions:`
        ];

        for (let i = findCustomer.transactions.length - 1; i >= 0; i--) {
            result.push(`${i + 1}. ${findCustomer.transactions[i]}`);
        }

        return result.join('\n');
    }

}

let bank = new Bank('SoftUni Bank');

console.log(bank.newCustomer({firstName: 'Svetlin', lastName: 'Nakov', personalId: 6233267}));
console.log(bank.newCustomer({firstName: 'Mihaela', lastName: 'Mileva', personalId: 4151596}));

bank.depositMoney(6233267, 250);
console.log(bank.depositMoney(6233267, 250));
bank.depositMoney(4151596,555);

console.log(bank.withdrawMoney(6233267, 125));

console.log(bank.customerInfo(6233267));