class SummerCamp {
    constructor(organaizer, location) {
        this.organaizer = organaizer;
        this.location = location;
        this.priceForTheCamp = {
            child: 150,
            student: 300,
            collegian: 500
        };
        this.listOfParticipants = [{}];
    }

    registerParticipant(name, condition, money) {
        if (!this.priceForTheCamp.hasOwnProperty(condition)) {
            throw new Error("Unsuccessful registration at the camp.");
        }
        if (this.listOfParticipants[0].hasOwnProperty(name)) {
            return `The ${name} is already registered at the camp.`;
        }
        if (money < this.priceForTheCamp[condition]) {
            return  `The money is not enough to pay the stay at the camp.`;
        }


        this.listOfParticipants[0][name] = {
            condition: condition,
            power: 100,
            wins: 0,
        };
        return `The ${name} was successfully registered.`
    }

    unregisterParticipant(name) {
        if (!this.listOfParticipants[0].hasOwnProperty(name)) {
            throw new Error(`The ${name} is not registered in the camp.`);
        }
        delete this.listOfParticipants[0][name];
        return `The ${name} removed successfully.`
    }

    timeToPlay(typeOfGame, participant1, participant2) {
        if (typeOfGame === 'WaterBalloonFights' && participant1 && participant2){
            if (!this.listOfParticipants[0].hasOwnProperty(participant1) || !this.listOfParticipants[0].hasOwnProperty(participant2)) {
                throw new Error(`Invalid entered name/s.`);
            } else if (this.listOfParticipants[0][participant1]['condition'] !== this.listOfParticipants[0][participant2]['condition']) {
                throw new Error(`Choose players with equal condition.`)
            }

            if(this.listOfParticipants[0][participant1]['power'] === this.listOfParticipants[0][participant2]['power']){
                return `There is no winner.`;
            }

            let winner = this.listOfParticipants[0][participant1]['power'] > this.listOfParticipants[0][participant2]['power'] ? participant1 : participant2;
            this.listOfParticipants[0][winner]['wins'] += 1;
            return `The ${winner} is winner in the game ${typeOfGame}.`

            
        } else if (typeOfGame === 'Battleship' && participant1) {
            if (!this.listOfParticipants[0].hasOwnProperty(participant1)) {
                throw new Error(`Invalid entered name/s.`);
            }
            this.listOfParticipants[0][participant1]['power'] += 20;
            return `The ${participant1} successfully completed the game ${typeOfGame}.`
        }
    }

    toString() {
        let nameValuePairs = Object.entries(this.listOfParticipants[0]);
        nameValuePairs = nameValuePairs.sort((a, b)=> b[1]['wins'] - a[1]['wins']);
        let result = [`${this.organaizer} will take ${nameValuePairs.length} participants on camping to ${this.location}`];
        nameValuePairs.forEach(el => {
            result.push(`${el[0]} - ${el[1].condition} - ${el[1].power} - ${el[1].wins}`);
        })
        return result.join('\n');
    }
}

const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp.registerParticipant("Sara Dickinson", "child", 200));
// console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Sara Dickinson"));
console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp.timeToPlay("Battleship", "Dimitur Kostov"));
console.log(summerCamp.timeToPlay("Battleship", "Dimitur Kostov"));
console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));

console.log(summerCamp.toString());