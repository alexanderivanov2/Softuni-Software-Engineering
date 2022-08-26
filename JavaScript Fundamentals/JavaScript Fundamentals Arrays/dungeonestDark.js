function clearDungeon(arr){
    let health = 100;
    let coins = 0;
    let rooms = arr[0].split('|');
    for (let i = 0; i < rooms.length; i++){
        let actionQuantity= rooms[i].split(' ');
        let action = actionQuantity[0];
        let quantity = Number(actionQuantity[1]);
        if (action === 'potion'){
            let healed = quantity;
            if (health === 100) {
                healed = 0;
            } else if (health + healed > 100) {
                healed = 100 - health;
                health = 100;
            } else {
                healed = quantity;
                health += quantity;
            }
            console.log(`You healed for ${healed} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (action === 'chest'){
            coins += quantity;
            console.log(`You found ${quantity} coins.`);
        } else {
            health -= quantity;
            if (health > 0){
                console.log(`You slayed ${action}.`);
            } else {
                console.log(`You died! Killed by ${action}.`);
                console.log(`Best room: ${i + 1}`);
                return;
            }
        }
    }
    console.log("You've made it!");
    console.log(`Coins: ${coins}\nHealth: ${health}`);
}

clearDungeon(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);

clearDungeon(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"]);