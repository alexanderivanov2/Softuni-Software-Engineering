function extensibleObject() { 
    const obj = Object.getPrototypeOf(this);
    obj.extend = function(objectParam) {
        Object.entries(objectParam).map(([key, value]) => {
            if (typeof value == 'function') {
                obj[key] = value;
            } else {
                this[key] = value;
            }
        }) 
    }

    return this
} 



const myObj = extensibleObject(); 
console.log(myObj) 
const template = { 
    extensionMethod: function () {}, 
    extensionProperty: 'someString' 
} 
myObj.extend(template); 
console.log(myObj.extensionProperty);