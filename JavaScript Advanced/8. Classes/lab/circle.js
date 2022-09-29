class Circle {
    constructor(radius) {
        this._radius = radius;
    }

    get radius() {
        return this._radius;
    }
    
    set radius(value) {
        if (value < 0) {
            console.log('Error');
        }
        
        this._radius = value;
    }

    get diameter() {
        return this.radius * 2;
    }

    set diameter(n) {
        this.radius = n / 2;
    }

    get area() {
        return Math.PI * this.radius ** 2;
    }

}


let c = new Circle(2);
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);
c.diameter = 1.6;
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);