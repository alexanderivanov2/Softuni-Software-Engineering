function gladiatorInventory(input) {
    let arr = input.shift().split(' ');
    for (let el of input) {
        let [action, equipment] = el.split(' ');

        if (action === 'Buy' && arr.includes(equipment) === false) {
            arr.push(equipment);
        } else if (action === "Trash" && arr.includes(equipment)) {
            arr.splice(arr.indexOf(equipment), 1);
        } else if (action === 'Repair' && arr.includes(equipment)) {
            let getEquipment = arr.splice(arr.indexOf(equipment), 1);
            arr.push(getEquipment[0]);
        } else if (action === 'Upgrade') {
            let [equipment2, upgrade] = equipment.split('-');
            if (arr.includes(equipment2)) {
                arr.splice(arr.indexOf(equipment2) + 1, 0, `${equipment2}:${upgrade}`);
            }
        }
    }
    console.log(arr.join(' '));
}

gladiatorInventory(['SWORD Shield Spear',
'Buy Bag',
'Trash Shield',
'Repair Spear',
'Upgrade SWORD-Steel']);