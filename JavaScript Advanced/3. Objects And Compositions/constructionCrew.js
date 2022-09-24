function workerHydrated(obj) {
    let workObj = obj;

    if (workObj.dizziness) {
        workObj.levelOfHydrated = 0.1 * workObj.weight * workObj.experience;
        workObj.dizziness = false;
    }
    return workObj;
}


console.log(workerHydrated({ weight: 80,
    experience: 1,
    levelOfHydrated: 0,
    dizziness: true }));