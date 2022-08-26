function tsteamAcc(arr) {
    let games = arr[0].split(' ');
    let workArr = arr.slice(1, arr.length);
    let index = 0
    let [action, game] = workArr[index].split(' ');
    while (action !== 'Play!') {
        if (action === 'Install' && !games.includes(game)) {
            games.push(game);
        } else if (action === 'Uninstall' && games.includes(game)){
            let index = games.indexOf(game);
            games.splice(index, 1);
        } else if (action === 'Update' && games.includes(game)){
            let index = games.indexOf(game);
            games.splice(index, 1);
            games.push(game);
        } else if ( action === 'Expansion') {
            let [name, expansion] = game.split('-');
            if (games.includes(name)){
                let index = games.indexOf(name);
                games.splice(index + 1, 0, `${name}:${expansion}`);
            }
        }
        
        
        index += 1;
        if (workArr[index] !== 'Play!') {
            [action, game] = workArr[index].split(' ');
        } else {
            action = workArr[index];
        }
    }
    console.log(games.join(' '));
}

tsteamAcc(['CS WoW Diablo',
'Install LoL',
'Uninstall WoW',
'Update Diablo',
'Expansion CS-Go',
'Play!']);