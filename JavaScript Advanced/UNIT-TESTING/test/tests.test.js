let { Repository } = require("../repository/solution.js");
let { expect, assert } = require('chai');

describe("Test Repository", function () {
    describe("instantiation test", function () {
        it("constructor Test", function () {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            expect(repository.props).to.be.equal(properties);
            expect(repository.props.name).to.be.equal('string');
            expect(repository.props.age).to.be.equal('number');
            expect(repository.props.birthday).to.be.equal('object');
            expect(typeof repository.data).to.be.equal('object');
            expect(repository.nextId()).to.be.equal(0);
            expect(repository instanceof Repository).to.be.equal(true);
            expect(typeof repository).to.be.equal('object');
            assert.deepEqual(repository.data, new Map);
        });

        it('count function', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);

            expect(repository.count).to.be.equal(0);
        });

        it('Validate', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 1,
                age: 22,
                birthday: new Date(1998, 0, 7)
            }

            expect(() => repository.add({age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is missing from the entity!');
            expect(() => repository.add({name: '22', birthday: new Date(1998, 0, 7)})).to.throw('Property age is missing from the entity!');
            expect(() => repository.add({name: 22, age: 22})).to.throw('Property birthday is missing from the entity!');

            expect(() => repository.add({name: 12,age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is not of correct type!');
            expect(() => repository.add({name: true,age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is not of correct type!');
            expect(() => repository.add({name: [],age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is not of correct type!');
            expect(() => repository.add({name: undefined,age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is not of correct type!');
            expect(() => repository.add({name: NaN,age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is not of correct type!');
            expect(() => repository.add({name: null,age: 22, birthday: new Date(1998, 0, 7)})).to.throw('Property name is not of correct type!');

            expect(() => repository.add({name: '22', age: '22',birthday: new Date(1998, 0, 7)})).to.throw('Property age is not of correct type!');
            expect(() => repository.add({name: '22', age: true,birthday: new Date(1998, 0, 7)})).to.throw('Property age is not of correct type!');
            expect(() => repository.add({name: '22', age: [],birthday: new Date(1998, 0, 7)})).to.throw('Property age is not of correct type!');
            expect(() => repository.add({name: '22', age: null,birthday: new Date(1998, 0, 7)})).to.throw('Property age is not of correct type!');
            expect(() => repository.add({name: '22', age: undefined,birthday: new Date(1998, 0, 7)})).to.throw('Property age is not of correct type!');
            
            expect(() => repository.add({name: 'a', age: 22, birthday: 1})).to.throw('Property birthday is not of correct type!');
            expect(() => repository.add({name: 'a', age: 22, birthday: '2' })).to.throw('Property birthday is not of correct type!');
            expect(() => repository.add({name: 'a', age: 22, birthday: true})).to.throw('Property birthday is not of correct type!');
            expect(() => repository.add({name: 'a', age: 22, birthday: undefined})).to.throw('Property birthday is not of correct type!');
        });

        it('test add', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }

            expect(repository.add(entity)).to.be.equal(0);
            expect(repository.add(entity)).to.be.equal(1);
            expect(repository.count).to.be.equal(2);
        });

        it('test get id with invalid id', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }
            repository.add(entity);
            repository.add(entity);

            expect(() => repository.getId(3)).to.throw('Entity with id: 3 does not exist!');
            expect(() => repository.getId(5)).to.throw('Entity with id: 5 does not exist!')
        });

        it('test get id', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }
            repository.add(entity);
            repository.add(entity);

            assert.deepEqual(repository.getId(0), { name: 'Pesho', age: 22, birthday: new Date(1998, 0, 7) });
            expect(repository.getId(0)).to.be.equal(repository.data.get(0));
            expect(repository.getId(1)).to.be.equal(repository.data.get(1));
        });

        it('update invalid id', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }
            let newEntity = {
                name: 'Gosho',
                age: 23,
                birthday: new Date(1998, 0, 7)
            }
            repository.add(entity);
            repository.add(entity);
            assert.throws(function () { repository.update(0, { name: ['test'], age: 18, birthday: new Date(1995, 13, 08) }) }, TypeError, `Property name is not of correct type!`);
            assert.throws(function () { repository.update(0, { name: 'Kik', age: 'test', birthday: new Date(1995, 13, 08) }) }, TypeError, `Property age is not of correct type!`);
            assert.throws(function () { repository.update(0, { name: 'Kiko', town: 'Sofia', birthday: new Date(1995, 13, 08) }) }, Error, `Property age is missing from the entity!`);
            expect(() => repository.update(3, newEntity)).to.throw('Entity with id: 3 does not exist!')
        });

        it('update id', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }
            let newEntity = {
                name: 'Gosho',
                age: 23,
                birthday: new Date(1998, 0, 7)
            }
            repository.add(entity);
            repository.add(entity);
            repository.update(1, newEntity)

            expect(repository.data.get(1)).to.be.equal(newEntity);
        });

        it('delete invalid id', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }
            let newEntity = {
                name: 'Gosho',
                age: 23,
                birthday: new Date(1998, 0, 7)
            }
            repository.add(entity);
            repository.add(entity);

            expect(() => repository.del(3)).to.throw('Entity with id: 3 does not exist!')
        });

        it('delete id', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: 'Pesho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            }
            let newEntity = {
                name: 'Gosho',
                age: 23,
                birthday: new Date(1998, 0, 7)
            }
            repository.add(entity);
            repository.add(entity);
            
            repository.del(1);
            expect(() => repository.getId(1)).to.throw('Entity with id: 1 does not exist!');
            expect(repository.count).to.be.equal(1);
        });
    });
});
