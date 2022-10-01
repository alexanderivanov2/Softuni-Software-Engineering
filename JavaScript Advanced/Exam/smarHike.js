const { use } = require("chai");

class SmartHike {
    constructor(username) {
        this.username = username;
        this.goals = {};
        this.listOfHikes = [];
        this.resources = 100;
    }

    addGoal(peak, altitude) {
        if (this.goals.hasOwnProperty(peak)) {
            return `${peak} has already been added to your goals`;
        }

        this.goals[peak] = altitude;

        return `You have successfully added a new goal - ${peak}`;
    }

    hike(peak, time, difficultyLevel) {
        if (!this.goals.hasOwnProperty(peak)) {
            throw new Error(`${peak} is not in your current goals`);
        }

        if (this.resources == 0) {
            throw new Error("You don't have enough resources to start the hike");
        }

        const needResources = time * 10;

        if (this.resources < needResources) {
            return "You don't have enough resources to complete the hike";
        }

        this.resources -= needResources;
        this.listOfHikes.push({peak, time, difficultyLevel});

        return `You hiked ${peak} peak for ${time} hours and you have ${this.resources}% resources left`;
    }

    rest(time) {
        const restedTime = time * 10
        this.resources += restedTime;

        if (this.resources > 100) {
            this.resources = 100;
            return `Your resources are fully recharged. Time for hiking!`
        }

        return `You have rested for ${time} hours and gained ${restedTime}% resources`;
    }

    showRecord(criteria) {
        if (this.listOfHikes.length == 0) {
            return `${this.username} has not done any hiking yet`
        }

        if (criteria == 'easy') {
            const easyHikes = this.listOfHikes.filter(hike => hike.difficultyLevel == criteria);
            if (easyHikes.length == 0) {
                return `${this.username} has not done any ${criteria} hiking yet`;
            }

            const hikingSort = easyHikes.sort((a, b) => a.time - b.time)[0];

            return `${this.username}'s best ${criteria} hike is ${hikingSort.peak} peak, for ${hikingSort.time} hours`;
        } else if (criteria == 'hard') {
            const hardHikes = this.listOfHikes.filter(hike => hike.difficultyLevel == criteria);
            if (hardHikes.length == 0) {
                return `${this.username} has not done any ${criteria} hiking yet`;
            }

            const hikingSort = hardHikes.sort((a, b) => a.time - b.time)[0];

            return `${this.username}'s best ${criteria} hike is ${hikingSort.peak} peak, for ${hikingSort.time} hours`;
        } else if (criteria == 'all') {
            const result = ["All hiking records:"];
            this.listOfHikes.forEach(hike =>{
                result.push(`${this.username} hiked ${hike.peak} for ${hike.time} hours`)
            });

            return result.join('\n');
        }
    }
}

// FIRST
// const user = new SmartHike('Vili');
// console.log(user.addGoal('Musala', 2925));
// console.log(user.addGoal('Rui', 1706));
// console.log(user.addGoal('Musala', 2925));

// You have successfully added a new goal - Musala
// You have successfully added a new goal - Rui 
// Musala has already been added to your goals

// SECOND

// const user = new SmartHike('Vili');
// console.log(user.addGoal('Musala', 2925));
// console.log(user.addGoal('Rui', 1706));
// console.log(user.hike('Musala', 8, 'hard'));
// console.log(user.hike('Rui', 3, 'easy'));
// console.log(user.hike('Everest', 12, 'hard'));

// You have successfully added a new goal - Musala
// You have successfully added a new goal - Rui
// You hiked Musala peak for 8 hours and you have 20% resources left 
// You don’t have enough resources to complete this hike
// Uncaught Error: Everest is not in your current goals

// THIRD

// const user = new SmartHike('Vili');
// console.log(user.addGoal('Musala', 2925));
// console.log(user.hike('Musala', 8, 'hard'));
// console.log(user.rest(4));
// console.log(user.rest(5));

// Output 3
// You have successfully added a new goal - Musala
// You hiked Musala peak for 8 hours and you have 20% resources left 
// You have rested for 4 hours and gained 40% resources 
// Your resources are fully recharged. Time for hiking!

// FOURTH 

// const user = new SmartHike('Vili');
// console.log(user.showRecord('all'));


// Output 4
// Vili has not done any hiking yet

// FIFTH

const user = new SmartHike('Vili');
user.addGoal('Musala', 2925);
user.hike('Musala', 8, 'hard');
console.log(user.showRecord('easy'));
user.addGoal('Vihren', 2914);
user.hike('Vihren', 4, 'hard');
console.log(user.showRecord('hard'));
user.addGoal('Rui', 1706);
user.hike('Rui', 3, 'easy');
console.log(user.showRecord('all'));

// Output 5
// Vili has not done any easy hiking yet
// Vili's best hard hike is Musala peak, for 8 hours
// All hiking records:
// Vili hiked Musala for 8 hours