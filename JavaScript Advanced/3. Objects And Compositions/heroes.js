function solve() {
    let obj = {
        mage(name) {
            let heroMage = {
                name,
                health: 100,
                mana: 100,
                cast(spellName) {
                    this.mana -= 1;
                    console.log(`${this.name} cast ${spellName}`)
                }
            }
            return heroMage;
        },
        fighter(name) {
            let heroFighter = {
                name,
                health: 100,
                stamina: 100,
                fight() {
                    this.stamina -= 1;
                    console.log(`${this.name} slashes at the foe!`);
                }
            }
            return heroFighter;
        }
    }
    return obj;
}

let create = solve();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball")
scorcher.cast("thunder")
scorcher.cast("light")

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight()

console.log(scorcher2.stamina);
console.log(scorcher.mana);