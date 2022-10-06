const { expect } = require('chai');
const { companyAdministration } = require('../companyAdministration.js');

console.log(companyAdministration);

describe('Testing companyAdministration', () => {
    describe('Testing hiringEmployee', () => {
        it('Test throw error for different position', () => {
            expect(() => companyAdministration.hiringEmployee('A', '', 5)).to.throw(`We are not looking for workers for this position.`);
            expect(() => companyAdministration.hiringEmployee('A', 'programmer', 5)).to.throw(`We are not looking for workers for this position.`);
            expect(() => companyAdministration.hiringEmployee('A', true, 5)).to.throw(`We are not looking for workers for this position.`);
            expect(() => companyAdministration.hiringEmployee('A', [], 5)).to.throw(`We are not looking for workers for this position.`);
        });

        it('Test hired for the position', () => {
            expect(companyAdministration.hiringEmployee('A', 'Programmer', 3)).to.be.equal( `A was successfully hired for the position Programmer.`);
            expect(companyAdministration.hiringEmployee('A', 'Programmer', 4)).to.be.equal( `A was successfully hired for the position Programmer.`);
        });

        it('Test not approved position', () => {
            expect(companyAdministration.hiringEmployee('A', 'Programmer', 2)).to.be.equal(`A is not approved for this position.`);
            expect(companyAdministration.hiringEmployee('A', 'Programmer', 1)).to.be.equal(`A is not approved for this position.`);
        });
    });

    describe('Test calculateSalary', () => {
        it('Test invalid hours', () => {
            expect(() => companyAdministration.calculateSalary()).to.throw("Invalid hours");
            expect(() => companyAdministration.calculateSalary('a')).to.throw("Invalid hours");
            expect(() => companyAdministration.calculateSalary(-1)).to.throw("Invalid hours");
            expect(() => companyAdministration.calculateSalary(true)).to.throw("Invalid hours");
            expect(() => companyAdministration.calculateSalary([])).to.throw("Invalid hours");
            expect(() => companyAdministration.calculateSalary({})).to.throw("Invalid hours");
        });

        it ('Test hours paid under 160 hours', () => {
            expect(companyAdministration.calculateSalary(10)).to.be.equal(150);
            expect(companyAdministration.calculateSalary(100)).to.be.equal(1500);
        });

        it('Test hours over 160', () => {
            expect(companyAdministration.calculateSalary(1000)).to.be.equal(16000);
            expect(companyAdministration.calculateSalary(10000)).to.be.equal(151000);
        });
    });

    describe('Test firedEmployee', () => {
        it('test employees is not array', () => {
            expect(() => companyAdministration.firedEmployee()).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee({}, 1)).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee(true, 2)).to.throw("Invalid input");
        });

        it('test index is not number', () => {
            expect(() => companyAdministration.firedEmployee(['a'])).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee(['a', ''])).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee(['a', true])).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee(['a'], [])).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee(['a'], {})).to.throw("Invalid input");
            expect(() => companyAdministration.firedEmployee(['a'], -1)).to.throw("Invalid input");
        });

        it('Test delete employee', () => {
            const employees = ['a', 'b', 'c'];
            const result = 'a, c';
            expect(companyAdministration.firedEmployee(employees, 1)).to.be.equal(result);
        });
    });
});