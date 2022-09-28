function cars(arr) {
    let carsObjs = {};

    let objFunctions = {
        create: (createName) => {
            carsObjs[createName] = {}
        },
        inherit: (createName, inheritName) => {
            carsObjs[createName] = {};
            let carObj = carsObjs[createName];
            Object.setPrototypeOf(carObj, carsObjs[inheritName]);
        },
        set: (carName, keyName, value) => {
            carsObjs[carName][keyName] = value;
        },
        print: (carName) => {
            let print = [];
            for (let key in carsObjs[carName]) {
                print.push(`${key}:${carsObjs[carName][key]}`);
            }
            console.log(print.join(','));
        }
    }

    for (let txt of arr) {
        let [action, ...other] = txt.split(' ');
        if (action === 'create') { 
            if (other[1] === 'inherit') {
                objFunctions.inherit(other[0], other[2]);
            } else {
                objFunctions.create(other[0]);
            }
        } else if (action == 'set') {
            objFunctions.set(other[0],other[1],other[2]);
        } else if (action == 'print') {
            objFunctions.print(other[0]);
        }
    }

}


cars(['create c1',
'create c2 inherit c1',
'set c1 color red',
'set c2 model new',
'print c1',
'print c2']);