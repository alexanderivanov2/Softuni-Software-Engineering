function printLoadingBar(loadProcent) {
    let loadProcentSigns = loadProcent / 10;
    let procentage = `${loadProcent}%`
    let bar = `[${'%'.repeat(loadProcentSigns)}${'.'.repeat(10 - loadProcentSigns)}]`;
    let message = loadProcentSigns === 10 ? '100% Complete!' : 'Still loading...';
    
    if (loadProcentSigns === 10) {
        console.log(message)
    }  else {
        console.log(`${procentage} ${bar}\n${message}`);
    }
}


printLoadingBar(30);
printLoadingBar(100);
