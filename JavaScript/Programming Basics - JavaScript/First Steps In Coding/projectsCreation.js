function projectsCreation(input){
    let name = input[0];
    let numOfProjects = Number(input[1]);
    let neededHours = numOfProjects * 3;
    console.log(`The architect ${name} will need ${neededHours} hours to complete ${numOfProjects} project/s.`);
}

projectsCreation(['George', '12'])