function createHeroicInventory(input) {
    let inventory = [];
    for (let el of input) {
        let hero = {};
        let [name, level, items] = el.split(' / ');
        hero.name  = name;
        hero.level = Number(level);
        hero.items = items ? items.split(', ') : [];
        inventory.push(hero);
    }

    return JSON.stringify(inventory);
}

console.log(createHeroicInventory(['Isacc / 25 / Apple, GravityGun',
'Derek / 12 / BarrelVest, DestructionSword',
'Hes / 1 / Desolator, Sentinel, Antara']));