let pattern = /@(?<name>[A-Za-z]+)[^\@\-\!\:\>]*:(?<population>\d+)[^\@\-\!\:\>]*!(?<action>[AD])![^\@\-\!\:\>]*->(?<soldiers>\d+)/g;

let text = 'PQ@Alderaa1:30000!A!->20000';
let match = pattern.exec(text);
console.log(match);
let {name, population, action, soldiers} = match.groups;

console.log(name, action);