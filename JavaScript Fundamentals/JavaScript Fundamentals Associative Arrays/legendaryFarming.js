function solve(arr) {
    const needQuantity = 250;
    let legendaryArr = ["shards", "fragments", "motes"];
    let keyMaterials = {
        shards: 0,
        fragments: 0,
        motes: 0
    };
    let otherMaterials = {}
    
    arr = arr.split(' ');

    for (let i = 0; i < arr.length; i += 2) {
        let quantity = Number(arr[i]);
        let material = arr[i + 1].toLowerCase();

        if (legendaryArr.includes(material)) {
            keyMaterials[material] += quantity;
            

            if (keyMaterials[material] >= needQuantity) {
                switch(material) {
                    case 'shards': console.log("Shadowmourne obtained!"); break;
                    case 'fragments': console.log("Valanyr obtained!"); break;
                    case 'motes': console.log("Dragonwrath obtained!"); break;
                }
                keyMaterials[material] -= needQuantity;
                break;
            }
        } else {
            if (otherMaterials.hasOwnProperty(material)) {
                otherMaterials[material] += quantity;
            } else {
                otherMaterials[material] = quantity;
            }
        }
    }

    let sortKeyMaterials = Object.entries(keyMaterials).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
    let sortOtherMaterials = Object.entries(otherMaterials).sort((a, b) => a[0].localeCompare(b[0]));
    
    for (let [key, value] of sortKeyMaterials) {
        console.log(`${key}: ${value}`);
    }

    for (let [key, value] of sortOtherMaterials) {
        console.log(`${key}: ${value}`);
    }
}

solve('3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards');

solve('123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver');