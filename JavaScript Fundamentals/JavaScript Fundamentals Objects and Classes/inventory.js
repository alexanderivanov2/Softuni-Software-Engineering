function inventory(inputArr) {
    function createObj(name, level, items) {
        let obj = {
            name,
            level,
            items,
            info() {
                console.log(`Hero: ${this.name}\nlevel => ${this.level}\nitems => ${this.items}`)
            }
        }
        return obj;
    }

    let arrOfObjs = [];

    for (let el of inputArr) {
        let [name, level, items] = el.split(' / ');
        level = Number(level);

        arrOfObjs.push(createObj(name, level, items));
    }

    arrOfObjs.sort((a, b) => a.level - b.level);
    for (let obj of arrOfObjs) {
        obj.info();
    }
}


inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])