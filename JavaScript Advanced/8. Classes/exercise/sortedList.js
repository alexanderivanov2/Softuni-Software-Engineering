class List {
    constructor() {
        this.list = []
        this.size = 0;
    }

    checkIndex(index) {
        if (index < 0 || index >= this.size) {
            throw new Error ('Invalid Index');
        }
    }


    add(element) {
        this.list.push(element);
        this.list.sort((a, b) => a - b);
        this.size += 1;
    }

    remove(index) {
        this.checkIndex(index);
        this.list.splice(index, 1);
        this.size -= 1;
    }

    get(index) {
        this.checkIndex(index);
        return this.list[index];
    }
}

let list = new List();


list.add(7);
console.log(list.size);
list.add(6);
list.add(5);
console.log(list.list);
console.log(list.get(1)); 
list.remove(1);
console.log(list.get(1));
console.log(list.size);